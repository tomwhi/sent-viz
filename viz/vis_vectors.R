library(ggplot2)
args <- commandArgs(TRUE)

input_filename <- args[1]
output_filename <- args[2]

sentence_data <- read.table(input_filename, sep="\t", header=TRUE)

ggplot(sentence_data, aes(comp1, comp2)) + geom_point(aes(colour=topic, alpha=sentence_idx))
ggsave(output_filename)