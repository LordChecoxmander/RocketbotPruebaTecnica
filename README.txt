RocketbotPruebaTecnica

Instalacion del Entorno(en este caso utilizo virtualenv)

instalacion de virtual env
    python3 -m venv env
Alta y configuracion de virtual env con las librerias
    source env/bin/activate
    pip install openpyxl
    pip install selenium
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

En el ejercico de selenium con openpyxl:
    Challenge.py utilizando la libreria openpyxl abre el archivo xlsx, e itera sobre las filas del mismo verificando la columna J(estado). 
    En caso de "Atrasado" atrasado importa la funcion send_email() (del archivo complete_email.py), el mismo utiliza la API de gmail
    y en caso de "Regularizado" importala funcion charge_form() (del archivo complete_form.py), el mismo utiliza el webdriver de selenium para cargar los datos del fomulario

En el ejercico de los robots(el codigo se encuentra en la carpeta ROBOT) utilice 3 bots:
    El primer bot nombrado Challenge que abre el xlsx e itera sobre las filas verificando la columna de estado. En caso de "Atrasado" Challenge ejecuta el bot "hijo" nombrado send_email el cual envia un mail utilizndo el modulo de gmail. En caso de "Regularizado" ejecuta el bot "hijo" nombrado charge_form que carga los datos en el fomulario