#login#
Username= 'lalo20'
password= '10lalo20'

intentos=0 #Declaracion de contador

usuarioAccedio=False
intentos=0 #contador 
#Bienvenida
msg_bienvenida='Bienvenido al sistema\n Accede con tus credenciales\n'
print(msg_bienvenida)
#Recibe n numero de intentos
while not usuarioAccedio:
    intentos += 1#incremento 
    if intentos ==4:
        exit();#salimos del programa
    #Autenticidad de credenciales
    if input('Usuario:\t')==Username and input('Contrasena:\t')== password :
        print('Hola, has accedido correctamente\n')
        usuarioAccedio=True
    else:
        print('Has agotado el primer intento, Quedan 3', 3-intentos)
#fin del login#

"""
Generacion de un listado de los 5 productos con mayores ventas
"""
from lifestore_file import lifestore_sales,lifestore_products,lifestore_searches

soldproduct=[]
timesold=[]
#Creacion de listas anidadas
soldproduct=[sale[1] for sale in lifestore_sales]

for sale in lifestore_products:
    anidada=[]
    timesold.append(anidada)

    for k in range(1):
        anidada.append(sale[0]) #Obtenemos ID
        anidada.append(sale[1]) #Obtenemos Nombre
        anidada.append(soldproduct.count(sale[0])) #Contamos numero de ventas
        anidada.append(sale[-2]) # Obtenemos Categoria
#Ordemos la lista
#Especificamente la tercera columna que contiene el numero de ventas
def Sort(timesold):
    timesold.sort(key= lambda x:x[2])# Utilizamos la funcion Lambda
    return timesold 

timesold =Sort(timesold)

print( "Productos con mayores ventas")
#Se imprime la lista ordenada.
for i in (-1,-2,-3,-4,-5):
    print(F'ID:{timesold[i][0]}\t NAME:{timesold[i][1]}\t SALES:{timesold[i][2]}\t')


#10 productos con mayores busquedas
searchedproduct =[];
timesearched=[]

searchedproduct=[busqueda[1] for busqueda in lifestore_searches]

for busqueda in lifestore_products:
    anidada=[]
    timesearched.append(anidada)

    for k in range(1):
        anidada.append(busqueda[0]) #Obtenemos ID
        anidada.append(busqueda[1]) #Obtenemos Nombre
        anidada.append(searchedproduct.count(busqueda[0])) #Contamos el numero de busquedas
        anidada.append(busqueda[-2]) #Obtenemos la categoria 
#Se ordenda la lista
#Ordenamos la tercera columna que corresponde a busquedas
def Sort(timesearched):
    timesearched.sort(key=lambda x:x[2])
    return timesearched
timesearched=Sort(timesearched)

#Se imprime la lista ordenada.
print('Productos mas buscados')
for i in (-1,-2,-3,-4,-5,-6,-7,-8,-9,-10):
    print(F'ID:{timesearched[i][0]}\t Nombre:{timesearched[i][1]}\t Busquedas:{timesearched[i][2]}\t')

#Ventas por categoria y busquedas por categoria
#Creacion de la categoria de los prodructos
categorias=[];
procesadores=[]; gpus=[]; motherboards=[]; hdd=[]; usb=[]; screen=[]; speaker=[]; headphones=[]
categorias=[item[-2] for item in lifestore_products]
categorias=list(dict.fromkeys(categorias))
#Agrupacion y extraccion de los productos rezagados por categoria
#Se repite para cada categoria
for item in timesold:
    if categorias[0]  in item:
        procesadores.append(item[:4])

    elif categorias[1] in item:
        gpus.append(item[:4])

    elif categorias[2] in item:
        motherboards.append(item[:4])

    elif categorias[3] in item:
        hdd.append(item[:4])

    elif categorias[4] in item:
        usb.append(item[:4])

    elif categorias[5] in item:
        screen.append(item[:4])

    elif categorias[6] in item:
        speaker.append(item[:4])

    elif categorias[7] in item:
        headphones.append(item[:4])
#Impresion de cada producto rezagado por categoria
print('\n\tProcesadores menos vendidos ')
for i in range(5):
    print(F'ID: {procesadores[i][0]}\t Nombre:{procesadores[i][1]}\t Ventas: {procesadores[i][2]}\t ')

print('\n\tGPUS con menos ventas')
for i in range(5):
    print(F'ID: {gpus[i][0]}\t Nombre:{gpus[i][1]}\t Ventas: {gpus[i][2]}\t ')

print('\n\tTarjetas Madre menos vendidas')

for i in range(5):
    print(F'ID: {motherboards[i][0]}\t Nombre:{motherboards[i][1]}\t Ventas: {motherboards[i][2]}\t ')

print('\n\t Discos duros menos vendidos')
for i in range(5):
    print(F'ID: {hdd[i][0]}\t Nombre:{hdd[i][1]}\t Ventas: {hdd[i][2]}\t ')


print('\n\tUSBs menos vendidas')
for i in range(2):
    print(F'ID: {usb[i][0]}\t Nombre:{usb[i][1]}\t Ventas: {usb[i][2]}\t ')

print('\n\t Monitores menos vendidos')
for i in range(5):
    print(F'ID: {screen[i][0]}\t Nombre:{screen[i][1]}\t Ventas: {screen[i][2]}\t ')

print('\n\t Bocinas menos vendidas')
for i in range(5):
    print(F'ID: {speaker[i][0]}\t Nombre:{speaker[i][1]}\t Ventas: {speaker[i][2]}\t ')

print('\n\t Audifonos menos vendidas')
for i in range(5):
    print(F'ID: {headphones[i][0]}\t Nombre:{headphones[i][1]}\t Venta: {headphones[i][2]}\t ')


#Busquedas por categoria 
#Declaramos nuevamente las categorias
procesador=[]; gpu=[]; motherboard=[]; HDDs=[]; usbs=[]; monitor=[]; speakr=[]; headphone=[];

for stock in timesearched:
    if categorias[1] in stock:
        gpu.append(stock[:4])
    elif categorias[2] in stock:
        motherboard.append(stock[:4])
    elif categorias[3] in stock:
        HDDs.append(stock[:4])
    elif categorias[4] in stock:
        usbs.append(stock[:4])
    elif categorias[5] in stock:
        monitor.append(stock[:4])
    elif categorias[6] in stock:
        speakr.append(stock[:4])
    elif categorias[7] in stock:
        headphone.append(stock[:4])

    

print('\n\t Tarjetas de video con menos busquedas')
for i in range(10):
    print(F'ID: {gpu[i][0]}\t Nombre:{gpu[i][1]}\t Busquedas: {gpu[i][2]}\t ')

print('\n\t Tarjetas Madre con menos busquedas')
for i in range(10):
    print(F'ID: {motherboard[i][0]}\t Nombre:{motherboard[i][1]}\t Busquedas: {motherboard[i][2]}\t ')

print('\n\t Discos duros  con menos busquedas')
for i in range(10):
    print(F'ID: {HDDs[i][0]}\t Nombre:{HDDs[i][1]}\t Busquedas: {HDDs[i][2]}\t ')

print('\n\t USBs con menos busquedas')
for i in range(2):
    print(F'ID: {usbs[i][0]}\t Nombre:{usbs[i][1]}\t Busquedas: {usbs[i][2]}\t ')

print('\n\t Pantallas con menos busquedas')
for i in range(10):
    print(F'ID: {monitor[i][0]}\t Nombre:{monitor[i][1]}\t Busquedas: {monitor[i][2]}\t ')

print('\n\t Bocinas con menos busquedas')
for i in range(10):
    print(F'ID: {speakr[i][0]}\t Nombre:{speakr[i][1]}\t Busquedas: {speakr[i][2]}\t ')

print('\n\t Audifonos con menos buquedas')
for i in range(10):
    print(F'ID: {headphone[i][0]}\t Nombre:{headphone[i][1]}\t Busquedas: {headphone[i][2]}\t ')

#Reseña por producto
promedio=0;
puntajetotal=[]
acomulado=[]
for resena_producto in lifestore_products:
    for resena in lifestore_sales:
        if resena_producto[0]==resena[1]:
            promedio +=resena[2]
    puntajetotal.append(promedio)
    promedio=0;

for resena in timesold:
    anidada=[]
if resena[2]>0:
    acomulado.append(anidada)
    for k in range(1):
                  anidada.append(resena[0])
                  anidada.append(resena[1])
                  anidada.append(resena[2])
                  anidada.append(puntajetotal[resena[0]-1]/resena[2])

def Sort (acomulado):
    acomulado.sort(key=lambda x:x[-1])
    return acomulado

acomulado=Sort(acomulado)
print('Productos con mejor resena')
for i in range(0,10):
    print(F'ID: {acomulado[i][0]}\t Nombre:{acomulado[i][1]}\t Puntaje: {acomulado[i][2]}\t ')