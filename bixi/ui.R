library(shiny)
library(shinythemes)
library(leaflet)

source("bixi.R")

shinyUI(fluidPage(
        theme = shinytheme("darkly"),
        titlePanel("Real Time Bixi Stations in Montreal"),
        mainPanel(tabsetPanel(
                tabPanel("Stations",
                         leafletOutput("map", height = "800px", width = "1600px"),
                         tabPanel("About", includeMarkdown("bixi.md"))
                ))
        )
        
))