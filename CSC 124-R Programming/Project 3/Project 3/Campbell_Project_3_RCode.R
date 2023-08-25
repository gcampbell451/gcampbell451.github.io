# Gregory Campbell  Project 3   April 14, 2022

# read in xlsx, ggplot2, arules
library(readxl)
library(ggplot2)
library(arules)

OnlineShopping <- read_excel("Online Retail.xlsx")

# copy original dataset into new one called myOnlineShopping
myOnlineShopping <- OnlineShopping

# what time do people often purchase online
# extract timestamp from InvoiceDate
myOnlineShopping$Date <- as.Date(myOnlineShopping$InvoiceDate)
myOnlineShopping$Time <- format(as.POSIXct(myOnlineShopping$InvoiceDate), 
                                format = "%H:%M:%S")
g <- ggplot(myOnlineShopping, aes(x = Time))
g <- g + geom_histogram(stat = "count")
g

# how many items each customer bought
g <- ggplot(myOnlineShopping, aes(x = Quantity))
g <- g + geom_histogram(stat = "count")
g <- g + xlim(0, 30)
g

# what are the top 10 best sellers
bestSellers <- myOnlineShopping[order(-myOnlineShopping$Quantity),]
bestSellers <- bestSellers[-11:-541909,]

g <- ggplot(bestSellers, aes(x = reorder(Description, -Quantity), y = Quantity))
g <- g + geom_col()
g <- g + theme(axis.text.x = element_text(angle = 90, hjust = 1))
g

# remove unnecessary columns
# stock code
myOnlineShopping <- myOnlineShopping[-2]
# invoicedate, unit price 
myOnlineShopping <- myOnlineShopping[-4:-5]


# convert strings and numbers to factors
myOnlineShopping$InvoiceNo<- as.factor(myOnlineShopping$InvoiceNo)
myOnlineShopping$Description <- as.factor(myOnlineShopping$Description)
myOnlineShopping$Quantity <- as.factor(myOnlineShopping$Quantity)
myOnlineShopping$CustomerID <- as.factor(myOnlineShopping$CustomerID)
myOnlineShopping$Country <- as.factor(myOnlineShopping$Country)
myOnlineShopping$Date <- as.factor(myOnlineShopping$Date)
myOnlineShopping$Time <- as.factor(myOnlineShopping$Time)

# convert to tds
myOnlineShopping.trans <- as(myOnlineShopping, "transactions")

# run apriori, store in ruleset variable
ruleset <- apriori(myOnlineShopping.trans, parameter = list(support = .001, confidence = .8))
summary(ruleset)
inspect(ruleset)
sorted <- sort(ruleset, by = 'confidence', decreasing = TRUE)
inspect(sorted[1:100])


