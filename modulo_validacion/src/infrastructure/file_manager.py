from pathlib import Path
from django.core.files.uploadedfile import UploadedFile
import shutil

def crear_carpeta(ruta: str) -> Path:
    carpeta = Path(ruta)
    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta

def guardar_imagen(
    archivo: UploadedFile,
    carpeta_destino: Path,
    nombre_archivo: str | None = None
) -> Path:
    carpeta_destino.mkdir(parents=True, exist_ok=True)

    extension = Path(archivo.name).suffix
    nombre_final = nombre_archivo or archivo.name

    ruta_final = carpeta_destino / f"{nombre_final}{extension}"

    with ruta_final.open("wb+") as destino:
        for chunk in archivo.chunks():
            destino.write(chunk)

    return ruta_final


def eliminar_carpeta(ruta: Path | str) -> None:
    carpeta = Path(ruta)

    if carpeta.exists() and carpeta.is_dir():
        shutil.rmtree(carpeta)
