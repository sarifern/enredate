# STEM WEEK - Domótica con Webex

Este repositorio contiene el código para poder interactuar (encender/apagar) un switch inteligente Sonoff Basic con firmware Tasmota a través de un bot de Webex.

## Instalación

1. Clona este repositorio 

```bash 
git clone https://github.com/sarifern/enredate
```

2. Instala las librerías

```bash 
pip install -r requirements.txt
```

3. Crea un archivo llamado .env con el siguiente contenido. Pide el token y la contraseña a tu instructor

``` 
WEBEX_TOKEN=<pide el token a tu instructor!!!>
MQTT_HOST=node02.myqtthub.com
MQTT_USER=stem_week_2023
MQTT_PW=<pide la contraseña a tu instructor!!!>
```

4. En el archivo main.py, actualiza la variable de switch_name por la variable de tu switch. Si tienes dudas, pregunta a tu instructor.

![image](https://github.com/sarifern/enredate/assets/9137865/44d0b3e9-1693-42b2-9ba5-36215d80a69a)
 

## Usa el bot

1. Enciende el bot con el comando
``` bash
python main.py
```

2. Crea una conversacion con el email de tu bot, esto lo puedes ver cuando el bot inicia. Háblale!
Ejemplo
``` 
2023-07-04 13:54:11  [INFO]  [webex_bot.webex_bot.webex_bot.get_me_info]:90 Running as bot 'Botcito' with email [**'botcito_stem2@webex.bot'**]
``` 
![image](https://github.com/sarifern/enredate/assets/9137865/96037863-04d9-4c68-b91f-24e9670c5fd7)

3. Selecciona una de las opciones, verás como enciende o apaga tu foquito. Felicidades!

## Agradecimientos

Este workshop se logró con las siguientes librerias:

![Webex Bot](https://github.com/fbradyirl/webex_bot)
![Tasmota](https://github.com/robertdiers/solar-manager/blob/main/python/Tasmota.py)
