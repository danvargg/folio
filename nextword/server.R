library(shiny)
library(shinythemes)
library(markdown)

source("pred.R")

shinyServer(function(input, output, session) {
        
        pt1 <- reactive(p(input$texti)[1])
        output$texti1 <- pt1
        observeEvent(input$b1, { 
                updateTextInput(session, "texti",
                                value = paste(input$texti, pt1()))
        })
        pt2 <- reactive(p(input$texti)[2])
        output$texti2 <- pt2
        observeEvent(input$b2, { 
                updateTextInput(session, "texti",
                                value = paste(input$texti, pt2()))
        })
        pt3 <- reactive(p(input$texti)[3])
        output$texti3 <- pt3
        observeEvent(input$b3, { 
                updateTextInput(session, "texti",
                                value = paste(input$texti, pt3()))
        })
})