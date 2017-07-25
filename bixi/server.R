library(shiny)

source("bixi.R")

function(input, output, session) {
        output$map <- renderLeaflet({
                invalidateLater(30000, session)
                json %>% 
                        leaflet() %>%
                        addTiles(
                                urlTemplate = "//{s}.tiles.mapbox.com/v3/jcheng.map-5ebohr46/{z}/{x}/{y}.png",
                                attribution = 'Maps by <a href="http://www.mapbox.com/">Mapbox</a>'
                        ) %>% 
                        addCircleMarkers(~lng, ~lat, 
                                         popup = paste("Station:", json$stations.s, "<br>", 
                                                       "Available Docks:", json$stations.da, "<br>", 
                                                       "Available Bikes:", json$stations.ba), 
                                         radius = 5, 
                                         color = "red", 
                                         stroke = FALSE, 
                                         fillOpacity = 0.7)
        })
}
