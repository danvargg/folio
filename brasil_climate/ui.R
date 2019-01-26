shinyUI(navbarPage(
        theme=shinytheme("paper"),
        title="Welcome",
        tabPanel(
                "Climate Changes in Brazil", value = "commChart"),
        collapsible=TRUE,
                   id="tsp",
                   conditionalPanel(
                           "input.tsp=='commChart'",
                                    fluidRow(
                                            ##column(8, h5("Data")),
                                            column(8,
                                                   fluidRow(
                                                           column(6, selectInput(
                                                                   "location", "Community", 
                                                                   c("", locs), selected="", 
                                                                   multiple=F, width="100%")),
                                                           column(6, selectInput(
                                                                   "dec", "Decades", 
                                                                   dec.lab, selected=dec.lab[c(1:9)], 
                                                                   multiple=TRUE, width="100%"))
                                                   ),
                                                   fluidRow(
                                                           column(3, selectInput(
                                                                   "variable", "Climate Variable", 
                                                                   c("Temperature", "Precipitation"), 
                                                                   selected="Temperature", multiple=F, width="100%")),
                                                           column(3, selectInput(
                                                                   "units", "Units", 
                                                                   c("C, mm", "F, in"), 
                                                                   selected="C, mm", multiple=F, width="100%")),
                                                           column(3, selectInput(
                                                                   "rcp", "RCP", 
                                                                   c("4.5 (low)", "8.5 (high)"), 
                                                                   selected="4.5 (low)", multiple=F, width="100%")),
                                                           column(3, selectInput(
                                                                   "value", "Value", 
                                                                   c("Mean", "Min", "Max"), 
                                                                   selected="Mean", multiple=F, width="100%"))
                                                   )
                                            )
                                    ),
                                    fluidRow(
                                            column(4, 
                                                   leafletOutput("Map")),
                                            column(8,
                                                   showOutput("Chart1", "highcharts"),
                                                   HTML('<style>.rChart {width: 100%; height: "auto"}</style>')
                                            )
                                    ))
))