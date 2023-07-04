from onCommand import onCommand
from offCommand import offCommand
from webex_bot.webex_bot import WebexBot
import os
from dotenv import load_dotenv

load_dotenv()
# Create a Bot Object
bot = WebexBot(
    teams_bot_token=os.getenv("WEBEX_TOKEN"),
    bot_name="STEM WEEK BOT",
    # include_demo_commands=False,
)

# Add new commands for the bot to listen out for.
bot.add_command(onCommand(switch_name="5BA7B3"))
bot.add_command(offCommand(switch_name="5BA7B3"))

# Call `run` for the bot to wait for incoming messages.
bot.run()
