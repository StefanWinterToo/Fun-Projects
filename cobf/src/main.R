library("BatchGetSymbols")
library("PerformanceAnalytics")
library("quantmod")
library("raster")
library("extrafont")
library("ggrepel")
library("magrittr")


container <- scrape.data()

# Load stock symbols into the local environment
symbol_env <- new.env()
lapply(container$ticker, getSymbols, src = "yahoo", env = symbol_env)
listsymbols <- as.list(symbol_env)
names(listsymbols)

# Test NA
for(i in 1:length(listsymbols)){
  if(sum(is.na(listsymbols[[i]][,6]))>5){
    print(names(listsymbols[i]))
  }
  if(sum(is.na(listsymbols[[i]][,6]))<=5 && sum(is.na(listsymbols[[i]][,6]))>0){
    listsymbols[[i]][which(is.na(listsymbols[[i]][,6])),6] <- 0
    cat("added 0 to", names(listsymbols[i]))
  }
}

# Check Weekends
for(i in 1:length(container$date)){
  container$date[i] <- transform_wday_op(i)
  print(i)
}

# Add column return, calculate it for a stock and enter it at specific location
container[,"return"] <- NA
for(i in 1:length(listsymbols)){
  tryCatch(container[which(container$ticker==names(listsymbols[i])),6] <- insert_return_container(i, get_return(i)),
           warning = "Warning", 
           error = function(i){print(paste("Error"))})
}

# Insert Days since post
container <- container %>%
  mutate(ElapsedDays = as.Date(container$date, format="%Y/%m/%d")-as.Date(Sys.Date(), format="%Y/%m/%d"))

# Calculate annualized performance
container %>%
  mutate(arr = ((return)^(365/as.numeric(container$ElapsedDays))))
Re(as.complex(container[5,6])^(2/3))

for(i in 1:nrow(container)){
  if(is.na(container[i,6])){
  } else if(container[i,6] < 0){
    container[i,"arr"] <- sqrt((container$return[i]^2))^(365/as.numeric(container$ElapsedDays[i]))
  } else if(container[i,6] >= 0){
    container[i,"arr"] <- container$return[i]^2^(365/as.numeric(container$ElapsedDays[i]))
  }
}

# Annualized Returns
for(i in 1:nrow(container)){
  container$arr[i] <- annualized_return(i)
}



