## Experimento de la doble rendija

# Inicios
El experimento de la doble rendija fue planteado originalmente en 1801 por Thomas Young y lo hizo con la intención de determinar si la luz se comportaba como onda o como partícula, actualmente este experimento se repoduce en una cámara oscura la cual  deja entrar un haz de luz por una rendija estrecha, cuando la luz llega a una pared intermedia de  dos rendijas, la luz debe pasar por alguna de estas dos y chocar con una placa que se encuentra despues de la rendija .


En la siguiente imagen se pude observar cómo es el comportamiento de las partículas en el experimento.

![image](https://user-images.githubusercontent.com/53798019/76539289-92b84d00-644e-11ea-92df-48442a1831d2.png)
![image](https://user-images.githubusercontent.com/53798019/76539496-d90dac00-644e-11ea-8118-415db8201075.png)
![image](https://user-images.githubusercontent.com/53798019/76540305-f7c07280-644f-11ea-8610-5f409855351d.png)


más adelante se explicara el porque se presenta este comportamiento.


## Experimento Casero

Antes de mostrar la forma en que se desarrollo  el experimento se mencionaran los materiales que fueron utilizados para este experimento:

**Materiales:**
- 1/4 de cartoon paja 
- bisturi
- laser
- regla 
- papel 
- mina 0.5 o hilo 


# Empezando

- Se realizaron cortes al cartón paja, para crear un soporte en el cual se colocaría el láser, este soporte a su vez se fijaría a una base para que no se moviera.

- Luego con una forma rectangular se corta un pedazo de cartón paja el cual se tomará como soporte para la rendija y este también estará fijo a la base.

- Para la construcción de la rendija se puede hacer de dos formas la primera es colocar la mina justamente pegada al laser, colocar un hilo en la figuta rectangular de tal manera que sea perpendicular a la base  *(los cuales representaran la doble rendija) *


# Proceso:

![image](https://user-images.githubusercontent.com/53798019/76020821-268b9580-5ef2-11ea-8f11-e2ca34942eb1.png)

![image](https://user-images.githubusercontent.com/53798019/76020694-e0cecd00-5ef1-11ea-8e07-51b32bd5413d.png)

![image](https://user-images.githubusercontent.com/53798019/76020764-052aa980-5ef2-11ea-94bf-b9cf57e9981e.png)


El resultado de estos pasos es como el que se muestra en la imagen:
![image](https://user-images.githubusercontent.com/53798019/75843488-48c1ce00-5da1-11ea-9ef0-99a95b922e55.png)


![image](https://user-images.githubusercontent.com/53798019/75843715-d0a7d800-5da1-11ea-9833-04c4231fb213.png)


![image](https://user-images.githubusercontent.com/53798019/75939978-cb0dc900-5e59-11ea-9cc1-4d793654a7b5.png)


# Desarrollo Experimento
Para realizar la simulación del experimento se debe apuntar con un láser a la redija ya creada y montada, según lo observado se ve que el resultado se asemeja más al comportamiento de ondas con el patrón de interferencia, pero esto en  la época del experimento  desconsternaba a los científicos el hecho de que al poner detectores después de la rendija para saber por dónde pasaba la luz el patrón del experimento era equivalente al de las partículas, lo que nos da entender que cuando el experimento está siendo monitoreado nos da como resultado el de las partículas y cuando no el resultado es el de patrón de interferencia de las ondas, como se muestra a continuación:

![image](https://user-images.githubusercontent.com/53798019/75939978-cb0dc900-5e59-11ea-9cc1-4d793654a7b5.png)

![image](https://user-images.githubusercontent.com/53798019/75940145-2fc92380-5e5a-11ea-9428-54fa5f43ce30.png)


![image](https://user-images.githubusercontent.com/53798019/75844199-495b6400-5da3-11ea-88bd-993922dc9d39.png)

A continuación un vistazo con mas detalle sobre el experimento realizado, en el siguiente enlace https://www.youtube.com/watch?v=46sw1-2oxFI.

Para poder lograr entender el resultado del experimento en la época aplicaron el principio de superposición cuántico en el que dice que las partículas (en este caso la luz) puede  dos o más valores de una determinada magnitud (su posición ) tambien conocida como  **"onda de posibilidades"** que pasan por las dos ranuras para luego interferir con ella misma hasta que golpear la pared de impacto  y que al ser monitoreado este se ve afectado a que se dice que este principio colapsa y solo   lograremos observar una de todos los posibles resultados.


## Sistema

Antes de seguir se debe tener en cuenta la forma en que el experimento sera representado como un sistema cuantico, este sistema tendra una matriz de adyacencia asociada y un vector el cual representara el estado inicial del sistema, donde sus posiciones representaran el peso de una conexion especifica entre componentes del sistema, a continuacion se mostrar un ejemplo del sistema cuantico para el experimento de la doble rendija.

## Simulacion del Experimento 
![image](https://user-images.githubusercontent.com/53798019/75844546-5b89d200-5da4-11ea-9f58-34fa00904b27.png)

*grafica 1*

## Matriz asociada al sistema
![image](https://user-images.githubusercontent.com/53798019/75844753-fda9ba00-5da4-11ea-9168-6ac8bf285863.png)

*grafica 2*

## Representacion en la libreria
- Representacion de la matriz en la libreria corresponde a :
```
matrix = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [0, 0],[1, 0], [0, 0], [0,0]],
         [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
          [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
```



### Pre-requisitos

- Tener instalado una version mayor o igual a python 3
- Es opcional tener instalado git 



### Instalando y ejecucion del programa

En caso de no tener instalado python o tener python 2.7 ,este  se podra descargar del siguiente link 
https://www.python.org/downloads/ .

En caso de no tener instalado git, este  se podra descargar del siguiente link 
https://git-scm.com/downloads.

### Pruebas del programa 

Las pruebas en un programa son muy importantes, tanto es asi que estas permiten verificar que las funcionalidades del programa se cumplen en cada iteración correctamente.
Para este caso se usa la libreria de python  **unittest**; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es  importada con la linea de codigo **import unittest** que se encuentra en Test.py ,en este .py se encontraran  pruebas por cada una de las funciones implementadas sobre sistemael experimento de doble rendija.


**Prueba**:  Prueba  la cual dada una matriz de elementos de numeros imaginarios y un vector de estado inicial de un sistema probabilistico cuantico  ( ** experimento de las multiples rendijas ** ), calcula el estado final que este se encontrara dado un numero de veces que este cambiara.

```
def testExperimentBooleanMatrix( self  ):
	matrix = [...]
	vectIni = [...]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                          [0.16, 0.33, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
			  [........])
```


## Ejecutando Pruebas

Para ejecutar las pruebas se deben seguir los siquientes pasos:

1) Descargar el repositorio en git hub usando el comando git clone  
```
git clone https://github.com/Rincon10/CNYT.git
```

2)  abrir el lugar donde se encuentra la implementacion
```
cd Experimento Doble Rendija

```

3) ejecutar las pruebas  con el siguiente comando 

```
 python Test.py
```


## Autores

- **Iván Camilo Rincón Saavedra** - *Latest Commmit* - [Rincon10](https://github.com/Rincon10)
- **Nicolas Torres Paez** - [Novenix](https://github.com/Novenix)
- **Lorenzo Marquez Pinto** -[DrLolo03](https://github.com/DrLolo03) 



## Bibliografia 
 - Yanofsky, N. and Mannucci, M. (2018). Quantum computing for computer scientists. Cambridge: Cambridge University Press, pp.88-97, grafica 1, grafica2. - 

- Mecánica cuántica, experimento de la doble rendija. (2012). [video] Directed by A. Garcia Orduña. https://www.youtube.com/watch?v=SzX-R38dZQw.
