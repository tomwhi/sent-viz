library(ggplot2)
x <- read.table("tSNE_results_2components.txt", sep="\t", header=TRUE)
filt<-x[x$topic == "Charlie Parker",]


png("1vs2_tSNE_3components.png", width=1000, height=1000)
plot(0, xlim=c(-20,20), ylim=c(-20,20), cex=0.01)
for (paragraph in unique(filt$paragraph_idx)) {
  curr_par <- filt[filt$paragraph_idx == paragraph,]
  text(curr_par$comp1[1], curr_par$comp2[1], curr_par$paragraph_idx, col=curr_par$paragraph_idx)
  lines(curr_par$comp1, curr_par$comp2, cex=1, col=curr_par$paragraph_idx)
  points(curr_par$comp1, curr_par$comp2, cex=0.5, pch=16, col=curr_par$paragraph_idx)
}
dev.off()
