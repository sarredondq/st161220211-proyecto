# st161220211-proyecto
![](image/diagrama.png)

Contamos con tres maquinas EC2 de AWS.
## Twitter
En una hacemos la obteción de datos de twitter. Para eso está la carpeta llamanad twitter en la cual estan el codigo que recoge los datos y los manda por kafka. Para ello deberia actualizar mytiterKeys.py con sus credenciales de twitter. Ya con esto puedes hacer python3 twitter2kafka.py

## Analisis
En otra maquina tenemos la parte del analisis de sentimientos al cual es la carpeta de analsi, en debes configurar settings.py para configurar los puestos de comunicación de kafka. Se le hace una limpieza a los datos. Tambien tener en cuenta que solo cogemos los twits que tengan exteded_tweet. Ya tenindo esto en cuenta hacemos python3 sentiment_analysis.py

## ELK
Y por ultimo en la ultima maquina debemos tener instalado elastichsearch, kibana y logstach. Ya con debemos iniciar elasticsearch y kibana. Para pasar los datos de kafka a elasticsearh utilizaremos logstach con la configuración que esta en la carpeta elk. Teniendo en cuenta que logstach se ejecuta así bin/logstach le pasaremos la configuración de la siguiente manera:  bin/logstach -f etl-kafka.conf así ya recibirá los datos desde kafka y los almacenará.
