import mysql.connector

config= {
    "user":"root",
    "password":"",
    "host":"127.0.0.1",
    "database":"suscripciones"
}
  
conexion =mysql.connector.connect(**config)