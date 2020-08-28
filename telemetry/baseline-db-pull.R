library(DBI)
library(RMySQL)

conn <- dbConnect(
  drv = MySQL(),
  dbname = "device_logs",
  host = "http://xxx.php",
  username = "daniel_vargas",
  password = "mypassword")

dbListTables(conn)

rs <- dbSendQuery(conn, "SELECT * FROM `device_logs` ORDER BY `device_timestamp` DESC;")

dbFetch(rs)
##   ID           Name CountryCode      District Population
## 1  1          Kabul         AFG         Kabol    1780000
## 2  2       Qandahar         AFG      Qandahar     237500
## 3  3          Herat         AFG         Herat     186800
## 4  4 Mazar-e-Sharif         AFG         Balkh     127800
## 5  5      Amsterdam         NLD Noord-Holland     731200
dbClearResult(rs)
dbDisconnect(conn)
