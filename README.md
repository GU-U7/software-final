# software-final


Como se aprecia en el resumen general de los stress test:
- Throughputs de acuerdo a los lineamientos (post: 40 req/sec ; get: 20 req/sec)
- Se obtiene un error de 0%
![](img/REPORTE_RESUMEN.jpg)

Timeout establecido de requests:
![](img/GET_TIMEOUT.jpg)
![](img/POST_TIMEOUT.jpg)

Detalles de las consultas y respuestas:
POST (INCLUYE HEADERS):
![](img/POST_REQUEST.jpg)
![](img/POST_RESPONSE.jpg)
![](img/POST_HEADER.jpg)

GET:
![](img/GET_RESPONSE.jpg)
![](img/GET_RESPONSE.jpg)

Finalmente observamos que los gráficos de thread groups muestra que el tiempo nunca es excedido con sus throughputs definidos:
PUBLISH (2000 ms):
![](img/GRAFICO_PUBLISH.jpg)
SUBSCRIBE (1000ms):
![](img/GRAFICO_SUBSCRIBE.jpg)
