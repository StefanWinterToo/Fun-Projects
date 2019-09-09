library("rvest")
library("tidyverse")
library("stringr")
library("lubridate")

cobf <- read_html("http://www.cornerofberkshireandfairfax.ca/forum/investment-ideas/")

# Scrape Data -----
scrape.data <- function(maximum = 2030){
  
  date_raw <- lapply(paste0('http://www.cornerofberkshireandfairfax.ca/forum/index.php?thememode=mobile;redirect=http%3A%2F%2Fwww.cornerofberkshireandfairfax.ca%2Fforum%2Finvestment-ideas%2F', seq(from = 0, to = maximum, by = 15),"%2F"),
                     function(url){
                       url %>% read_html() %>%
                         html_nodes("a p") %>%
                         html_text() %>%
                         gsub("\\n", '', .) %>%
                         gsub("\\t", '', .) %>%
                         subset(!grepl("Last.*\\d", .)) %>%
                         gsub(".*?on ", "", .) %>%
                         dmy_hm(format = "%d/%m/%y %H:%M", tz = "") %>%
                         as.data.frame(stringsAsFactors=FALSE) %>%
                         filter(!is.na(.))
                     })
  
  
  
  ideas_raw <- lapply(paste0('http://www.cornerofberkshireandfairfax.ca/forum/investment-ideas/', seq(from = 0, to = maximum, by = 15)),
                      function(url){
                        url %>% read_html() %>%
                          html_nodes("span a") %>%
                          html_text() %>%
                          gsub("SMF 2.0.15", NA, .) %>%
                          gsub("SMF © 2017", NA, .) %>%
                          gsub("Simple Machines", NA, .) %>%
                          gsub("Simple Machines", NA, .) %>%
                          as.data.frame(stringsAsFactors=FALSE) %>%
                          filter(!is.na(.))
                      })
  
  # Multiple Pages Mobile
  user_raw <- lapply(paste0('http://www.cornerofberkshireandfairfax.ca/forum/investment-ideas/', seq(from = 0, to = maximum, by = 15)),
                     function(url){
                       url %>% read_html() %>%
                         html_nodes("p") %>%
                         html_text() %>%
                         gsub("\\n", '', .) %>%
                         gsub("\\t", '', .) %>%
                         gsub("Started by ", '', .) %>%
                         gsub("\\d", '', .) %>%
                         gsub("[[:space:]]", '', .) %>%
                         gsub("[[:punct:]]", '', .) %>%
                         gsub("[[:blank:]]", '', .) %>%
                         gsub("NormalTopicHotTopicMorethanrepliesVeryHotTopicMorethanreplies", NA, .) %>%
                         gsub("LockedTopicStickyTopicPoll", NA, .) %>%
                         as.data.frame(stringsAsFactors=FALSE) %>%
                         filter(!is.na(.)) %>%
                         filter(. != "")
                     })
  
  views_raw <- lapply(paste0('http://www.cornerofberkshireandfairfax.ca/forum/investment-ideas/', seq(from = 0, to = maximum, by = 15)),
                      function(url){
                        url %>% read_html() %>%
                          html_nodes("[class='stats windowbg']") %>%
                          html_text()%>%
                          gsub("\\n", '', .) %>%
                          gsub("\\t", '', .) %>%
                          gsub("*. Views", "", .) %>%
                          gsub(" .*", "", .) %>%
                          as.numeric() %>%
                          as.data.frame(stringsAsFactors=FALSE) %>%
                          filter(!is.na(.)) %>%
                          filter(. != "")
                      })
  
  
  # Clean Data #
  
  # Date
  date <- data.frame()
  
  for(i in 1:length(date_raw)){
    date <- rbind(date, date_raw[[i]])
  }
  colnames(date) <- "date"
  print(nrow(date))
  
  # User
  user <- data.frame()
  
  for(i in 1:length(user_raw)){
    user <- rbind(user, user_raw[[i]])
  }
  colnames(user) <- "user"
  print(nrow(user))
  
  # Ideas
  ideas <- data.frame(stringsAsFactors=FALSE)
  
  for(i in 1:length(ideas_raw)){
    ideas <- rbind(ideas, ideas_raw[[i]])
  }
  colnames(ideas) <- "stock"
  print(nrow(ideas))
  
  ideas <- separate(data = ideas, col = stock, into = c('ticker', 'name'), sep = '- ')
  ideas$ticker <- as.data.frame(gsub(x = ideas$ticker, "[[:space:]]", ''), stringsAsFactors=FALSE)
  colnames(ideas$ticker) <- "ticker"
  
  
  # Views
  views <- data.frame()
  
  for(i in 1:length(views_raw)){
    views <- rbind(views, views_raw[[i]])
  }
  views <- rbind(22,views)
  if(nrow(views)>2000){
    views[nrow(views)+1,] <- 0
  }
  
  print(nrow(views))
  colnames(views) <- "replies"
  print(nrow(views))
  
  # Combine
  container <- data.frame()
  container <- cbind(ideas, user, date, views)
  
  #print(container)
  return(container)
}
# Scrape Data End
