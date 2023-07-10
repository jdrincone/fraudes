# Fraudes en reclamaciones a sinistros

### Este repositorio contiene la solución a la prueba de selección para [DATA SCIENTIST en  R5](https://bitbucket.org/wilmards/r5-ds-challenge/src/master/)

- La solución de los puntos del 1 al 4 se en encientran en `\input\problema_posgres.sql` y su explicación se encuentra en el
notebook de trabajo `\fradues\notebook\notebook.ipynb`
- La solución del punto 5 es un tablero realizado en Power BI [aqui](https://app.powerbi.com/view?r=eyJrIjoiNTdkYTJiMGYtZjBlNS00ZTIwLWIzNWItNTk5YTZlZTM3YTJmIiwidCI6Ijk5ZTFlNzIxLTcxODQtNDk4ZS04YWZmLWIyYWQ0ZTUzYzFjMiIsImMiOjR9)
y en la raiz de este repositorio `tablero_fraudes.pbix`

- El punto 6
Las conclusiones generales después de analizar los datos con el notebook y Power BI, probar modelos de clasificación
para detectar cuando una reclamación es un fraude y asi reducir las perdidas en dinero se pueden revisar el final
del notebook de trabajo.

![My Image](images/confusion_matrix.png)

#!!! **Extra:** este repositorio se realizó con el objetivo de emular el desarrollo de un proyecto real, siguiendo
los lineamientos de la información que se encuentra en la rama de master, para su instalación y funcionamiento
se debe seguir los siguientes pasos:
- Clonar el repositorio

```git https://github.com/jdrincone/fraudes.git```

- Crear un entorno virtual e installar los requerimientos

```pip install -r requeriments.txt```

- Actualizar el modelo

```$ python actualizar_modelo.py```

- Levantar la api

```uvicorn app_fraudes:app```

**En lo los anteriores pasos se ha realizado**

- Estructura de repositorio siguiendo las buenas practicas de desarrollo y siguiento los convensional commits.
- Aplicación reglas del PEP8 para tener un código a lo pytonista.
- Scripts para procesamiento y entrenamientos los cuales se encuentran en el modulo de `src`
- Dado que no es debido subir a los repositorios la fuente de datos y menos credenciales de Bases de datos o
  fuentes de almacenamiento como el S3, en este caso, se toma los datos iniciales desde ruta en el S3 que temporalemte
  estará abierta.
- Creación script principal para actualizar modelo de clasificación.
- Creación API que dado las parámetros de una reclamación se indica si esta es un fraude o no, dentro de lo
  que el modelo lo permite.

![params](images/params.png)
![prediction](images/prediction.png)

**Consideraciones a futuro**
A futuro se debe dockerizar la aplicación, crear funciones de testeo para el código que deben de estar en integracción
 continua (CI) por medio de un pipeline con las git actions. El modelo y los datos se tactualizan continuamente
 por tanto se debe realizar un pipeline para esta labor. De igual modo que se tiene completa trazabilidad del 
 código, se debe tener trazabilidad de los datos y esto se logra con data version control (DVC).
Por ultimo, el servicio puede ser desplegado por medio de una lambda fuction de AWS. (Trabajo es lo que hay!!!)