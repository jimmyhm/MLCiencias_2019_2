set.seed(13)
X = 1:100
Y = -15 + sqrt(2)*X + rnorm(100,0,8)
plot(1:100,Y, type="p")

data.table::fwrite( data.table::data.table( X = 1:100, Y = Y ), "datos_ajuste_1.csv" )

set.seed(13)
X = -30:30
Y = -15 + sqrt(2)*X - 0.2*X**2 + rnorm(61,0,12)
plot(-30:30,Y, type="p")

data.table::fwrite( data.table::data.table( X = -30:30, Y = Y ), "datos_ajuste_2.csv" )

set.seed(13)
X = 1:100
Y = 2 + 0.02*X + sqrt(2)*sin(2*pi*X/48) + sqrt(3)*cos(2*pi*X/48) + rnorm(100,0,1)
plot(1:100,Y, type="p")

data.table::fwrite( data.table::data.table( X = 1:100, Y = Y ), "datos_ajuste_3.csv" )

set.seed(13)
X = 1:100
Y = 12 + pi*X + 0.5*X*cos(2/3*X) + rnorm(100,0,12)
plot(1:100,Y, type="p")

data.table::fwrite( data.table::data.table( X = 1:100, Y = Y ), "datos_ajuste_4.csv" )


