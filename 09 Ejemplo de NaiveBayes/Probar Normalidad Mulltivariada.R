##########################################################################################
# Cargamos los datos de Iris
##########################################################################################

# Leemos los datos
datos_iris <- read.csv("iris.csv")

# Analisis descriptivo (univariado) de cada columna
par(mfrow=c(1,1)) # Con esto le decimos que queremos 2 graficas de fila x

variable <- datos_iris$Sepal_Length
hist( variable, breaks=50, probability=TRUE, col="#1CACDB", main="Sepal_Length")
curve(dnorm(x,mean(variable), sd(variable)), add=TRUE, col="red", lwd=3)
grid()                          # Agregamos una cuadricula
ks.test(x=variable,y="pnorm")   # Prueba Kolmogorov-Smirnov
shapiro.test(x=variable)        # Prueba Shapiro
qqnorm(variable)
variable <- datos_iris$Sepal_Width
hist( variable, breaks=50, probability=TRUE, col="#1CACDB", main="Sepal_Width")
curve(dnorm(x,mean(variable), sd(variable)), add=TRUE, col="red", lwd=3)
grid()                          # Agregamos una cuadricula
ks.test(x=variable,y="pnorm")   # Prueba Kolmogorov-Smirnov
shapiro.test(x=variable)        # Prueba Shapiro

variable <- datos_iris$Petal_Length
hist( variable, breaks=50, probability=TRUE, col="#1CACDB", main="Petal_Length")
curve(dnorm(x,mean(variable), sd(variable)), add=TRUE, col="red", lwd=3)
grid()                          # Agregamos una cuadricula
ks.test(x=variable,y="pnorm")   # Prueba Kolmogorov-Smirnov
shapiro.test(x=variable)        # Prueba Shapiro

variable <- datos_iris$Petal_Width
hist( variable, breaks=50, probability=TRUE, col="#1CACDB", main="Petal_Width")
curve(dnorm(x,mean(variable), sd(variable)), add=TRUE, col="red", lwd=3)
grid()                          # Agregamos una cuadricula
ks.test(x=variable,y="pnorm")   # Prueba Kolmogorov-Smirnov
shapiro.test(x=variable)        # Prueba Shapiro


##########################################################################################
# Utilizando la biblioteca 'MVN'
##########################################################################################

# Las siguientes funciones ya no son 'compatibles'
# MVN::hzTest(      datos_iris[,c(1,2,3,4)] )
# MVN::mardiaTest(  datos_iris[,c(1,2,3,4)] )
# MVN::roystonTest( datos_iris[,c(1,2,3,4)] )
par(mfrow=c(1,1))

MVN::mvn( data=datos_iris[,c(1,2,3,4)], mvnTest="hz",      desc=FALSE, multivariatePlot="qq")
MVN::mvn( data=datos_iris[,c(1,2,3,4)], mvnTest="mardia",  desc=FALSE, multivariatePlot="qq")
MVN::mvn( data=datos_iris[,c(1,2,3,4)], mvnTest="royston", desc=FALSE, multivariatePlot="qq")
