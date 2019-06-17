MODELO_AR = forecast::auto.arima(y = AirPassengers, max.q = 0, max.d = 0, max.Q = 0, max.D = 0)
MODELO_AR
plot( forecast::forecast(MODELO_AR) )


arima(x = AirPassengers, order = c(12,0,0) )
