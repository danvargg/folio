library(plyr)
library(shiny)
library(shinythemes)
library(shinyBS)
library(rCharts)
library(leaflet)

lapply(list.files(pattern = ".*.RData"), load, envir = .GlobalEnv)

cities <- cities[, c(1, 7, 6, 4, 3)]

colnames(d)[1] <- "ID"
colnames(d)[2] <- "Location"
d <- d[, c(1, 2, 5, 4, 3, 6, 10, 13, 7)]
d$Min <- as.integer(d$Min)
d$Max <- as.integer(d$Max)
d$a <- substr(d$Scenario, 1, 3)
d$b <- substr(d$Scenario, 4, 6)
d$b <- as.numeric(d$b) / 10

d$Scenario <- paste(d$a, d$b, sep = " ")

locs <- unique(cities$Location)

dec.lab <- paste0(seq(2010, 2099, by = 10), "s")

brks <- c(0, 1e4, 5e4, 1e5, 2.5e5, 5e5, 1e6)
nb <- length(brks)
cities$PopClass <- cut(cities$Population, breaks=brks, include.lowest=TRUE, labels=FALSE)
cities$PopClass[is.na(cities$PopClass)] <- 1

## Markers colors
palfun <- colorFactor(
        palette = c("navy", "navy", "magenta4", "magenta4", "red", "red"), 
        domain = 1:(nb - 1))