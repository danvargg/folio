library(shiny)
library(shinydashboard)
library(leaflet)
library(readr)
#library(ggplot2)
library(plotly)
library(plyr)

dataset <- read_csv("device_logs-2.csv", 
                    col_types = cols(created = col_datetime(format = "%Y-%m-%d %H:%M:%S"), 
                                     device_timestamp = col_datetime(format = "%Y-%m-%d %H:%M:%S"), 
                                     uid = col_character()))

dataset$id = as.factor(dataset$id)
dataset$device_trip_id = as.factor(dataset$device_trip_id)
dataset$uid = as.factor(dataset$uid)
dataset$type = as.factor(dataset$type)
dataset$battery = as.factor(dataset$battery)
dataset$sdk = as.factor(dataset$sdk)

filter1 = dataset$type %in% c("ACCELERATION", "DECELERATION", "START_TRIP","STOP_TRIP")
aux = dataset[filter1,]

filter2 = aux$device_trip_id!= 'xxxxxxxxxxxxx'
aux = aux[filter2,]

filter3 = aux$device_timestamp >= aux$device_timestamp[aux$type=="START_TRIP"]
aux = aux[filter3,]

filter4 = aux$device_timestamp <= aux$device_timestamp[aux$type=="STOP_TRIP"]
aux = aux[filter4,]

aux$device_trip_id = 
  revalue(aux$device_trip_id,c("xxxxxxxxxx"="Device_B"))

# Define server logic required to draw a histogram
shinyServer(function(input, output, session) {
  data <- reactive({
    iniPeriodo = input$daterange[1]
    fimPeriodo = input$daterange[2]
    tsFilter = as.Date(aux$device_timestamp) >= iniPeriodo & as.Date(aux$device_timestamp) <= fimPeriodo
    aux[tsFilter,]
    
  })
  output$plot1 <- renderPlotly({
    
    invalidateLater(3.6e+6, session) #Refresh every hour
    
    p <- ggplot(data=data(), 
                aes(x=device_timestamp, y=substring(device_trip_id,1,8), color=substring(uid,12,20))) + 
      geom_line() + 
      geom_point(data = data(),
                 mapping=aes(x=device_timestamp, y=substring(device_trip_id,1,8), shape=type, color = type), size=5)
    
    ggplotly(p) %>% layout(dragmode = "select")
  })
  aux2 = aux[aux$latitude != 0, ]
  output$map <- renderLeaflet({
    leaflet() %>%
      addProviderTiles(providers$Stamen.TonerLite,
                       options = providerTileOptions(noWrap = TRUE)
      ) %>%
      addMarkers(data = aux2, 
                 label= ~as.character(type))
  })
  output$table <- renderDataTable(aux2)
  
})
