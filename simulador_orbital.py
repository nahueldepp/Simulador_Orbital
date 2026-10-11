#datos
G = 6.67430e-11 
M_SOL = 1.989e30 #masa sol
R_SOL = 6.9634e8 #radio sol
M_TIERRA = 5.972e24 #masa tierra

x_0 = 1.496e11 #posición inicial en x (1 unidad astronomica en metros, o sea, esta a esa cantidad de metros del sol)
y_0 = 0.0 #posicion inicial en y
vx_0 = 0.0 #velocidad inicial en x
vy_0 = 29780.0 #velocidad inicial en y (velocidad orbital de la tierra, o sea, )

dt = 3600.0 #paso del tiempo
t_final = 3.154e7 #tiempo total de simulacion

#listas para tabla
tiempos = []
lista_x = []
lista_y = []
lista_vx = []
lista_vy = []

#bucle
t = 0.0

#valores iniciales, despues los vamos cambiando
x = x_0
y = y_0
vx = vx_0
vy = vy_0

while t <= t_final:
    #guarda los datos actuales en las listas
    tiempos.append(t)
    lista_x.append(x)
    lista_y.append(y)
    lista_vx.append(vx)
    lista_vy.append(vy)
    
    #distancia al sol, que es el origen
    r = (x**2 + y**2)**0.5
    
    #formula acción de la ley de gravitación universal
    factor_grav = (G * M_SOL) / (r**3)
    ax = -factor_grav * x
    ay = -factor_grav * y
    
    #metodo de euler para actualizar valores en el siguiente instante
    x = x + vx * dt
    y = y + vy * dt
    vx = vx + ax * dt
    vy = vy + ay * dt
    
    #avanza el tiempo
    t = t + dt