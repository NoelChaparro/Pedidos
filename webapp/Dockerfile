FROM python:3.8

#Var de entorno para definir el ambiente
ARG DJANGO_ENV

#Error standard lo muestre en consola
ENV PYTHONUNBUFFERED=1
#Var entorno directorio de la pedidos
ENV WEBAPP_DIR=/webapp

#Cuando crea el contenedor va a crear una carpeta en raiz llamada webapp
RUN mkdir $WEBAPP_DIR

#Directorio de trabajo
WORKDIR $WEBAPP_DIR

#Copiarlo y pegarlo dentro de la carpeta de trabajo el archivo requierements.txt
ADD requirements/base.txt $WEBAPP_DIR/
ADD requirements/$DJANGO_ENV.txt $WEBAPP_DIR/

#Instalar las app en requirements
RUN pip install -r $DJANGO_ENV.txt
#Copiar todo dentro de la carpeta de WEBAPP
ADD . $WEBAPP_DIR/