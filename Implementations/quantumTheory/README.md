.
## quantumTheory

El sistema que se modela consiste en una partícula confinada a un conjunto discreto de posiciones en una línea, el cual se puede realizar las siguientes operaciones:

- Calcular la probabilidad de encontrarlo en una posición en particular.
- El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
- Operacion Bra
- Normalizacion  de vectores cuanticos 


## Empezando



### Pre-requisitos

-Tener instalado una version mayor o igual a python 3
-Es opcional tener instalado git 


### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link 
https://www.python.org/downloads/ .

En caso de no tener instalado git, este  se podra descargar del siguiente link 
https://git-scm.com/downloads.





## Ejecutando Programa 

Para ejecutar el programa se deben seguir los siquientes pasos:

1) Descargar el repositorio en git usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/quantumTheory

```
3) ejecutar el archivo con el siguiente comando 

```
python quantumTheory.py
```

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.

Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en testMatrixandVector.py .

En este .py se encontraran 2 pruebas por cada una de las funciones implementadas de operaciones para vectores y matrices complejas.

A continuacion se mostrara un ejemplo de una prueba de la funcion quantumTheory la cual permite calcular la  probabilidad de econtrar al sistema en una posicion especifica , de forma analoga sera para las demas funciones:

# Funcion en la libreria 
```
def testProbability( self ):
        prob = [ [-3,-1],[0,-2],[0,1],[2,0]];
        self.assertEqual( probability(prob, 2 ),0.0526);
```




## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/quantumTheoryTest

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python quantumTheoryTest.py
```
# Salida en IDLE
![image](https://user-images.githubusercontent.com/53798019/76693852-c1464b80-6639-11ea-9baa-a8ad0320e62b.png)


## Autor

**Iván Camilo Rincón Saavedra** -[Rincon10](https://github.com/Rincon10)


## Referencias
El modelo que se siguio para diseñar el readme fue tomado del usuario:

[PurpleBooth](https://github.com/PurpleBooth)


