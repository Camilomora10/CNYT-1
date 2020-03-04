## Experimento de la doble rendija

# Inicios
El experimento de la doble rendija fue planteado originalmente en 1801 por Thomas Young y lo hizo con la intención de determinar si la luz se comportaba como onda o como partícula.


En la siguiente imagen se pude observar cómo es el comportamiento de las partículas vs el comportamiento de las ondas realizando el mismo experimento.

![image](https://user-images.githubusercontent.com/53798019/75840496-5ecb9080-5d99-11ea-9e36-2c4ad91a21b4.png)

es importante recalcar dichos comportamientos, ya que los patrones que generan ambos discrepan.


## Experimento Casero

Antes de mostrar la forma en que se desarrollo  el experimento se mencionaran los materiales que fueron utilizados para este experimento:

**Materiales:**
- 1/4 de cartoon paja 
- bisturi
- laser
- regla 
- papel 
- marcador de color negro


# Empezando

- Se realizaron cortes al carton paja, para crear un  soporte en el cual se colocaria el laser, este soporte a su vez se fijaria a una base para que no se moviera.

- Luego con una forma rectagular se corta un pedazo de carton paja el cual se tomara como soporte para la rendija y este tambien estara fijo a la base.

- Para la construccion de la rendija cortamos un pedazo de papel con forma de rectangulo y realizamos dos cortes finos con el bisturi de forma paralela *(los cuales representaran la doble rendija)*

-Con el marcador, rayamos la rendija para que al realizar el experimento no pasen los fotones a traves del papel

El resultado de estos pasos es como el que se muestra en la imagen:
![image](https://user-images.githubusercontent.com/53798019/75843488-48c1ce00-5da1-11ea-9ef0-99a95b922e55.png)


![image](https://user-images.githubusercontent.com/53798019/75843715-d0a7d800-5da1-11ea-9833-04c4231fb213.png)


![image](https://user-images.githubusercontent.com/53798019/75843793-19f82780-5da2-11ea-862e-f2eca95cb03b.png)






## Sistema 
![image](https://user-images.githubusercontent.com/53798019/75600835-61b93f00-5a82-11ea-9b08-d9b01abfdc87.png)

## Matriz asociada al sistema
![image](https://user-images.githubusercontent.com/53798019/75600862-cbd1e400-5a82-11ea-9aba-1d3151e20887.png)

## Estado inicial del sistema 
![image](https://user-images.githubusercontent.com/53798019/75600871-e1dfa480-5a82-11ea-974d-5d833c298ba9.png)

## Representacion en la libreria
- Representacion de la matriz en la libreria corresponde a :
```
matrix = [   [ [0, 0], [0, 0] , [0, 0] ,[0, 0] ,[0, 0]    ],
             [  [0, 0], [0, 0] , [0, 0] ,[0, 0] ,[0, 0]  ],
	     [  [0, 0], [1, 0] , [0, 0] ,[0, 0] ,[1, 0]   ],
	     [  [0, 0], [0, 0] , [0, 0] ,[0, 0] ,[0, 0]  ],
	     [  [0, 0], [0, 0] , [1, 0] ,[0, 0] ,[0, 0] ],
	     [  [1, 0], [0, 0] , [0, 0] ,[1, 0] ,[0, 0]   ]]
```

- Representacion del vector en la libreria corresponde a :
```
vector = [ [6, 0],
 	   [2, 0],
	   [1, 0],
	   [5, 0] ,
	   [3, 0] ,
	   [10, 0]]
```

### Pre-requisitos

- Tener instalado una version mayor o igual a python 3
- Tener instalado las librerias numpy, scipy y matplotlib - python
- Es opcional tener instalado git 



### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link 
https://www.python.org/downloads/ .

En caso de no tener instalado git, este  se podra descargar del siguiente link 
https://git-scm.com/downloads.

En caso de no tener instalado numpy, scipy y matplotlib - python, seguir los pasos del siguiente video https://www.youtube.com/watch?v=oE4KeuVNqcQ&list=LLwZJu6f8CavefyakHGC1HEw





## Ejecutando Programa 

Para ejecutar el programa se deben seguir los siquientes pasos:

1) Descargar el repositorio en git usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/classicalToQuantum

```
3) ejecutar el archivo con el siguiente comando 

```
python classicalToQuantum.py
```

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.
Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en classicalToQuantumTest.py ,en este .py se encontraran  pruebas por cada una de las funciones implementadas sobre sistemas.

- **Primer prueba**: Prueba asociada al experimentos #1, la cual dada una matriz de elementos booleanos y un vector de estado inicial de un sistema deterministico, calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testExperimentBooleanMatrix( self  ):
        booleanMatrix = [...]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [False, True, True, False, False, False] )
```

- **Segunda prueba**: Prueba asociada al experimento #2, la cual dada una matriz de elementos que representa una probabilidad y un vector de estado inicial de un sistema probabilistico ( ** experimento de las multiples rendijas ** ), calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testMultipleSlitQuantumExperiment( self ):
	matrix = [...]
	vectIni = [...]
        self.assertEqual( probabilisticSystem( matrix[:], vectIni[:], 1 ), [...] )
```


- **Tercera prueba**:  Prueba asociada al experimento #3, la cual dada una matriz de elementos de numeros imaginarios y un vector de estado inicial de un sistema probabilistico cuantico  ( ** experimento de las multiples rendijas ** ), calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testExperimentBooleanMatrix( self  ):
	matrix = [...]
	vectIni = [...]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [False, True, True, False, False, False] )
```



- **Cuarta prueba**:   Prueba asociada a la funcion #4, la cual dado un vector de estado de un sistema probabilistico, logre graficar la probabilidad en cada uno de los estados.

```
def testGraphProbabilitiesVector( self ):
         graphProbabilitiesVector( [ [0,0] ,[0,0]  ,[0,0] ,
                                     [1/6,0],[1/6,0], [1/3,0],
                                     [1/6,0],[1/6,0] ]  )
```



## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Implementations/classicalToQuantum

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python classicalToQuantumTest.py
```


## Autor

**Iván Camilo Rincón Saavedra** - *Latest Commmit* - [Rincon10](https://github.com/Rincon10)


## Referencias
El modelo que se siguio para diseñar el README	fue tomado del usuario:

[PurpleBooth](https://github.com/PurpleBooth)


