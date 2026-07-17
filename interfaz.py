"""
interfaz.py

Interfaz gráfica del sistema de auditoría.

Compatible con:
- modelo.py
- funciones.py
- cuestionario.py
"""

import streamlit as st

from cuestionario import DIMENSIONES
from funciones import (
    estado_dimension,
    estado_subdimension,
    progreso_expediente,
    resultado_general,
)

RESPUESTAS = [
    "Sin responder",
    "Cumple",
    "No cumple",
    "No aplica",
]


# ==========================================================
# TÍTULO
# ==========================================================

def encabezado():

    st.title("Sistema de Auditoría")

    st.divider()


# ==========================================================
# PROGRESO
# ==========================================================

def mostrar_progreso(expediente):

    porcentaje = progreso_expediente(expediente)

    st.progress(porcentaje / 100)

    st.caption(
        f"Completitud del expediente: {porcentaje:.1f}%"
    )


# ==========================================================
# CRITERIO
# ==========================================================

def mostrar_criterio(
    expediente,
    dimension_id,
    subdimension_id,
    criterio,
):

    criterio_id = str(criterio["id"])
    texto_criterio = str(criterio.get("texto", ""))

    respuesta = expediente.dimensiones[
        dimension_id
    ].subdimensiones[
        subdimension_id
    ].obtener_respuesta(
        criterio_id
    )

    if respuesta not in RESPUESTAS:
        respuesta = "Sin responder"

    indice = RESPUESTAS.index(respuesta)

    valor = st.selectbox(
        label=texto_criterio,
        options=RESPUESTAS,
        index=indice,
        key=(
            f"exp_{expediente.numero}_"
            f"{dimension_id}_{subdimension_id}_{criterio_id}"
        ),
    )

    if valor != respuesta:

        expediente.responder(
            dimension_id,
            subdimension_id,
            criterio_id,
            valor,
        )

    descripcion = criterio.get("descripcion", "")

    if descripcion:

        with st.expander("Descripción"):

            st.write(
                str(descripcion)
            )
# ==========================================================
# SUBDIMENSIÓN
# ==========================================================

def mostrar_subdimension(
    expediente,
    dimension_id,
    subdimension_id,
    subdimension,
):

    st.subheader(subdimension["titulo"])

    meta = (
        f'Meta: '
        f'{subdimension["tipo_meta"]} '
        f'{subdimension["porcentaje_ideal"]}%'
    )

    # Mostrar la meta de una forma más legible
    if subdimension["tipo_meta"] == "igual":
        meta = f"Meta: = {subdimension['porcentaje_ideal']}%"
    elif subdimension["tipo_meta"] == "minimo":
        meta = f"Meta: ≥ {subdimension['porcentaje_ideal']}%"
    elif subdimension["tipo_meta"] == "maximo":
        meta = f"Meta: ≤ {subdimension['porcentaje_ideal']}%"

    st.caption(meta)

    for criterio in subdimension["criterios"]:

        mostrar_criterio(

            expediente,

            dimension_id,

            subdimension_id,

            criterio,

        )

    resultado = expediente.dimensiones[
        dimension_id
    ].subdimensiones[
        subdimension_id
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Cumplimiento",

            f"{resultado.porcentaje:.1f}%",

        )

    with col2:

        st.metric(

            "Contestadas",

            f"{resultado.respondidos}/{resultado.total}",

        )

    with col3:

        st.metric(

            "Estado",

            resultado.estado,

        )

    st.divider()


# ==========================================================
# DIMENSIÓN
# ==========================================================

def mostrar_dimension(
    expediente,
    dimension_id,
):

    dimension = DIMENSIONES[dimension_id]

    estado = estado_dimension(

        expediente,

        dimension_id,

    )

    with st.expander(

        f'{dimension["titulo"]}   {estado}',

        expanded=True,

    ):

        for subdimension_id, subdimension in dimension[
            "subdimensiones"
        ].items():

            mostrar_subdimension(

                expediente,

                dimension_id,

                subdimension_id,

                subdimension,

            )
# ==========================================================
# IMPORTACIONES PARA EL CONTROL DE LA APLICACIÓN
# ==========================================================

from modelo import Auditoria
from funciones import (
    inicializar_expedientes,
    promedio_auditoria,
)


# ==========================================================
# ESTADO DE LA SESIÓN
# ==========================================================

def inicializar_estado():

    if "pantalla" not in st.session_state:
        st.session_state.pantalla = "inicio"

    if "auditoria" not in st.session_state:
        st.session_state.auditoria = None


# ==========================================================
# PANTALLA DE INICIO
# ==========================================================

def pantalla_inicio():

    encabezado()

    st.header("Bienvenido")

    st.write(
        "Indique cuántos expedientes desea registrar."
    )

    numero_expedientes = st.number_input(
        "Número de expedientes",
        min_value=1,
        max_value=29,
        value=1,
        step=1,
    )

    st.divider()

    if st.button(
        "Comenzar auditoría",
        type="primary",
        use_container_width=True,
    ):

        auditoria = Auditoria(
            total_expedientes=int(numero_expedientes)
        )

        inicializar_expedientes(auditoria)

        st.session_state.auditoria = auditoria
        st.session_state.pantalla = "expediente"

        st.rerun()


# ==========================================================
# BARRA LATERAL
# ==========================================================

def mostrar_barra_lateral(auditoria):

    expediente = auditoria.expediente

    with st.sidebar:

        st.title("Auditoría")

        st.write(
            f"**Expediente "
            f"{auditoria.numero_expediente_actual} "
            f"de {auditoria.total_expedientes}**"
        )

        st.progress(
            expediente.porcentaje_completitud / 100
        )

        st.caption(
            "La barra indica únicamente el avance "
            "de captura, no el cumplimiento."
        )

        st.divider()

        st.metric(
            "Completitud",
            f"{expediente.porcentaje_completitud:.1f}%",
        )

        st.metric(
            "Cumplimiento global",
            f"{expediente.porcentaje_global:.1f}%",
        )

        st.divider()

        if st.button(
            "Nueva auditoría",
            use_container_width=True,
        ):
            st.session_state.clear()
            st.rerun()


# ==========================================================
# PANTALLA DEL EXPEDIENTE
# ==========================================================

def pantalla_expediente():

    auditoria = st.session_state.auditoria
    expediente = auditoria.expediente

    mostrar_barra_lateral(auditoria)

    st.title(
        f"Expediente "
        f"{auditoria.numero_expediente_actual} "
        f"de {auditoria.total_expedientes}"
    )

    mostrar_progreso(expediente)

    st.info(
        "La completitud únicamente representa el avance "
        "del cuestionario. Los semáforos corresponden al "
        "análisis de las respuestas."
    )

    st.divider()

    for dimension_id in DIMENSIONES:
        mostrar_dimension(
            expediente,
            dimension_id,
        )

    st.divider()

    columna_anterior, columna_siguiente = st.columns(2)

    with columna_anterior:

        if auditoria.expediente_actual > 0:

            if st.button(
                "← Expediente anterior",
                use_container_width=True,
            ):
                auditoria.anterior()
                st.rerun()

    with columna_siguiente:

        if auditoria.ultimo:

            texto_boton = "Finalizar auditoría"

        else:

            texto_boton = "Guardar y continuar →"

        if st.button(
            texto_boton,
            type="primary",
            use_container_width=True,
        ):

            if auditoria.ultimo:
                st.session_state.pantalla = "resultados"

            else:
                auditoria.siguiente()

            st.rerun()


# ==========================================================
# RESULTADO DE UN EXPEDIENTE
# ==========================================================

def mostrar_resultado_expediente(expediente):

    with st.expander(
        f"Expediente {expediente.numero} — "
        f"{expediente.porcentaje_global:.1f}%"
    ):

        st.metric(
            "Cumplimiento global",
            f"{expediente.porcentaje_global:.1f}%",
        )

        st.caption(
            f"Completitud de captura: "
            f"{expediente.porcentaje_completitud:.1f}%"
        )

        st.divider()

        for dimension_id, dimension in (
            expediente.dimensiones.items()
        ):

            st.subheader(
                f"{dimension.titulo} — {dimension.estado}"
            )

            st.write(
                f"Cumplimiento general: "
                f"**{dimension.porcentaje_cumplimiento:.1f}%**"
            )

            for subdimension in (
                dimension.subdimensiones.values()
            ):

                col1, col2, col3 = st.columns([3, 1, 2])

                col1.write(
                    f"**{subdimension.titulo}**"
                )

                col2.write(
                    f"{subdimension.porcentaje:.1f}%"
                )

                col3.write(
                    subdimension.estado
                )

                st.caption(
                    f"Meta: {subdimension.descripcion_meta}"
                )

            st.divider()


# ==========================================================
# PANTALLA DE RESULTADOS
# ==========================================================

def pantalla_resultados():

    auditoria = st.session_state.auditoria

    encabezado()

    st.header("Resultados finales")

    st.success(
        f"Se evaluaron "
        f"{auditoria.total_expedientes} expedientes."
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Cumplimiento general de la auditoría",
        f"{promedio_auditoria(auditoria):.1f}%",
    )

    expedientes_completos = sum(
        expediente.completo
        for expediente in auditoria.expedientes
    )

    col2.metric(
        "Expedientes completamente contestados",
        f"{expedientes_completos}/"
        f"{auditoria.total_expedientes}",
    )

    st.divider()

    for expediente in auditoria.expedientes:
        mostrar_resultado_expediente(expediente)

    st.divider()

    # ======================================================
    # INDICADORES ADICIONALES
    # ======================================================

    st.header("Indicadores adicionales")

    # ------------------------------------------------------
    # REINGRESOS HOSPITALARIOS
    # ------------------------------------------------------

    st.subheader("Reingresos hospitalarios")

    col1, col2 = st.columns(2)

    with col1:
        ingresos = st.number_input(
            "Número de ingresos",
            min_value=0,
            value=0,
            step=1,
            key="ingresos",
        )

    with col2:
        reingresos = st.number_input(
            "Número de reingresos",
            min_value=0,
            value=0,
            step=1,
            key="reingresos",
        )

    if reingresos > ingresos and ingresos > 0:
        st.warning(
            "El número de reingresos no puede ser mayor "
            "que el número de ingresos."
        )

    elif ingresos > 0:

        porcentaje_reingresos = (
            reingresos / ingresos * 100
        )

        st.metric(
            "Porcentaje de reingresos",
            f"{porcentaje_reingresos:.2f}%",
        )

        if porcentaje_reingresos <= 10:
            st.success("🟢 Cumple con la meta de ≤10%.")

        else:
            st.error("🔴 No cumple con la meta de ≤10%.")

    else:
        st.info(
            "Ingrese el número de ingresos para calcular "
            "el porcentaje de reingresos."
        )

    st.divider()

    # ------------------------------------------------------
    # SEGURIDAD DE LA DOSIFICACIÓN
    # ------------------------------------------------------

    st.subheader("Seguridad de la dosificación")

    col1, col2 = st.columns(2)

    with col1:
        dosis = st.number_input(
            "Número de administraciones",
            min_value=0,
            value=0,
            step=1,
            key="dosis",
        )

    with col2:
        errores = st.number_input(
            "Número de errores",
            min_value=0,
            value=0,
            step=1,
            key="errores",
        )

    if errores > dosis and dosis > 0:
        st.warning(
            "El número de errores no puede ser mayor "
            "que el número de administraciones."
        )

    elif dosis > 0:

        porcentaje_errores = errores / dosis * 100

        st.metric(
            "Porcentaje de errores de dosificación",
            f"{porcentaje_errores:.2f}%",
        )

        if porcentaje_errores == 0:
            st.success("🟢 Cumple con la meta de 0% de errores.")

        else:
            st.error("🔴 No cumple con la meta de 0% de errores.")

    else:
        st.info(
            "Ingrese el número de administraciones para "
            "calcular el porcentaje de errores."
        )

    st.divider()

    # ======================================================
    # NAVEGACIÓN
    # ======================================================

    col_anterior, col_nueva = st.columns(2)

    with col_anterior:

        if st.button(
            "← Volver al último expediente",
            use_container_width=True,
        ):
            st.session_state.pantalla = "expediente"
            st.rerun()

    with col_nueva:

        if st.button(
            "Iniciar nueva auditoría",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.clear()
            st.rerun()


# ==========================================================
# EJECUCIÓN PRINCIPAL
# ==========================================================

def ejecutar_app():

    inicializar_estado()

    if st.session_state.pantalla == "inicio":
        pantalla_inicio()

    elif st.session_state.pantalla == "expediente":
        pantalla_expediente()

    elif st.session_state.pantalla == "resultados":
        pantalla_resultados()

    else:
        st.session_state.pantalla = "inicio"
        st.rerun()