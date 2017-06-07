#library(ggplot2)
args <- commandArgs(TRUE)
input_filename <- args[1] # "SentenceData.txt"
output_prefix <- args[2] # "ThoughtVectorViz"

library(plotly)
set.seed(100)
df <- read.table("SentenceData.txt", sep="\t", header=TRUE, quote = "", stringsAsFactors = FALSE)
p <- plot_ly(df, x = ~comp1, y = ~comp2, text = ~sentence) #, color = ~topic
htmlwidgets::saveWidget(as.widget(p), paste(output_prefix, ".html", sep=""))

#sentence_data <- read.table(input_filename, sep="\t", header=TRUE, quote = "", stringsAsFactors = FALSE)
#sentence_data$sentence_placement <- 1-(sentence_data$sentence_idx/(max(sentence_data$sentence_idx)+0.01))
#sentence_data$topic <- factor(sentence_data$topic, levels=as.character(unique(sentence_data$topic)))

#ggplot(sentence_data, aes(comp1, comp2)) + geom_point(aes(colour=topic, alpha=sentence_placement)) + scale_alpha(range = c(0.1, 0.4)) + coord_fixed() + scale_color_manual(values=c("lightblue", "darkblue", "pink", "darkred", "yellow", "orange")) + labs(x = "Component 1", y = "Component 2", title = "skip-tought vector t-SNE: bhtsne") + theme(plot.title = element_text(hjust = 0.5))
#ggsave(paste(output_prefix, "bhtsne.png", sep="_"))

#ggplot(sentence_data, aes(comp1_sklearn, comp2_sklearn)) + geom_point(aes(colour=topic, alpha=sentence_placement)) + scale_alpha(range = c(0.1, 0.4)) + coord_fixed() + scale_color_manual(values=c("lightblue", "darkblue", "pink", "darkred", "yellow", "orange")) + labs(x = "Component 1", y = "Component 2", title = "skip-tought vector t-SNE: sklearn") + theme(plot.title = element_text(hjust = 0.5))
#ggsave(paste(output_prefix, "sklearn.png", sep="_"))
