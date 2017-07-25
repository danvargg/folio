library(jsonlite)
library(leaflet)
library(curl)

options(digits = 10) ## Increase decimal precision for coordinates

json <- as.data.frame(fromJSON("https://secure.bixi.com/data/stations.json"))

## id: Idenfiant unique de la station
## s: Nom de la station
## n: Identifiant du terminale de la station,
## st: etat de la station
## la: latitude de la station
## lo: longitude de la station
## da: Nombre de bornes disponibles a cette station
## ba: Nombre de velos disponibles a cette station

json$lat <- json$stations.la
json$lng <- json$stations.lo

json$stations.st = factor(json$stations.st,
                           levels = c(0, 1),
                           labels = c("Inactive", "Active"))