library(xts)
library(dplyr)
library(ggplot2)

# Plot a series temporais do usuarios de interesse
for(device in unique(dataset$device_trip_id)){
    tsDevice = xts(x=dataset[dataset$device_trip_id==device,c("heading")], 
                  order.by = pull(dataset[dataset$device_trip_id==device,c("device_timestamp")],device_timestamp))
  print(plot(tsDevice, main = device))
  print(addEventLines(tsDevice, lty=2, on=1, offset=.4, pos=2, srt=90, cex=1.5, col="red") )
    
  tsPremio = xts(
    perregtotprem[
      perregtotprem$CodigoUsuario==device,c("Valor")],
    pull(perregtotprem[
      perregtotprem$CodigoUsuario==device,c("DataResultado","Valor")],
      DataResultado))
  
  print(addEventLines(tsPremio, lty=2, on=1, offset=.4, pos=2, srt=90, cex=1.5, col="red") )
  ggplot(data=dataset, aes(x=device_timestamp, y=device, color=device)) + geom_line()
}

filter1 = dataset$type %in% c("ACCELERATION", "DECELERATION", "START_TRIP","STOP_TRIP")

filter2 = dataset$device_trip_id!= 'xxxxxxxxxxxx'

ggplot(data=dataset[filter2,], aes(x=device_timestamp, y=device_trip_id, color=device_trip_id)) + 
  geom_line() + 
  geom_point(data = dataset[filter1 & filter2,],
             mapping=aes(x=device_timestamp, y=device_trip_id, shape=type, color = type), size=5)
