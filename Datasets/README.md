TRABAJO FINAL DATA ENGENIER HENRY

1 LIMPIEZA DE DATOS

Para este trabajo se dividio en 5 partes para su desarrollo. trabajando cada parte de la limpieza de los datos. Utilizamos las librerias de pandas y numpy para la confección del código que se describe a continuación

A- Primero tomamos las columnas de cada dataframe y con el método .astype() determinamos los datos que encontramos en cada columna. Por últmo se creó una columna id que contiene la primera letra de la variable que guarda el dataframe mas el valor de la columna show_id, repitiendo el método .astype().

B- Con la función .replace() reemplazamos los vaores nan de la columna rating, en cada dataframe, por el string 'G'. También, una vez finalizado los demas pasos, en la columna duration_type se uniformizan los stings que indican temporadas a seasons.

C- Luego con el método .split() tomamos los valores int y str de la columna duration de cada dataframe y los pusimos en dos nuevas columnas, los valores enteros se colocaron en la columna duration_int y los valores srting se colocaron en la columna duration_type. De esta forma se puede extraer información de los valores de esta columna.

D- En el caso de la columna date_added para cada dataframe ordenamos las fechas utilizamos el método pd.to_datetime().

E- por último con el método .lower() en los dataframe en cada columna que sus valores son string se uniformiza todas las letras a minúscula.

2 DESARROLLO DE LAS PREGUNTAS PEDIDAS

Se comenzo a desarrollar las preguntas que se pidieron, para ello se escribieron en lenguaje python, aunque no se alcanzo una funcionalidad optima de todas ellas, se describiran los razonamientos logicos utilizados en su confeccion.

A- Dentro de la función recibe dos parámetros llamados plataforma (para indicar en cual dataframe debe buscar) y keyword (para indicar cual es la palabra clave que se desea utilizar). Se busca que esta enumere todos los títulos en los que coincide la palabra clave dentro de la plataforma.
 En la funcion se encuentan un if segudo de tres elif todos con la misma estructura. para que sea mas claro se explicara con el primer fragmento que corresponde al if. Si el parámetro recibido en la variable es igual al strig amazon entonces este retorna una busqueda en la columna title que con el método .str.contains coloca en un dataframe de una columna por una cantidad de filas igual al numero de veces que se repite la keyword y luego con el método .shape[0] devuelve el numero de filas.

B- En este caso la función recibe tres parámetros, plataforma (para indicar a que base de datos ingresa) score (que corresponde a un puntaje numérico o int) y el anio (correspone al año de estreno).
  Dentro de la función es similar a la anterior ya que posee un if y tres elif que corresponden a cada una de las plataformas que pueden elegirse. Y cada uo responde de la siguente manera, si por ejemplo en el caso del if el parámetro plataforma fuera igual al string amazon este guarda en una variable (df) una fila si esta cumple con las condiciones de que la columna type del string amazon sea igual al sating movie ademas que la columna score sea mayor al valor score dentro del parámetro y el valor de la columna  sea igual al valor del parámetro anio, entonces esta fila es guardada en el dataframe anidado en la variable df. Para finalmente retornar el valor de df.shape[0] el cual indica el numero de filas presentes en df.

C- 
La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

D- Película que más duró según año, plataforma y tipo de duración

E- Primero Unimos en una nueva variable los 4 datafarmes con el metodo pd.concat() y axis = 0 para asi poder utilizar solamente una base de datos y aprovechando que las 4 son iguales, axis=0 nos permite que todas las columnas al estar pocisionada y nombradas igual esta se fusionan en una sola. Dentro de la funcion colocamos el parametro rating y luego colocamos una nueva variable (en este caso llamada df) que guarda: si el valor en la columna general rating es igual a el valor del parametro rating, entonces, retorna df.shape[0] esto devuelve el numero de filas que cumplen con la condicion antes mencionada. Cantidad de series y películas por rating

3) ARMADO DE APIS, REALIZACION DE CONSULTAS ONLINE
En este paso se decidio ocupar el programa FastApi. creado por un latinoamericano. El mismo presenta beneficios operativos frente a otros sistemas, como la realizacion de la "dokerizacion"de manera automatica, se busco instructivos sobre como operar con esta libreria tan util. 
Para ello fue necesario crear un archivo .py, al mismo se lo denomino main.py . este archivo contendria la importacion de fastapi, y las librerias necesarias para su ejecucion.  Su preceso de instanciado en un objeto llamado "app". el cual sera evocado mediante un "decorado" consignado por la varibale @app (app =nombre que se le otorgo a la variable) 
cada funcion se definio posterior a su vinculacion mediante este metodo. colocando las diferentes funciones creadas anteriormente en jupyter. 
luego de esta confeccion, mediante la consola se realiza un entorno virtual, mediante la descarga de fastapi y uvicorn 
se entro en este entorno virtual y se activo mediante la consola la funcion uvicorn main(nombre del archivo):app (nombre de la variable) --reload, funcion que permite cargar todos los cambios realizados en el archivo cada vez que se consulte. 

4) desde deta se descarga el Deta CLI, posteriormetnte se crea una cuenta en Deta. se coloca el comando deta loing, ingresando a nuestra cuenta en Deta. luego mediante ubicarnos (en el directorio de la consola) donde tenemos nuestros archivos.py , bases de datos limpias, un txt especifico y el programa nos facilita una direccion para realizar nuestras consultas.
