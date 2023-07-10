from tasmotta import on

from webex_bot.models.command import Command
import logging
import os
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)


class onCommand(Command):
    switch_name = ""
    password = ""

    def __init__(self, switch_name="", password=""):
        self.switch_name = switch_name
        self.password = password
        super().__init__(
            command_keyword="on",
            help_message="Enciende tu foco",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # AQUI DEBERIAMOS CONECTARNOS AL SERVIDOR DE MENSAJES
        # connect(os.getenv("MQTT_HOST"), os.getenv("MQTT_USER"), os.getenv("MQTT_PW"))
        # AQUI DEBERIAMOS PUBLICAR UN MENSAJE PARA PRENDER EL FOCO
        on(self.switch_name, self.password)
        # PODRIAMOS REGRESAR UN MENSAJE DE CONFIRMACION NO?
        return "encendi tu foco"
