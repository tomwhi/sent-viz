library(ggplot2)
x <- read.table("tSNE_results_2components.txt", sep="\t", header=TRUE)

png("1vs2_tSNE_3components.png", width=1000, height=1000)
plot(x[,1], x[,2], col=x[,3], pch=16, cex=1)
#text(x[,1], x[,2], labels = rownames(x), cex=0.5)
dev.off()

