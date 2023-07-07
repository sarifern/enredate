from webex_bot.models.command import Command
import logging
import os
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)


class ejemploCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="",
            help_message="",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        pass
