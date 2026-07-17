"""
iniciar.py

Lanzador del Sistema de Auditoría.
"""

import os
import socket
import sys
import threading
import time
import traceback
import webbrowser
from pathlib import Path

from streamlit.web import cli as stcli


PUERTO = 8501
DIRECCION = "127.0.0.1"


def obtener_ruta_app() -> Path:
    """Localiza app.py dentro o fuera del ejecutable."""

    if getattr(sys, "frozen", False):
        carpeta_base = Path(sys._MEIPASS)
    else:
        carpeta_base = Path(__file__).resolve().parent

    return carpeta_base / "app.py"


def puerto_disponible() -> bool:
    """Comprueba si el servidor ya responde en el puerto."""

    try:
        with socket.create_connection(
            (DIRECCION, PUERTO),
            timeout=1,
        ):
            return True
    except OSError:
        return False


def abrir_navegador() -> None:
    """Espera a que Streamlit arranque y abre el navegador."""

    url = f"http://{DIRECCION}:{PUERTO}"

    for _ in range(60):
        if puerto_disponible():
            print(f"Servidor disponible en: {url}", flush=True)
            webbrowser.open(url)
            return

        time.sleep(0.5)

    print(
        "No fue posible detectar el servidor de Streamlit.",
        flush=True,
    )
    print(
        f"Intenta abrir manualmente: {url}",
        flush=True,
    )


def main() -> None:
    try:
        app_path = obtener_ruta_app()

        print("Iniciando Sistema de Auditoría...", flush=True)
        print(f"Ejecutable: {sys.executable}", flush=True)
        print(f"Carpeta empaquetada: {getattr(sys, '_MEIPASS', 'No')}", flush=True)
        print(f"Archivo de la aplicación: {app_path}", flush=True)
        print(f"¿Existe app.py?: {app_path.exists()}", flush=True)

        if not app_path.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo: {app_path}"
            )

        hilo_navegador = threading.Thread(
            target=abrir_navegador,
            daemon=True,
        )
        hilo_navegador.start()

        os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

        os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
        os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"

        sys.argv = [
            "streamlit",
            "run",
            str(app_path),
            "--global.developmentMode=false",
            f"--server.address={DIRECCION}",
            f"--server.port={PUERTO}",
            "--server.headless=true",
            "--browser.gatherUsageStats=false",
        ]

        print("Arrancando el servidor de Streamlit...", flush=True)

        stcli.main()

    except Exception:
        print("\nOCURRIÓ UN ERROR:\n", flush=True)
        traceback.print_exc()

        input(
            "\nPresiona Enter para cerrar esta ventana..."
        )


if __name__ == "__main__":
    main()