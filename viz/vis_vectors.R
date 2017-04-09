library(ggplot2)
args <- commandArgs(TRUE)

input_filename <- "SentenceData.txt" #args[1]
output_prefix <- "SentenceViz" #args[2]

sentence_data <- read.table(input_filename, sep="\t", header=TRUE)
sentence_data$sentence_placement <- 1-sentence_data$sentence_idx/max(sentence_data$sentence_idx)

ggplot(sentence_data, aes(comp1, comp2)) + geom_point(aes(colour=topic, alpha=sentence_placement)) + scale_alpha(range = c(0.1, 0.6)) + coord_fixed()
ggsave(paste(output_prefix, "bhtsne.png", sep="_"))

ggplot(sentence_data, aes(comp1_sklearn, comp2_sklearn)) + geom_point(aes(colour=topic, alpha=sentence_placement)) + scale_alpha(range = c(0.1, 0.6)) + coord_fixed()
ggsave(paste(output_prefix, "sklearn.png", sep="_"))
