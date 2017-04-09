library(ggplot2)
args <- commandArgs(TRUE)

input_filename <- args[1]
output_prefix <- args[2]

sentence_data <- read.table(input_filename, sep="\t", header=TRUE)

ggplot(sentence_data, aes(comp1, comp2)) + geom_point(aes(colour=topic))#, alpha=sentence_idx
ggsave(paste(output_prefix, "_bhtsne.png"))

ggplot(sentence_data, aes(comp1_sklearn, comp2_sklearn)) + geom_point(aes(colour=topic))#, alpha=sentence_idx
ggsave(paste(output_prefix, "_sklearn.png"))
              