library(shiny)
library(shinythemes)
library(leaflet)
library(curl)
library(jsonlite)

## id: Idenfiant unique de la station
## s: Nom de la station
## n: Identifiant du terminale de la station,
## st: etat de la station
## la: latitude de la station
## lo: longitude de la station
## da: Nombre de bornes disponibles a cette station
## ba: Nombre de velos disponibles a cette station

transdata = function() {
        json <- as.data.frame(fromJSON("https://secure.bixi.com/data/stations.json")) 
        json$lat <- json$stations.la 
        json$lng <- json$stations.lo
        return(json)
}

pal <- colorBin(c("yellow", "orange", "red", "blue", "black"), domain = transdata()$stations.da)

function(input, output, session) {
        output$map <- renderLeaflet({
                invalidateLater(60000, session)
                transdata() %>%
                        leaflet() %>%
                        addTiles(
                                urlTemplate = "//{s}.tiles.mapbox.com/v3/jcheng.map-5ebohr46/{z}/{x}/{y}.png"
                                ) %>%
                        addCircleMarkers(~lng, ~lat,
                                         popup = paste("Station:", transdata()$stations.s, "<br>",
                                                       "Available Docks:", transdata()$stations.da, "<br>",
                                                       "Available Bikes:", transdata()$stations.ba),
                                         radius = 5,
                                         color = ~pal(stations.ba),
                                         stroke = FALSE,
                                         fillOpacity = 1) %>%
                        addLegend("bottomleft", pal = pal, values = ~stations.ba,
                                  title = "Available Bikes",
                                  opacity = 1)
        })
}