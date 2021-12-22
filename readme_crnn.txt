Para comprobar que la demo funcione correctamente se ejecutará:

python src/predict.py -h

En caso de que no surjan errores, se continuará.
Antes de ejecutarla, se inroducirán en la carpeta 'demo' las imagenes con el texto que se desee reconocer (ya hay algunas incluidas dentro).

Y, se continuará ejecutando dicha demo, con el comando:

python src/predict.py demo/<imagen.extensión>

En caso de querer reconocer el texto en más de una imagen al mismo tiempo, se podrá ejecutar un comando como los siguientes:

python src/predict.py demo/*.jpg
python src/predict.py demo/*.png

Para que se realice dicha operación con las imagenes con extensión jpg o png, respectivamente.
