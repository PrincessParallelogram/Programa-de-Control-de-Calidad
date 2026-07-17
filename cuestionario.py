"""
cuestionario.py

Configuración completa del instrumento de auditoría.

Este archivo contiene:
- Dimensiones.
- Subdimensiones.
- Criterios.
- Metas de evaluación.

Tipos de meta:
- "igual": el porcentaje debe ser exactamente igual a la meta.
- "minimo": el porcentaje debe ser mayor o igual a la meta.
- "maximo": el porcentaje de incumplimientos debe ser menor
  o igual a la meta.
"""

DIMENSIONES = {

    # ======================================================
    # DIMENSIÓN 1
    # ======================================================

    "D1": {
        "id": "D1",
        "titulo": "VALORACIÓN INTEGRAL E INTEGRADA",

        "subdimensiones": {

            # --------------------------------------------------
            # D1 - SUBDIMENSIÓN 1
            # --------------------------------------------------

            "D1_S1": {
                "id": "D1_S1",
                "titulo": "Documentación básica del expediente",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D1_S1_C1",
                        "texto": (
                            "Ficha de identidad completa con coordenadas "
                            "GPS o referencias precisas del domicilio."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S1_C2",
                        "texto": (
                            "Formato de Consentimiento Informado "
                            "debidamente firmado y fechado por el "
                            "paciente o tutor."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S1_C3",
                        "texto": (
                            "Documento de Voluntades Anticipadas o "
                            "Plan de Preferencias de Final de la Vida "
                            "firmado."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D1 - SUBDIMENSIÓN 2
            # --------------------------------------------------

            "D1_S2": {
                "id": "D1_S2",
                "titulo": "Valoración inicial mediante escalas",
                "porcentaje_ideal": 95,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D1_S2_C1",
                        "texto": (
                            "Registro de la escala ESAS para la "
                            "valoración de síntomas, aplicada dentro "
                            "de las primeras 48 horas del ingreso."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S2_C2",
                        "texto": (
                            "Registro de la escala PPS para la "
                            "valoración de funcionalidad, aplicada "
                            "dentro de las primeras 48 horas del ingreso."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S2_C3",
                        "texto": (
                            "Registro de la escala Zarit para la "
                            "valoración de sobrecarga del cuidador, "
                            "aplicada dentro de las primeras 48 horas."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D1 - SUBDIMENSIÓN 3
            # --------------------------------------------------

            "D1_S3": {
                "id": "D1_S3",
                "titulo": "Plan farmacológico y manejo de crisis",
                "porcentaje_ideal": 90,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D1_S3_C1",
                        "texto": ("Esquema Basal Fijo."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S3_C2",
                        "texto": ("Pauta de Rescate Explícita."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S3_C3",
                        "texto": (
                            "Acuse de Recibo de la Guía de Manejo "
                            "de Crisis."
                        ),
                        "descripcion": 
                            "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D1 - SUBDIMENSIÓN 4
            # --------------------------------------------------

            "D1_S4": {
                "id": "D1_S4",
                "titulo": "Verificación clínica y ajuste terapéutico",
                "porcentaje_ideal": 90,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D1_S4_C1",
                        "texto": "Inspección Física Obligatoria.",
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S4_C2",
                        "texto": "Confrontación de Datos Clave.",
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S4_C3",
                        "texto": "Asentamiento en Nota de Evolución.",
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D1_S4_C4",
                        "texto": (
                            "Justificación de Ajuste Terapéutico."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

        },
    },

    # ======================================================
    # DIMENSIÓN 2
    # ======================================================

    "D2": {
        "id": "D2",
        "titulo": "APOYO AL CUIDADOR Y A LA FAMILIA",

        "subdimensiones": {

            # --------------------------------------------------
            # D2 - SUBDIMENSIÓN 1
            # --------------------------------------------------

            "D2_S1": {
                "id": "D2_S1",
                "titulo": "Capacitación al cuidador",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D2_S1_C1",
                        "texto": ("Evaluación de Competencia Práctica."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S1_C2",
                        "texto": (
                            "Bitácora de Retorno de Demostración."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S1_C3",
                        "texto": ("Identificación Autónoma de Crisis."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S1_C4",
                        "texto": (
                            "Manejo Seguro de Material Punzocortante."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D2 - SUBDIMENSIÓN 2
            # --------------------------------------------------

            "D2_S2": {
                "id": "D2_S2",
                "titulo": "Soporte de guardia 24/7",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D2_S2_C1",
                        "texto": ("Cero Desvíos Automatizados."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S2_C2",
                        "texto": ("Acceso Inmediato al Expediente."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S2_C3",
                        "texto": ("Tiempo de Respuesta Telefónica."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S2_C4",
                        "texto": ("Registro Obligatorio."),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D2 - SUBDIMENSIÓN 3
            # --------------------------------------------------

            "D2_S3": {
                "id": "D2_S3",
                "titulo": "Monitoreo de sobrecarga",
                "porcentaje_ideal": 90,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D2_S3_C1",
                        "texto": (
                            "Periodicidad Calendarizada Obligatoria."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S3_C2",
                        "texto": ("Ambiente de Aplicación Privado."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S3_C3",
                        "texto": (
                            "Umbrales de Alerta Automatizados."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S3_C4",
                        "texto": ("Ruta de Intervención por Puntaje."),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D2 - SUBDIMENSIÓN 4
            # --------------------------------------------------

            "D2_S4": {
                "id": "D2_S4",
                "titulo": "Voluntad del lugar de muerte",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D2_S4_C1",
                        "texto": (
                            "Concertación y Registro Explícito."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S4_C2",
                        "texto": (
                            "Plan de Contingencia de Deceso en Casa."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S4_C3",
                        "texto": ("Identificación de No Reanimación."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S4_C4",
                        "texto": (
                            "Coordinación Funeraria Anticipada."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D2 - SUBDIMENSIÓN 5
            # --------------------------------------------------

            "D2_S5": {
                "id": "D2_S5",
                "titulo": "Satisfacción del paciente y la familia",
                "porcentaje_ideal": 95,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D2_S5_C1",
                        "texto": ("Instrumento Estandarizado."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S5_C2",
                        "texto": (
                            "Temporalidad y Canales de Aplicación."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S5_C3",
                        "texto": ("Anonimato y Sesgo de Respuesta."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D2_S5_C4",
                        "texto": ("Mecanismo de Quejas Activo."),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

        },
    },

    # ======================================================
    # DIMENSIÓN 3
    # ======================================================

    "D3": {
        "id": "D3",
        "titulo": "ADMINISTRACIÓN Y GESTIÓN",

        "subdimensiones": {

            # --------------------------------------------------
            # D3 - SUBDIMENSIÓN 1
            # --------------------------------------------------

            "D3_S1": {
                "id": "D3_S1",
                "titulo": "Suministro de opioides",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D3_S1_C1",
                        "texto": (
                            "Cálculo de Stock Crítico Domiciliario."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S1_C2",
                        "texto": (
                            "Bloqueo Preventivo Pre-Festivo."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S1_C3",
                        "texto": (
                            "Logística de Emisión de Recetarios "
                            "de Controlados."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S1_C4",
                        "texto": (
                            "Monitoreo de Surtimiento Efectivo."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D3 - SUBDIMENSIÓN 2
            # --------------------------------------------------

            "D3_S2": {
                "id": "D3_S2",
                "titulo": "Tiempo de respuesta",
                "porcentaje_ideal": 95,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D3_S2_C1",
                        "texto": (
                            "Triaje Telefónico de Clasificación."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S2_C2",
                        "texto": (
                            "Despacho Prioritario del Equipo "
                            "Domiciliario."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S2_C3",
                        "texto": (
                            "Cronometraje Digital del Traslado, "
                            "con límite menor a cuatro horas."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S2_C4",
                        "texto": (
                            "Acceso Inmediato a Insumos de "
                            "Alivio Rápido."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D3 - SUBDIMENSIÓN 3
            # --------------------------------------------------

            "D3_S3": {
                "id": "D3_S3",
                "titulo": "Control de reingresos hospitalarios",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D3_S3_C1",
                        "texto": (
                            "Notificación Inmediata de Hospitalización."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S3_C2",
                        "texto": (
                            "Sesión Obligatoria de Análisis "
                            "de Causa Raíz."
                       ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S3_C3",
                        "texto": (
                            "Clasificación del Origen de la Falla."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S3_C4",
                        "texto": (
                            "Diseño del Plan Remedial Inmediato."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D3 - SUBDIMENSIÓN 4
            # --------------------------------------------------

            "D3_S4": {
                "id": "D3_S4",
                "titulo": (
                    "Logística de rutas de consultas domiciliarias"
                ),
                "porcentaje_ideal": 85,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D3_S4_C1",
                        "texto": ("Zonificación Territorial."),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S4_C2",
                        "texto": (
                            "Programación Centralizada Automatizada."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S4_C3",
                        "texto": (
                            "Asignación de Equipos de Soporte "
                            "Domiciliario por Zona Geográfica."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D3_S4_C4",
                        "texto": (
                            "Métrica de Rendimiento del Tiempo "
                            "de Traslado."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

        },
    },

    # ======================================================
    # DIMENSIÓN 4
    # ======================================================

    "D4": {
        "id": "D4",
        "titulo": "INVESTIGACIÓN Y EDUCACIÓN",

        "subdimensiones": {

            # --------------------------------------------------
            # D4 - SUBDIMENSIÓN 1
            # --------------------------------------------------

            "D4_S1": {
                "id": "D4_S1",
                "titulo": "Certificación del personal",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D4_S1_C1",
                        "texto": (
                            "Verificación de Credenciales Académicas."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S1_C2",
                        "texto": (
                            "Competencia Específica en Entorno "
                            "Domiciliario."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S1_C3",
                        "texto": (
                            "Expediente de Personal Actualizado."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S1_C4",
                        "texto": (
                            "Evaluación Anual de Competencias Clínicas."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D4 - SUBDIMENSIÓN 2
            # --------------------------------------------------

            "D4_S2": {
                "id": "D4_S2",
                "titulo": "Materiales educativos",
                "porcentaje_ideal": 100,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D4_S2_C1",
                        "texto": (
                            "Filtro de Lenguaje Sencillo y No Técnico."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S2_C2",
                        "texto": ("Actualización Anual Obligatoria.",
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S2_C3",
                        "texto": (
                            "Proceso de Validación Institucional."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S2_C4",
                        "texto": (
                            "Diversificación de Formatos Adaptativos."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D4 - SUBDIMENSIÓN 3
            # --------------------------------------------------

            "D4_S3": {
                "id": "D4_S3",
                "titulo": "Seguridad de la dosificación",
                "porcentaje_ideal": 0,
                "tipo_meta": "igual",

                "criterios": [

                    {
                        "id": "D4_S3_C1",
                        "texto": (
                            "Auditoría Física y Conteo de Fármacos."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S3_C2",
                        "texto": (
                            "Evaluación Dinámica de Comprensión."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S3_C3",
                        "texto": (
                            "Documentación en Nota de Enfermería."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S3_C4",
                        "texto": (
                            "Activación de Alerta por Desviación."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

            # --------------------------------------------------
            # D4 - SUBDIMENSIÓN 4
            # --------------------------------------------------

            "D4_S4": {
                "id": "D4_S4",
                "titulo": "Sesiones clínicas de casos",
                "porcentaje_ideal": 95,
                "tipo_meta": "minimo",

                "criterios": [

                    {
                        "id": "D4_S4_C1",
                        "texto": (
                            "Frecuencia y Quórum Obligatorio."
                       ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S4_C2",
                        "texto": (
                            "Criterio de Inclusión de Casos Complejos."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S4_C3",
                        "texto": ("Minuta de Acuerdos Clínicos.",
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                    {
                        "id": "D4_S4_C4",
                        "texto": (
                            "Traslado de Decisiones al Expediente."
                        ),
                        "descripcion": "",
                        "observacion": "",
                    },

                ],
            },

        },
    },

}