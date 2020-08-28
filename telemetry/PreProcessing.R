require(Hmisc)
library(readr)

dataset <- read_csv("device_logs-3-2.csv", 
                          col_types = cols(created = col_datetime(format = "%Y-%m-%d %H:%M:%S"), 
                                           device_timestamp = col_datetime(format = "%Y-%m-%d %H:%M:%S"), 
                                           uid = col_character()))

dataset$id = as.factor(dataset$id)
dataset$device_trip_id = as.factor(dataset$device_trip_id)
dataset$uid = as.factor(dataset$uid)
dataset$type = as.factor(dataset$type)
dataset$battery = as.factor(dataset$battery)
dataset$sdk = as.factor(dataset$sdk)
