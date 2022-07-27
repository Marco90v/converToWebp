# App para convertir imágenes de formato PNG, JPG y JPEG en formato WEBP
# Debe colocar las imágenes a convertir en la carpeta imanes junto al archivo .py
# La aplicación creara la carpeta WEBP con las imágenes convertidas, tendrán el mismo nombre

from pathlib import Path
from PIL import Image
import os
import ntpath

def convert_to_webp(source):
    destination = "webp\\" + ntpath.basename(source).split(".")[0] + ".webp"
    image = Image.open(source)
    image.save(destination, format="webp")
    return destination

def runList(paths):
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)

def main():
    formats = ["png", "jpg", "jpeg"]
    if not os.path.exists('webp'):
        os.mkdir("webp/")
    for format in formats:
        paths = Path("images").glob("**/*."+format)
        runList(paths)

main()