# Gregory Campbell Project 1
# 1.
proj1_data <- read.csv("F:/CPCC/2022/CSC 124-N801 Intro to Data Science Programming/Project 1/proj1_data.csv")
colnames(proj1_data) <- c('date', 'state', 'fips', 'cases', 'deaths')
# 2.
# attaching dplyr package is necessary to use filter()
cleanData <- filter(proj1_data, date >= '2020-03-01')
# 3.
cleanData <- cleanData[,-3]
proj1_data <- proj1_data[,-3]
# 4.
mean(cleanData$cases)
# 5.
clean2020 <- filter(proj1_data, date < '2021-01-01')
mean(clean2020$cases)
clean2021 <- filter(proj1_data, date >= '2021-01-01')
mean(clean2021$cases)
# 6.
sortOnCases <- proj1_data[order(-proj1_data$cases),]
head(sortOnCases, 1)
# 7.
ncData <-filter(proj1_data, state == 'North Carolina')
# 8.
ncData2020 <- filter(ncData, date < '2021-01-01')
mean(ncData2020$cases)
ncData2021 <- filter(ncData, date >= '2021-01-01')
mean(ncData2021$cases)
# 9.
sortNCCases <- ncData[order(-ncData$cases),]
head(sortNCCases, 1)
# 10.
totalDeaths <- sum(proj1_data$deaths)
totalCases <- sum(proj1_data$cases)
totalDeathsNC <- sum(ncData$deaths)
totalCasesNC <- sum(ncData$cases)
mortalityRate <- totalDeaths / totalCases * 100
mortalityRateNC <- totalDeathsNC / totalCasesNC * 100
mortalityRate
mortalityRateNC


