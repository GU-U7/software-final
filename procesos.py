from soupsieve import select


insertar = lambda message, topic: "insert into mensajes values('"+str(message)+"','"+str(topic)+"');"

buscar = lambda topic: "select message, topic from mensajes where topic = '"+str(topic)+"';"