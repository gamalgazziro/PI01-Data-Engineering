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
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

C- La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

D- Película que más duró según año, plataforma y tipo de duración

E- Cantidad de series y películas por rating
