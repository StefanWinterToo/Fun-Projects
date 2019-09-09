# Transform weekend to workday
transform_wday_op <- function(i){
  if(wday(container$date)[i] == 7){
    return(as.Date(container$date[i])+2)
  } else if(wday(container$date)[i] == 1){
    return(as.Date(container$date[i])+1)
  } else {
    return(as.Date(container$date[i]))
  }
}
