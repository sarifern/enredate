import paho.mqtt.client
import paho.mqtt.publish


client = "unknown"


def on(name, password):
    try:
        topic = "cmnd/tasmota_" + name + "/POWER"
        # print(topic)
        global client
        paho.mqtt.publish.single(
            topic=topic,
            payload="ON",
            hostname="node02.myqtthub.com",
            port=1883,
            auth={"username": "stem_week_2023", "password": password},
        )

    #     client.publish(topic, "OFF")
    except Exception as ex:
        print("ERROR Tasmota: ", ex)


def off(name, password):
    try:
        topic = "cmnd/tasmota_" + name + "/POWER"
        # print(topic)
        global client
        paho.mqtt.publish.single(
            topic=topic,
            payload="OFF",
            hostname="node02.myqtthub.com",
            port=1883,
            auth={"username": "stem_week_2023", "password": password},
        )

    #     client.publish(topic, "OFF")
    except Exception as ex:
        print("ERROR Tasmota: ", ex)
