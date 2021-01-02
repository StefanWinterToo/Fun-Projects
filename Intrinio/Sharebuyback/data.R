load_data <- function(stock, tag_id){
  client <- IntrinioSDK::ApiClient$new()
  
  # Configure API key authorization: ApiKeyAuth
  client$configuration$apiKey <- "OjU3N2JhMWI0YTM0MjEzNTZjNDEwNjI0ZGNkOTQ3MGQz"
  
  # Setup API with client
  CompanyApi <- IntrinioSDK::CompanyApi$new(client)
  
  # Required params
  identifier <- stock # Character | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
  tag <- tag_id # Character | An Intrinio data tag ID or code reference [see - https://data.intrinio.com/data-tags]
  
  # Optional params
  opts <- list(
    frequency = "yearly", # Character | Return historical data in the given frequency
    type = NULL, # Character | Return historical data for given fiscal period type
    start_date = as.Date("2008-01-01"), # Date | Return historical data on or after this date
    end_date = NULL, # Date | Return historical data on or before this date
    sort_order = "desc", # Character | Sort by date `asc` or `desc`
    page_size = 100, # Integer | The number of results to return
    next_page = NULL # Character | Gets the next page of data from a previous API call
  )
  
  response <- CompanyApi$get_company_historical_data(identifier, tag, opts)
  
  response$content$historical_data_data_frame
}

