# Calculate Return
get_return <- function(i){
  price1 <- listsymbols[[i]][as.Date(container[which(container$ticker == names(listsymbols[i])),"date"]),6]
  price2 <- listsymbols[[i]][which(index(listsymbols[[i]]) == max(index(listsymbols[[i]]))),6]
  erg <- (price2[[1]]-price1[[1]])/price1[[1]]
  return(erg)
}

# To enter returns at specific entry in data frame
insert_return_container <- function(i, returns = NA){
  return(returns)
}

annualized_return <- function(i){
  (1+container[i,6])^(365/(as.numeric(abs(container$ElapsedDays[i]))))-1
}
