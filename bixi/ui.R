library(shiny)
library(shinythemes)
library(leaflet)

shinyUI(fluidPage(
        tags$style(type = "text/css", "#map {height: calc(100vh - 120px) !important;}"),
        theme = shinytheme("cerulean"),
        titlePanel("Real Time Bixi Stations in Montreal"),
        tabsetPanel(
                tabPanel("Stations",
                         leafletOutput("map")),
                tabPanel("About", includeMarkdown("bixi.md"))
        )
))