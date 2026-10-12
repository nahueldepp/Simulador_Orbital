#datos
import csv
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

G = 6.67430e-11 
M_SOL = 1.989e30 #masa sol
R_SOL = 6.9634e8 #radio sol
M_TIERRA = 5.972e24 #masa tierra
R_SOL = 6.925e8 #radio del sol

X0 = 1.496e11 #posición inicial en x (1 unidad astronomica en metros, o sea, esta a esa cantidad de metros del sol)
Y0 = 0.0 #posicion inicial en y
VX0 = 0.0 #velocidad inicial en x
VY0 = 29780.0 #velocidad inicial en y (velocidad orbital de la tierra, m/s)

DT = 3600 #paso del tiempo (un minuto)
DIAS_SIMULACION = 365
TIEMPO_SIMULACION = (DIAS_SIMULACION*24*DT) #tiempo total de simulacion (en segundos)
PASOS = int((TIEMPO_SIMULACION)/DT)

# ==============================================================================
# seleccion 
# ==============================================================================
def seleccionar_opcion():
    print("=" * 60)
    print(" SIMULADOR ORBITAL ")
    print("=" * 60)
    print("Selecciona un escenario:")
    print(" 1) Órbita circular")
    print(" 2) Caída libre hacia el Sol (v0 = 0 -> ¡Colisión directa!)")
    print(" 3) Personalizado (ingresar parámetros a mano)")
    opcion = input("Opción [1-3] (Enter para 1): ").strip()
    return opcion

#========================================
#simulacion de orbita
#========================================
def simular(x0 = X0, y0 = Y0, vx0= VX0, vy0=VY0):
    #listas para tabla
    tiempos = [0]
    lista_x = [x0]
    lista_y = [y0]
    lista_vx = [vx0]
    lista_vy = [vy0]
    colision = False
    #valores iniciales, despues los vamos cambiando

    for t in range(PASOS):
        
        #agarramos los ultimos valores que aparecen en las listas

        x = lista_x[-1]
        y = lista_y[-1]
        vx = lista_vx[-1]
        vy = lista_vy[-1]
        
        #distancia al sol, que es el origen
        r = (x**2 + y**2)**0.5

        #formula acción de la ley de gravitación universal
        factor_grav = (G * M_SOL) / (r**3)
        Fgx = -factor_grav * x
        Fgy = -factor_grav * y
        
        #metodo de euler para actualizar valores en el siguiente instante
        vx_sig = vx + Fgx * DT
        vy_sig = vy + Fgy * DT
        x_sig = x + vx_sig * DT
        y_sig = y + vy_sig * DT
        r_sig = (x_sig**2 + y_sig**2)**0.5 

        if (r_sig <= R_SOL):
            colision = True
            lista_x.append(x_sig)
            lista_y.append(y_sig)
            lista_vx.append(0)
            lista_vy.append(0)
            break
        
        
        #agregamos los nuevos valores a las tablas
        tiempos.append(t*PASOS)
        lista_x.append(x_sig)
        lista_y.append(y_sig)
        lista_vx.append(vx_sig)
        lista_vy.append(vy_sig)

    return (tiempos, lista_x, lista_y, lista_vx, lista_vy, colision)

def crear_tabla(tiempos, x, y):
    with open("datos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)

        # Escribir encabezados
        escritor.writerow(["tiempo", "x", "y"])

        # Escribir los datos
        for fila in range(len(tiempos)):
            escritor.writerow([fila, f"{tiempos[fila]/86400:.3f}", f"{x[fila]:.4e}", f"{y[fila]:.4e}"])

def main():
    opcion= seleccionar_opcion()
    x = X0
    y = Y0
    vx = VX0
    vy = VY0
    if opcion == "2":
       vy = 0
       vx = 0
    elif opcion == "3" :
        x = float(input("x0 (m): "))
        y = float(input("y0 (m): "))
        vx = float(input("vx0 (m/s): "))
        vy = float(input("vy0 (m/s): "))

    tiempos,x_vals,y_vals,vx_vals,vy_vals,colision= simular(x,y,vx,vy)
    crear_tabla(tiempos,x_vals,y_vals)
    if colision: 
        print("💥 ¡COLISIÓN CON EL SOL! 💥\n(r < R_sol)")


if __name__ == "__main__":
    main()