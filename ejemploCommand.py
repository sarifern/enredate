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

    def pre_execute(self, message, attachment_actions, activity):
        """
        (optional function).
        Reply before running the execute function.

        Useful to indicate the bot is handling it if it is a long running task.

        :return: a string or Response object (or a list of either).
        Use Response if you want to return another card.
        """
        pass

    def execute(self, message, attachment_actions, activity):
        pass
