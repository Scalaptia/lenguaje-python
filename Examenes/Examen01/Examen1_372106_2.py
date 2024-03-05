"""
Normalmente caben 6 huevos en una cartera. Escribe un script para calcular la cantidad de cajas que necesita un granjero para
almacenar 28 huevos. El script también determinará cuántos huevos se colocan en la última cartera sin completar y cuántos
huevos adicionales se necesitan para llenar esta última cartera.

Se le solicita al usuario ingresar un valor(números enteros) y desplegar como resultado lo siguiente:
    1. Los datos de salida deben ser idénticos a los mencionados en las imágenes de abajo de este examen.
    2. Solo podrá utilizar los operadores, sentencia if(estructura de selección if sencilla), símbolos y funciones integradas
    vistas en clase.
    3. Podrá anidar la sentencia de selección if sencillas en este ejercicio.
"""

huevos_obtenidos = int(input("Ingresar la cantidad de huevos obtenidos: "))
huevos_por_cartera = 6

if huevos_obtenidos <= 0:
    print(f"La cantidad de huevos que se necesitan para llenar la cartera es de: {huevos_por_cartera}")

if huevos_obtenidos > 0:
    if huevos_obtenidos < 6:
        huevos_para_llenar = int(input("La cantidad de huevos que se necesitan para llenar una cartera es de: "))

carteras_llenas = huevos_obtenidos // huevos_por_cartera
huevos_restantes = huevos_obtenidos % huevos_por_cartera

huevos_adicionales = 0
if huevos_restantes > 0:
    huevos_adicionales = huevos_por_cartera - huevos_restantes

if carteras_llenas == 1:
    print(f"Se lleno 1 cartera de {huevos_por_cartera} huevos.")

if carteras_llenas > 1:
    print(f"Se llenaron {carteras_llenas} carteras de {huevos_por_cartera} huevos.")

if huevos_restantes == 1:
    print(f"En la ultima cartera se coloco {huevos_restantes} huevo.")
if huevos_restantes > 1:
    print(f"En la ultima cartera se colocaron {huevos_restantes} huevos.")

if huevos_adicionales >= 1:
    print(f"La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de: {huevos_adicionales}.")
