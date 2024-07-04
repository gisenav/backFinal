import mysql.connector

config= {
    "user":"root",
    "password":"",
    "host":"127.0.0.1",
    "database":"tp18_back"
}
  
conexion =mysql.connector.connect(**config)