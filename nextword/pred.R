library(tidyr)
library(dplyr)
library(quanteda)
library(stringr)

clean <- function(texti) {
        texti <- corpus(tolower(texti))
        tokens <- tokenize(texti, 
                           remove_numbers = TRUE,
                           remove_punct = TRUE,
                           remove_symbols = TRUE,
                           remove_separators = TRUE,
                           remove_twitter = TRUE,
                           remove_hyphens = TRUE,
                           remove_url = TRUE,
                           verbose = FALSE)
        tokens[[1]]
}

ngram <- function(texti, n = 4) {
        n <- min(n - 1, length(texti))
        
        texti <-tail(texti, n)
        texti <- paste(texti, collapse = "_")
        
        ngrams <- list()
        ngrams$bi <- word(texti, -1, -1, sep = fixed("_"))
        ngrams$tri <- word(texti, -2, -1, sep = fixed("_"))
        ngrams$tet <- word(texti, -3, -1, sep = fixed("_"))
        
        ngrams
}

p <- function(texti) {
        texti <- clean(texti)
        nwords <- length(texti)
        ngrams <- ngram(texti)
        
        if(nwords >= 3 && (!exists("prediction") || nrow(prediction) < 5)) {
                tetp <- df4[df4$sentence == ngrams$test, ]
                if (!exists("prediction")) {
                        prediction <- head(tetp, 3)
                } else {
                        prediction <- rbind(prediction, head(tetp, 3))  
                }
        }
        if(nwords >= 2 && (!exists("prediction") || nrow(prediction) < 5)) {
                trip <- df3[df3$sentence == ngrams$tri, ]
                if (!exists("prediction")) {
                        prediction <- head(trip, 3)
                } else {
                        prediction <- rbind(prediction, head(trip, 3))  
                }
        }
        if(nwords >= 1 && (!exists("prediction") || nrow(prediction) < 5)) {
                bip <- df2[df2$sentence == ngrams$bi, ]
                if (!exists("prediction")) {
                        prediction <- head(bip, 3)
                } else {
                        prediction <- rbind(prediction, head(bip, 3))  
                }
        }
        if (!exists("prediction")) {
                return(rep("the", 5))
        } else {
                prediction <- prediction[order(prediction$probability, decreasing = TRUE),]
                prediction <- prediction$prediction
                pl <- length(prediction)
                if (pl < 5) {
                        prediction <- c(prediction, rep("the", 3 - pl))
                }
                return(prediction)
        }
}