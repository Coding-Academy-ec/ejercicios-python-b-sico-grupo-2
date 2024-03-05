from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Brayan Ruano"
    edad = 30
    estatura = 1.75
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Brayan Ruano\nEdad: 30\nEstatura: 1.75\n"
