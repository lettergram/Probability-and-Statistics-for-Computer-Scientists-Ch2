

library(gdata)
library(ggplot2)

data <- read.csv("MagAdsReadability.csv")
data

plot <- ggplot(data, aes(factor(Group), X3Syllables))
box  <- plot + geom_boxplot()
ggsave(box, file="Boxplot-Syllable-MagAds.png")

plot <- ggplot(data, aes(factor(Group), Sentence))
box  <- plot + geom_boxplot()
ggsave(box, file="Boxplot-Sentence-MagAds.png")