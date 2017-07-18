library(jsonlite)
library(leaflet)

options(digits = 10) ## Increase decimal precision for coordinates

## s1 <- Sys.time()
json <- as.data.frame(fromJSON("https://secure.bixi.com/data/stations.json"))
## e1 <- Sys.time()
## jtime <- e1 - s1
## jtime

## id: Idenfiant unique de la station
## s: Nom de la station
## n: Identifiant du terminale de la station,
## st: État de la station,
## b: Valeur booléenne (true ou false) spécifiant si la station est bloquée,
## su: Valeur booléenne (true ou false) spécifiant si la station est suspendue,
## m: Valeur booléenne (true ou false) spécifiant si la station est affichée comme hors service,
## lu: horodatage de la dernière mise à jour des données en nombres de millisecondes depuis le 1 janvier 1970.
## lc: horodatage de la dernière communication avec le serveur en nombres de millisecondes depuis le 1 janvier 1970.
## bk: (Pour usage futur)
## bl: (Pour usage futur)
## la: latitude de la station selon le référentiel géodésique WGS84
## lo: longitude de la station selon le référentiel géodésique WGS84
## da: Nombre de bornes disponibles à cette station
## dx: Nombre de bornes indisponibles à cette station
## ba: Nombre de vélos disponibles à cette station
## bx: Nombre de vélos indisponibles à cette station

json$lat <- json$stations.la
json$lng <- json$stations.lo

json %>% 
        leaflet() %>%
        addTiles(
                urlTemplate = "//{s}.tiles.mapbox.com/v3/jcheng.map-5ebohr46/{z}/{x}/{y}.png",
                attribution = 'Maps by <a href="http://www.mapbox.com/">Mapbox</a>'
        ) %>% 
        addCircleMarkers(~lng, ~lat, 
##                          popup = ~as.character(id), 
                         radius = 5, 
                         color = "black", 
                         stroke = FALSE, 
                         fillOpacity = 0.7)