# load airquality dataset into new set named airquality
myairquality <- airquality

# clean up NAs
myairqualityClean <- na.omit(myairquality)

# create histograms for each variable, number of bins chosen by taking
# the square root of the number of data points and rounding up = 11,
# binwidth calculated by taking the range of the data points and dividing
# by number of bins, rounding up
library(ggplot2)
# ozone
ozoneHist <- ggplot(myairqualityClean, aes(x=Ozone))
ozoneHist <- ozoneHist + geom_histogram(binwidth = 15, color="black", fill="light blue")
ozoneHist <- ozoneHist + ggtitle('Ozone Histogram')
ozoneHist

# solar.r
solarrHist <- ggplot(myairqualityClean, aes(x=Solar.R))
solarrHist <- solarrHist + geom_histogram(binwidth = 30, color="black", fill="light blue")
solarrHist <- solarrHist + ggtitle('Solar.R Histogram')
solarrHist

# wind
windHist <- ggplot(myairqualityClean, aes(x=Wind))
windHist <- windHist + geom_histogram(binwidth = 2, color="black", fill="light blue")
windHist <- windHist + ggtitle('Wind Histogram')
windHist

# temp
tempHist <- ggplot(myairqualityClean, aes(x=Temp))
tempHist <- tempHist + geom_histogram(binwidth = 4, color="black", fill="light blue")
tempHist <- tempHist + ggtitle('Temp Histogram')
tempHist

# month
monthHist <- ggplot(myairqualityClean, aes(x=Month))
monthHist <- monthHist + geom_histogram(binwidth = 1, color="black", fill="light blue")
monthHist <- monthHist + ggtitle('Month Histogram')
monthHist

# day
dayHist <- ggplot(myairqualityClean, aes(x=Day))
dayHist <- dayHist + geom_histogram(binwidth = 3, color="black", fill="light blue")
dayHist <- dayHist + ggtitle('Day Histogram')
dayHist

# boxplot for Ozone
ozoneBox <- ggplot(myairqualityClean, aes(x=as.factor(Month), y=Ozone))
ozoneBox <- ozoneBox + geom_boxplot(fill="light blue")
ozoneBox <- ozoneBox + ggtitle('Ozone Boxplot')
ozoneBox

# boxplot for wind
windBox <- ggplot(myairqualityClean, aes(x=as.factor(Month), y=Wind))
windBox <- windBox + geom_boxplot(fill="light blue")
windBox <- windBox + ggtitle('Wind Boxplot')
windBox

# explore how the data changes over time
# create appropriate dates
myairquality$Date <- as.Date(paste("1973", myairquality$Month, myairquality$Day, sep = "-"))

# create line charts for ozone, temp, wind, and solar.r
# ozone
ozoneLine <- ggplot(myairquality, aes(x=Date, y=Ozone))
ozoneLine <- ozoneLine + geom_line(color = "blue")
ozoneLine <- ozoneLine + ggtitle('Ozone Levels, New York, May 1-Sep 30, 1973')

# temp
tempLine <- ggplot(myairquality, aes(x=Date, y=Temp))
tempLine <- tempLine + geom_line(color = "red")
tempLine <- tempLine + ggtitle('Ozone Levels, New York, May 1-Sep 30, 1973')
tempLine

# wind
windLine <- ggplot(myairquality, aes(x=Date, y=Wind))
windLine <- windLine + geom_line(color = "green")
windLine <- windLine + ggtitle('Ozone Levels, New York, May 1-Sep 30, 1973')
windLine

# solar.r
solarLine <- ggplot(myairquality, aes(x=Date, y=Solar.R))
solarLine <- solarLine + geom_line(color = "orange")
solarLine <- solarLine + ggtitle('Ozone Levels, New York, May 1-Sep 30, 1973')
solarLine

# create chart with all 4
allFour <- ggplot(myairquality, aes(x=Date, y=Ozone)) + geom_line(color="blue")
allFour <- allFour + geom_line(aes(x=Date, y=Temp), color = "red")
allFour <- allFour + geom_line(aes(x=Date, y=Wind), color = "dark green")
allFour <- allFour + geom_line(aes(x=Date, y=Solar.R), color = "orange")
allFour <- allFour + ggtitle("Ozone, Temp, Wind, Solar.R for New York, May 1-Sep 30, 1973")
allFour <- allFour + labs(y = "Ozone(Blue), Temp(Red), Wind(Green), Solar.R(Orange)")
allFour

# look at all the data via a heatmap



# look at all the data via a scatter chart with wind along the x-axis and temperature along
# the y-axis, size representing ozone, color representing solar.r
scatter <- ggplot(myairquality, aes(x=Wind, y=Temp))
scatter <- scatter + geom_point(aes(size=Ozone, color=Solar.R))
scatter <- scatter +ggtitle("Wind vs. Temperature with Ozone by Size and Solar.R by Color, May 1-Sep 30, 1973")
scatter <- scatter + labs(y="Temperature")
scatter
