#!/usr/bin/env Rscript
#
# Invoke: RScript hotdog.R
# Output: Histogram of Calories vs Sodium for various hotdog types 
#
# Written for HW 2.12 in 
# Probability and Statistics for Computer Scientists by D.A. Forsyth (Sep 2014)

library(gdata)
data <- read.csv("hot-dogs.csv")

library(ggplot2)
plot <- ggplot(data, aes(x=Calories, y=Sodium)) + geom_point(shape=1)
plot <- plot + facet_grid(. ~ Type)
ggsave(plot, file="Hotdog-Histogram.png")