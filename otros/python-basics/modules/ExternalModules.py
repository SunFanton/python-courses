"""
Los modulos externos son aquellos desarrollados por terceros
que no forman parte de la biblioteca standar de Pyhton.

Para instalacion global:

- En MacOS desde la terminal:
pip3 install nombre_modulo -> para intalar un modulo
pip3 uninstall nombre_modulo -> para desintalar un modulo
pip3 list -> para ver lista de modulos instalados

- En Windows desde Powershell:
pip install nombre_modulo -> para intalar un modulo
pip uninstall nombre_modulo -> para desintalar un modulo
pip list -> para ver lista de modulos instalados
"""

# import pyautogui
# from time import sleep
from matplotlib import pyplot as plt

# sleep(1)
# pyautogui.write("This is written by a computer", interval = 0.25)

plt.plot([1,2,3,4])
plt.ylabel("Some numbers for the Y axis")
plt.show()
