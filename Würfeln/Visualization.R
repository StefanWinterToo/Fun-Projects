library(ggplot2)
setwd("/Users/stefanwinter/Documents/FindStox/Git/Würfeln")

file <- read.csv("data/results.csv")

p <- ggplot(data = file) +
  geom_bar(width = .5, position = "dodge", stat = "count", aes(x = Face, fill = Name)) +
  theme_minimal() +
  scale_x_continuous(breaks = seq(1,6))

ggsave("vis.png")
