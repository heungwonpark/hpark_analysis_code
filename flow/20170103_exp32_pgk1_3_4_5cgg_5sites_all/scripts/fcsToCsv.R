library('flowCore')
listOfFiles <- list.files(
    path='rawdata', pattern='.fcs$', full.names=TRUE)

convertToCsv <- function(infile) {
    data <- read.FCS(infile, transformation=FALSE)
    outfile <- gsub(".fcs",".csv", infile)
    write.csv(exprs(data), outfile)
}

temp <- lapply(listOfFiles, convertToCsv)
