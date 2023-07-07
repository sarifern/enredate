from tasmotta import connect, on

from webex_bot.models.command import Command
import logging
import os
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)


class onCommand(Command):
    switch_name = ""

    def __init__(self, switch_name=""):
        self.switch_name = switch_name
        super().__init__(
            command_keyword="on",
            help_message="Enciende tu foco",
            card=None,
        )

    def pre_execute(self, message, attachment_actions, activity):
        """
        (optional function).
        Reply before running the execute function.

        Useful to indicate the bot is handling it if it is a long running task.

        :return: a string or Response object (or a list of either).
        Use Response if you want to return another card.
        """
        # AQUI DEBERIAMOS CONECTARNOS AL SERVIDOR DE MENSAJES

    def execute(self, message, attachment_actions, activity):
        # AQUI DEBERIAMOS PUBLICAR UN MENSAJE PARA PRENDER EL FOCO
        # PODRIAMOS REGRESAR UN MENSAJE DE CONFIRMACION NO?

 