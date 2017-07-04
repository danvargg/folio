library(shinythemes)

source("pred.R")

shinyUI(fluidPage(
        theme = shinytheme("darkly"),
        tags$hr(),
        titlePanel("Next Word Prediction Application"),
        tags$hr(),
        
        mainPanel(tabsetPanel(
                tabPanel("Prediction",
                         sidebarLayout(
                                 sidebarPanel(
                                         width = 3,
                                         tags$p(""),
                                         tags$h5("Predicted next word:"),
                                         flowLayout(
                                                 actionButton("b1", label = textOutput("texti1")),
                                                 actionButton("b2", label = textOutput("texti2")),
                                                 actionButton("b3", label = textOutput("texti3"))
                                         )
                                 ),
                                 mainPanel(
                                         tags$p(""),
                                         tags$h5("Please, enter your text:"),
                                         h4(tags$textarea(id = "texti", rows = 5, cols = 30, "")))
                         )),
                tabPanel("About", includeMarkdown("README.md"))
        ))
))