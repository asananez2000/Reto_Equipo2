# Reto_Equipo2

## **Descripción del Proyecto**<br>
En este repositorio se encuentra el proyecto final de la Semana Tec "Herramientas computacionales: el arte de la programación", el cual consiste en la modificación de diversos juegos programados en Python y particularmente en la colaboración e integración de los mismos. <br>
<br>
**Código Original:** http://www.grantjenks.com/docs/freegames/index.html <br>
**Juegos incluidos:**
-	Paint
-	Snake
-	Pacman
-	Cannon
-	Memory <br>

## Instalación del Módulo Freegames
Para poder correr los programas del presente repositorio es necesario tener instalado el módulo “freegames”. Dichas instrucciones de instalación se encuentran a continuación: <br>
1.	Primero, asegúrese de tener instalado Python 3 en su computadora así como de poder llamarlo desde su terminal. 
2.	Instale el instalador “pip” desde la siguiente liga: https://bootstrap.pypa.io/get-pip.py
3.	Corra el instalador desde su terminal: <br>
`python3 get-pip.py`
4.	Instale el módulo: <br>
`pip install freegames`

## Aportaciones de los Integrantes del Equipo
-	**Andreína Sanánez / A01024927** <br>
Como parte de mi colaboración para la entrega final modifiqué los siguientes archivos: <br>
    •	`memory.py`: en el cual le agregué comentarios a cada sección del programa y cree las variables grid_dim y sqr_len para no solo cambiar las dimensiones de la cuadrícula a           una de 4x4, sino para facilitar cambios de estas en el futuro. <br>
    
    •	`canon.py` : en el cual generé una lista de colores que se selecciona aleatoriamente para que los targets cambien de color de forma intermitente, así como aumente el tamaño de       dichos targets y de la pelota.<br>
    
    •	`snake.py`: en este programa, añadí una variable “speed” para aumentar la velocidad de la serpiente e incrementar la dificultad del juego. <br>
    
 ##
-	**Tonatiuh Reyes / A01025459** <br>
Como parte de mi colaboración para la entrega final modifiqué los siguientes archivos: <br>

    •	`cannon.py` : Modifique las variables de las velocidades en "y" tanto en los objetivos como en la pelota. De modo que a los primeros se les agrego un factor de "Gravedad" en su movimiento y al segundo, que varie por tiro la gravedad de este.<br>
##
-	**Guillermo Nunez / A01025459** <br>
Como parte de mi colaboración para la entrega final modifiqué los siguientes archivos: <br>

    •	`pacman.py` : Modifiqué el tablero para agregar un nuevo camino lateral para que Pacman viajara. <br>

    •	`pacman.py` : Agregué dos nuevos fantasmas para perseguir a Pacman y hacer el juego un poco más difícil.. <br>

    •	`pacman.py` : Modifiqué el valor y del punto de partida de Pac Man para que comience más cerca del centro. <br>
    
