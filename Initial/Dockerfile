# Usamos una imagen base de Ubuntu que es perfecta para compilar C/C++
FROM ubuntu:22.04

# Evitamos que nos pida confirmaciones manuales (como zonas horarias) durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalamos el compilador (build-essential) y gnuplot (para dibujar la gráfica del fractal)
RUN apt-get update && apt-get install -y \
    build-essential \
    gnuplot \
    && rm -rf /var/lib/apt/lists/*

# Establecemos nuestra carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos todos los archivos que ya tienes (main.cpp, Makefile, etc.) al contenedor
COPY . .

# Compilamos el programa usando el archivo Makefile que descargaste
RUN make

# El comando final: ejecuta el programa compilado y luego genera la imagen con gnuplot
CMD ./julia && gnuplot julia_set.gp && cp julia_set.png /resultado/