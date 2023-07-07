from tasmotta import connect, off

from webex_bot.models.command import Command
import logging
import os
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)


class offCommand(Command):
    switch_name = ""

    def __init__(self, switch_name=""):
        self.switch_name = switch_name
        super().__init__(
            command_keyword="off",
            help_message="Apaga tu foco",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        # AQUI DEBERIAMOS CONECTARNOS AL SERVIDOR DE MENSAJES
        # AQUI DEBERIAMOS PUBLICAR UN MENSAJE PARA APAGAR EL FOCO
        # PODRIAMOS REGRESAR UN MENSAJE DE CONFIRMACION NO?
