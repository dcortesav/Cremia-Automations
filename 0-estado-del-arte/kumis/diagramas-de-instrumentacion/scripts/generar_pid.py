"""Genera los planos P&ID-L3-001 y P&ID-L3-002 de la línea de kumis.
Uso: python generar_pid.py   (requiere matplotlib)
Salida: ../imagenes/PID_Kumis_Hoja1.svg y ../imagenes/PID_Kumis_Hoja2.svg"""
import os
from pid_hoja1 import hoja1
from pid_hoja2 import hoja2

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "imagenes"))
os.makedirs(BASE, exist_ok=True)

hoja1(os.path.join(BASE, "PID_Kumis_Hoja1.svg"))
hoja2(os.path.join(BASE, "PID_Kumis_Hoja2.svg"))
print("ok")
