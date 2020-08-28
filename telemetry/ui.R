library(shiny)
library(shinydashboard)
library(leaflet)
library(plotly)

shinyUI(dashboardPage(
  skin = "yellow",
  dashboardHeader(title = "Telemetry analysis"),
  dashboardSidebar(
    width = 150,
    sidebarMenu(
      menuItem("Time Series", tabName = "series", icon = icon("bar-chart")),
      menuItem("Raw data", tabName = "raw", icon = icon("database")),
      menuItem("Map", tabName = "map", icon = icon("map-o")),
      checkboxGroupInput("sys",
                         "System:",
                         c("iOS" = "iOS",
                           "Andorid" = "Android")),
      checkboxGroupInput("user",
                         "Area:",
                         c("Montreal" = "iOS",
                           "Brasil" = "Android")),
      dateRangeInput("daterange", "Date range:", start="2017-06-05", end = "2017-06-07")
    )
  ),
  dashboardBody(
    tabItems(
      # First tab content
      tabItem(tabName = "series",
              fluidRow(
                fluidRow(
                  infoBox("Devices", 
                          value=length(unique(aux$device_trip_id)), width=3, 
                          icon = shiny::icon("mobile-phone")),
                  infoBox("Unique Events", value=length(unique(aux$type)), width=3, 
                          icon = shiny::icon("map-marker")),
                  infoBox("Anything else?", value=3, width=3)),
                box(width = 10, 
                  title = "Time Series", status = "success", solidHeader = TRUE,
                    collapsible = TRUE,
                    plotlyOutput("plot1", height = 450)
                )
              )
      ),
      
      # Second tab content
      tabItem(tabName = "raw",
              dataTableOutput('table')
      ),
      tabItem(tabName = "map",
              fluidPage(
                tags$style(type = "text/css", "#map {height: calc(100vh - 80px) !important;}"),
                leafletOutput("map", height = 800)
                )
    ))
  )
))
