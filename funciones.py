"""
funciones.py

Funciones auxiliares del sistema de auditoría.

Este archivo:
- Construye los expedientes a partir de cuestionario.py.
- Consulta resultados de dimensiones y subdimensiones.
- No contiene interfaz gráfica.
"""

from cuestionario import DIMENSIONES
from modelo import Auditoria, Expediente


# ==========================================================
# CREACIÓN DE LA AUDITORÍA
# ==========================================================

def inicializar_expedientes(auditoria: Auditoria) -> None:
    """
    Crea todos los expedientes de la auditoría y agrega
    las dimensiones configuradas en cuestionario.py.
    """

    auditoria.expedientes.clear()

    for numero in range(1, auditoria.total_expedientes + 1):

        expediente = Expediente(numero)

        for dimension in DIMENSIONES.values():
            expediente.agregar_dimension(dimension)

        auditoria.expedientes.append(expediente)


# ==========================================================
# CONSULTAS DEL CUESTIONARIO
# ==========================================================

def obtener_dimension(dimension_id: str) -> dict:
    """Devuelve la configuración de una dimensión."""

    return DIMENSIONES[dimension_id]


def obtener_subdimensiones(dimension_id: str) -> dict:
    """Devuelve las subdimensiones de una dimensión."""

    return DIMENSIONES[dimension_id]["subdimensiones"]


def obtener_subdimension(
    dimension_id: str,
    subdimension_id: str,
) -> dict:
    """Devuelve la configuración de una subdimensión."""

    return obtener_subdimensiones(dimension_id)[subdimension_id]


def lista_criterios_subdimension(
    dimension_id: str,
    subdimension_id: str,
) -> list[dict]:
    """Devuelve los criterios de una subdimensión."""

    return obtener_subdimension(
        dimension_id,
        subdimension_id,
    )["criterios"]


def total_criterios_subdimension(
    dimension_id: str,
    subdimension_id: str,
) -> int:
    """Cuenta los criterios de una subdimensión."""

    return len(
        lista_criterios_subdimension(
            dimension_id,
            subdimension_id,
        )
    )


def total_criterios_dimension(dimension_id: str) -> int:
    """Cuenta todos los criterios de una dimensión."""

    return sum(
        len(subdimension["criterios"])
        for subdimension in obtener_subdimensiones(
            dimension_id
        ).values()
    )


# ==========================================================
# RESULTADOS DE UNA SUBDIMENSIÓN
# ==========================================================

def resultado_subdimension(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
):
    """Devuelve el objeto de resultados de una subdimensión."""

    return expediente.dimensiones[
        dimension_id
    ].subdimensiones[subdimension_id]


def porcentaje_subdimension(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
) -> float:
    """
    Devuelve el porcentaje usado para comparar con la meta.

    En metas del tipo máximo devuelve el porcentaje
    de incumplimiento. En las demás devuelve cumplimiento.
    """

    return resultado_subdimension(
        expediente,
        dimension_id,
        subdimension_id,
    ).porcentaje


def porcentaje_cumplimiento_subdimension(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
) -> float:
    """Devuelve el porcentaje de criterios que cumplen."""

    return resultado_subdimension(
        expediente,
        dimension_id,
        subdimension_id,
    ).porcentaje_cumplimiento


def criterios_respondidos_subdimension(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
) -> int:
    """Devuelve el número de criterios contestados."""

    return resultado_subdimension(
        expediente,
        dimension_id,
        subdimension_id,
    ).respondidos


def subdimension_completa(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
) -> bool:
    """Indica si todos los criterios fueron contestados."""

    return resultado_subdimension(
        expediente,
        dimension_id,
        subdimension_id,
    ).completo


def subdimension_cumple(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
) -> bool:
    """Indica si la subdimensión alcanza su meta."""

    return resultado_subdimension(
        expediente,
        dimension_id,
        subdimension_id,
    ).cumple_meta


def estado_subdimension(
    expediente: Expediente,
    dimension_id: str,
    subdimension_id: str,
) -> str:
    """Devuelve el estado del semáforo."""

    return resultado_subdimension(
        expediente,
        dimension_id,
        subdimension_id,
    ).estado


# ==========================================================
# RESULTADOS DE UNA DIMENSIÓN
# ==========================================================

def resultado_dimension(
    expediente: Expediente,
    dimension_id: str,
):
    """Devuelve el objeto de resultados de una dimensión."""

    return expediente.dimensiones[dimension_id]


def porcentaje_dimension(
    expediente: Expediente,
    dimension_id: str,
) -> float:
    """Devuelve el cumplimiento general de la dimensión."""

    return resultado_dimension(
        expediente,
        dimension_id,
    ).porcentaje_cumplimiento


def criterios_respondidos_dimension(
    expediente: Expediente,
    dimension_id: str,
) -> int:
    """Devuelve los criterios contestados de una dimensión."""

    return resultado_dimension(
        expediente,
        dimension_id,
    ).criterios_respondidos


def dimension_completa(
    expediente: Expediente,
    dimension_id: str,
) -> bool:
    """Indica si toda la dimensión está contestada."""

    return resultado_dimension(
        expediente,
        dimension_id,
    ).completo


def dimension_cumple(
    expediente: Expediente,
    dimension_id: str,
) -> bool:
    """
    Indica si todas las subdimensiones evaluables
    alcanzan sus metas.
    """

    return resultado_dimension(
        expediente,
        dimension_id,
    ).cumple


def estado_dimension(
    expediente: Expediente,
    dimension_id: str,
) -> str:
    """Devuelve el estado general de la dimensión."""

    return resultado_dimension(
        expediente,
        dimension_id,
    ).estado


# ==========================================================
# RESULTADOS DEL EXPEDIENTE
# ==========================================================

def progreso_expediente(expediente: Expediente) -> float:
    """
    Devuelve la completitud de captura del expediente.

    Este resultado no representa calidad ni cumplimiento.
    """

    return expediente.porcentaje_completitud


def resultado_general(expediente: Expediente) -> float:
    """Devuelve el porcentaje global de cumplimiento."""

    return expediente.porcentaje_global


def expediente_completo(expediente: Expediente) -> bool:
    """Indica si todas las preguntas fueron contestadas."""

    return expediente.completo


# ==========================================================
# RESULTADOS DE LA AUDITORÍA
# ==========================================================

def promedio_auditoria(auditoria: Auditoria) -> float:
    """Devuelve el cumplimiento global de toda la auditoría."""

    return auditoria.porcentaje_global