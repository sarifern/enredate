import socket
from paho.mqtt import client as mqtt_client

client = "unknown"


def on(name):
    try:
        topic = "cmnd/tasmota_" + name + "/POWER"
        # print(topic)
        global client
        client.publish(topic, "ON")
    except Exception as ex:
        print("ERROR Tasmota: ", ex)


def off(name):
    try:
        topic = "cmnd/tasmota_" + name + "/POWER"
        # print(topic)
        global client
        client.publish(topic, "OFF")
    except Exception as ex:
        print("ERROR Tasmota: ", ex)


def connect(mqtt_broker, mqtt_port, mqtt_user, mqtt_password):
    try:
        client_id = "botmanager-tasmota-" + socket.gethostname()
        print(client_id)
        # Set Connecting Client ID
        global client
        client = mqtt_client.Client(client_id)
        client.username_pw_set(mqtt_user, mqtt_password)
        client.connect(mqtt_broker, mqtt_port)

    except Exception as ex:
        print("ERROR Tasmota: ", ex)
