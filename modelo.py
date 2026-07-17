"""
modelo.py

Modelo de datos del sistema de auditoría.

Reglas principales:
- Todos los criterios tienen el mismo peso.
- "No aplica" se excluye del cálculo.
- "Sin responder" no entra en el cálculo.
- Las metas pueden ser:
    * "igual": el resultado debe ser exactamente igual a la meta.
    * "minimo": el resultado debe ser mayor o igual a la meta.
    * "maximo": el porcentaje de incumplimientos debe ser menor
      o igual a la meta.
"""

from dataclasses import dataclass, field
from datetime import datetime


RESPUESTAS_VALIDAS = {
    "Sin responder",
    "Cumple",
    "No cumple",
    "No aplica",
}


# ==========================================================
# RESPUESTA
# ==========================================================

@dataclass
class Respuesta:
    """Representa la respuesta de un criterio."""

    criterio_id: str
    valor: str = "Sin responder"
    fecha: datetime | None = None

    def responder(self, valor: str) -> None:
        """Guarda una respuesta válida y registra la fecha."""

        if valor not in RESPUESTAS_VALIDAS:
            raise ValueError(
                f"Respuesta no válida para {self.criterio_id}: {valor}"
            )

        self.valor = valor
        self.fecha = datetime.now()


# ==========================================================
# SUBDIMENSIÓN
# ==========================================================

@dataclass
class SubdimensionResultado:
    """Agrupa las respuestas y resultados de una subdimensión."""

    id: str
    titulo: str
    porcentaje_ideal: float
    tipo_meta: str = "minimo"

    respuestas: dict[str, Respuesta] = field(default_factory=dict)

    def __post_init__(self) -> None:
        tipos_validos = {"igual", "minimo", "maximo"}

        if self.tipo_meta not in tipos_validos:
            raise ValueError(
                f"Tipo de meta no válido en {self.id}: "
                f"{self.tipo_meta}. Debe ser igual, minimo o maximo."
            )

        if not 0 <= self.porcentaje_ideal <= 100:
            raise ValueError(
                f"El porcentaje ideal de {self.id} debe estar "
                "entre 0 y 100."
            )

    def agregar_criterio(self, criterio_id: str) -> None:
        """Crea un criterio vacío dentro de la subdimensión."""

        if criterio_id in self.respuestas:
            raise ValueError(
                f"El criterio {criterio_id} está duplicado."
            )

        self.respuestas[criterio_id] = Respuesta(
            criterio_id=criterio_id
        )

    def responder(
        self,
        criterio_id: str,
        valor: str,
    ) -> None:
        """Registra la respuesta de un criterio."""

        if criterio_id not in self.respuestas:
            raise KeyError(
                f"El criterio {criterio_id} no pertenece "
                f"a la subdimensión {self.id}."
            )

        self.respuestas[criterio_id].responder(valor)

    def obtener_respuesta(self, criterio_id: str) -> str:
        """Devuelve el valor actual de un criterio."""

        if criterio_id not in self.respuestas:
            raise KeyError(
                f"El criterio {criterio_id} no existe en {self.id}."
            )

        return self.respuestas[criterio_id].valor

    @property
    def total(self) -> int:
        """Número total de criterios."""

        return len(self.respuestas)

    @property
    def respondidos(self) -> int:
        """
        Número de criterios contestados.

        Incluye Cumple, No cumple y No aplica.
        """

        return sum(
            respuesta.valor != "Sin responder"
            for respuesta in self.respuestas.values()
        )

    @property
    def sin_responder(self) -> int:
        """Número de criterios pendientes."""

        return self.total - self.respondidos

    @property
    def no_aplica(self) -> int:
        """Número de criterios marcados como No aplica."""

        return sum(
            respuesta.valor == "No aplica"
            for respuesta in self.respuestas.values()
        )

    @property
    def evaluables(self) -> int:
        """
        Número de criterios que participan en el porcentaje.

        Solo incluye Cumple y No cumple.
        """

        return sum(
            respuesta.valor in {"Cumple", "No cumple"}
            for respuesta in self.respuestas.values()
        )

    @property
    def cumplen(self) -> int:
        """Número de criterios que cumplen."""

        return sum(
            respuesta.valor == "Cumple"
            for respuesta in self.respuestas.values()
        )

    @property
    def no_cumplen(self) -> int:
        """Número de criterios que no cumplen."""

        return sum(
            respuesta.valor == "No cumple"
            for respuesta in self.respuestas.values()
        )

    @property
    def porcentaje_completitud(self) -> float:
        """
        Porcentaje de preguntas contestadas.

        Este dato solo representa avance de captura.
        No determina el resultado del análisis.
        """

        if self.total == 0:
            return 0.0

        return round(
            self.respondidos / self.total * 100,
            2,
        )

    @property
    def porcentaje_cumplimiento(self) -> float:
        """
        Porcentaje de criterios evaluables que cumplen.

        Los criterios No aplica se excluyen.
        """

        if self.evaluables == 0:
            return 0.0

        return round(
            self.cumplen / self.evaluables * 100,
            2,
        )

    @property
    def porcentaje_incumplimiento(self) -> float:
        """
        Porcentaje de criterios evaluables que no cumplen.

        Se utiliza para indicadores del tipo "máximo", como:
        - Menor o igual al 10%.
        - 0% de errores.
        """

        if self.evaluables == 0:
            return 0.0

        return round(
            self.no_cumplen / self.evaluables * 100,
            2,
        )

    @property
    def porcentaje(self) -> float:
        """
        Resultado que se compara con la meta.

        Para metas "igual" o "minimo":
            usa el porcentaje de cumplimiento.

        Para metas "maximo":
            usa el porcentaje de incumplimiento.
        """

        if self.tipo_meta == "maximo":
            return self.porcentaje_incumplimiento

        return self.porcentaje_cumplimiento

    @property
    def completo(self) -> bool:
        """Indica si todos los criterios fueron contestados."""

        return self.total > 0 and self.respondidos == self.total

    @property
    def evaluable(self) -> bool:
        """
        Indica si existe al menos un criterio evaluable.

        Una subdimensión con todos los criterios en No aplica
        se considera no evaluable.
        """

        return self.evaluables > 0

    @property
    def cumple_meta(self) -> bool:
        """Compara el resultado con la meta configurada."""

        if not self.evaluable:
            return False

        if self.tipo_meta == "igual":
            return self.porcentaje == self.porcentaje_ideal

        if self.tipo_meta == "minimo":
            return self.porcentaje >= self.porcentaje_ideal

        return self.porcentaje <= self.porcentaje_ideal

    @property
    def estado(self) -> str:
        """Devuelve el resultado para el semáforo."""

        if not self.completo:
            return "⚪ Pendiente"

        if not self.evaluable:
            return "⚪ No evaluable"

        if self.cumple_meta:
            return "🟢 Cumple"

        return "🔴 Insuficiente"

    @property
    def descripcion_meta(self) -> str:
        """Devuelve la meta en un formato legible."""

        simbolos = {
            "igual": "=",
            "minimo": "≥",
            "maximo": "≤",
        }

        simbolo = simbolos[self.tipo_meta]

        return f"{simbolo} {self.porcentaje_ideal:g}%"


# ==========================================================
# DIMENSIÓN
# ==========================================================

@dataclass
class DimensionResultado:
    """Agrupa las subdimensiones de una dimensión."""

    id: str
    titulo: str

    subdimensiones: dict[str, SubdimensionResultado] = field(
        default_factory=dict
    )

    def agregar_subdimension(
        self,
        subdimension: SubdimensionResultado,
    ) -> None:
        """Agrega una subdimensión a la dimensión."""

        if subdimension.id in self.subdimensiones:
            raise ValueError(
                f"La subdimensión {subdimension.id} está duplicada "
                f"en la dimensión {self.id}."
            )

        self.subdimensiones[subdimension.id] = subdimension

    def responder(
        self,
        subdimension_id: str,
        criterio_id: str,
        valor: str,
    ) -> None:
        """Registra una respuesta dentro de una subdimensión."""

        if subdimension_id not in self.subdimensiones:
            raise KeyError(
                f"La subdimensión {subdimension_id} no pertenece "
                f"a la dimensión {self.id}."
            )

        self.subdimensiones[subdimension_id].responder(
            criterio_id,
            valor,
        )

    @property
    def total_criterios(self) -> int:
        """Número total de criterios de la dimensión."""

        return sum(
            subdimension.total
            for subdimension in self.subdimensiones.values()
        )

    @property
    def criterios_respondidos(self) -> int:
        """Número total de criterios contestados."""

        return sum(
            subdimension.respondidos
            for subdimension in self.subdimensiones.values()
        )

    @property
    def criterios_evaluables(self) -> int:
        """Número total de criterios evaluables."""

        return sum(
            subdimension.evaluables
            for subdimension in self.subdimensiones.values()
        )

    @property
    def criterios_cumplen(self) -> int:
        """Número total de criterios que cumplen."""

        return sum(
            subdimension.cumplen
            for subdimension in self.subdimensiones.values()
        )

    @property
    def porcentaje_completitud(self) -> float:
        """Avance de captura de la dimensión."""

        if self.total_criterios == 0:
            return 0.0

        return round(
            self.criterios_respondidos
            / self.total_criterios
            * 100,
            2,
        )

    @property
    def porcentaje_cumplimiento(self) -> float:
        """
        Cumplimiento general de la dimensión.

        Todos los criterios tienen el mismo peso,
        independientemente de su subdimensión.
        """

        if self.criterios_evaluables == 0:
            return 0.0

        return round(
            self.criterios_cumplen
            / self.criterios_evaluables
            * 100,
            2,
        )

    @property
    def porcentaje(self) -> float:
        """Alias del cumplimiento general de la dimensión."""

        return self.porcentaje_cumplimiento

    @property
    def completo(self) -> bool:
        """Indica si todas las subdimensiones están contestadas."""

        return (
            len(self.subdimensiones) > 0
            and all(
                subdimension.completo
                for subdimension in self.subdimensiones.values()
            )
        )

    @property
    def cumple(self) -> bool:
        """
        Una dimensión cumple cuando todas sus subdimensiones
        evaluables alcanzan su meta.
        """

        subdimensiones_evaluables = [
            subdimension
            for subdimension in self.subdimensiones.values()
            if subdimension.evaluable
        ]

        if not subdimensiones_evaluables:
            return False

        return all(
            subdimension.cumple_meta
            for subdimension in subdimensiones_evaluables
        )

    @property
    def estado(self) -> str:
        """Estado general de la dimensión."""

        if not self.completo:
            return "⚪ Pendiente"

        if self.cumple:
            return "🟢 Cumple"

        return "🔴 Insuficiente"


# ==========================================================
# EXPEDIENTE
# ==========================================================

class Expediente:
    """Representa un expediente auditado."""

    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.dimensiones: dict[str, DimensionResultado] = {}

    def agregar_dimension(
        self,
        informacion: dict,
    ) -> None:
        """
        Crea una dimensión usando la configuración
        declarada en cuestionario.py.
        """

        dimension_id = informacion["id"]

        if dimension_id in self.dimensiones:
            raise ValueError(
                f"La dimensión {dimension_id} está duplicada."
            )

        dimension = DimensionResultado(
            id=dimension_id,
            titulo=informacion["titulo"],
        )

        for subdimension_info in informacion[
            "subdimensiones"
        ].values():

            subdimension = SubdimensionResultado(
                id=subdimension_info["id"],
                titulo=subdimension_info["titulo"],
                porcentaje_ideal=subdimension_info[
                    "porcentaje_ideal"
                ],
                tipo_meta=subdimension_info.get(
                    "tipo_meta",
                    "minimo",
                ),
            )

            for criterio in subdimension_info["criterios"]:
                subdimension.agregar_criterio(
                    criterio["id"]
                )

            dimension.agregar_subdimension(
                subdimension
            )

        self.dimensiones[dimension_id] = dimension

    def responder(
        self,
        dimension_id: str,
        subdimension_id: str,
        criterio_id: str,
        valor: str,
    ) -> None:
        """Registra una respuesta dentro del expediente."""

        if dimension_id not in self.dimensiones:
            raise KeyError(
                f"La dimensión {dimension_id} no existe "
                f"en el expediente {self.numero}."
            )

        self.dimensiones[dimension_id].responder(
            subdimension_id,
            criterio_id,
            valor,
        )

    @property
    def total_criterios(self) -> int:
        return sum(
            dimension.total_criterios
            for dimension in self.dimensiones.values()
        )

    @property
    def criterios_respondidos(self) -> int:
        return sum(
            dimension.criterios_respondidos
            for dimension in self.dimensiones.values()
        )

    @property
    def criterios_evaluables(self) -> int:
        return sum(
            dimension.criterios_evaluables
            for dimension in self.dimensiones.values()
        )

    @property
    def criterios_cumplen(self) -> int:
        return sum(
            dimension.criterios_cumplen
            for dimension in self.dimensiones.values()
        )

    @property
    def porcentaje_completitud(self) -> float:
        """Avance de captura del expediente."""

        if self.total_criterios == 0:
            return 0.0

        return round(
            self.criterios_respondidos
            / self.total_criterios
            * 100,
            2,
        )

    @property
    def porcentaje_global(self) -> float:
        """
        Porcentaje global de criterios que cumplen.

        Todos los criterios evaluables tienen el mismo peso.
        """

        if self.criterios_evaluables == 0:
            return 0.0

        return round(
            self.criterios_cumplen
            / self.criterios_evaluables
            * 100,
            2,
        )

    @property
    def completo(self) -> bool:
        return (
            len(self.dimensiones) > 0
            and all(
                dimension.completo
                for dimension in self.dimensiones.values()
            )
        )


# ==========================================================
# AUDITORÍA
# ==========================================================

class Auditoria:
    """Contiene todos los expedientes de la auditoría."""

    def __init__(self, total_expedientes: int) -> None:

        if not 1 <= total_expedientes <= 29:
            raise ValueError(
                "El número de expedientes debe estar entre 1 y 29."
            )

        self.total_expedientes = total_expedientes
        self.expedientes: list[Expediente] = []
        self.expediente_actual = 0

    @property
    def expediente(self) -> Expediente:
        """Devuelve el expediente que se está capturando."""

        if not self.expedientes:
            raise IndexError(
                "La auditoría todavía no contiene expedientes."
            )

        return self.expedientes[self.expediente_actual]

    @property
    def numero_expediente_actual(self) -> int:
        return self.expediente_actual + 1

    @property
    def ultimo(self) -> bool:
        return (
            self.expediente_actual
            == self.total_expedientes - 1
        )

    def siguiente(self) -> bool:
        """Avanza al expediente siguiente."""

        if self.ultimo:
            return False

        self.expediente_actual += 1
        return True

    def anterior(self) -> bool:
        """Regresa al expediente anterior."""

        if self.expediente_actual == 0:
            return False

        self.expediente_actual -= 1
        return True

    @property
    def porcentaje_global(self) -> float:
        """Promedio global de todos los expedientes."""

        evaluables = sum(
            expediente.criterios_evaluables
            for expediente in self.expedientes
        )

        if evaluables == 0:
            return 0.0

        cumplen = sum(
            expediente.criterios_cumplen
            for expediente in self.expedientes
        )

        return round(
            cumplen / evaluables * 100,
            2,
        )