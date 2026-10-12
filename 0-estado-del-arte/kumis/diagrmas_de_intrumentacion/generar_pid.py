"""Genera los planos P&ID-L3-001 y P&ID-L3-002 de la línea de kumis.
Uso: python3 generar_pid.py   (requiere matplotlib)
Salida: PID_Kumis_Hoja1.png/.svg, PID_Kumis_Hoja2.png/.svg y PID_Kumis.pdf"""
from pid_hoja1 import hoja1
from pid_hoja2 import hoja2
from PIL import Image
hoja1("PID_Kumis_Hoja1.png","PID_Kumis_Hoja1.svg")
hoja2("PID_Kumis_Hoja2.png","PID_Kumis_Hoja2.svg")
a=Image.open("PID_Kumis_Hoja1.png").convert("RGB"); b=Image.open("PID_Kumis_Hoja2.png").convert("RGB")
a.save("PID_Kumis.pdf",save_all=True,append_images=[b],resolution=200)
print("ok")
