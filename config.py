from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "5833550185:AAFzUdwF-uiFxIVwzrVS7VepS5GH9tfv0Bk"
    SUDOERS = [5468192421]
    NSFW_LOG_CHANNEL = -1001860694129
    SPAM_LOG_CHANNEL = -1001860694129
    ARQ_API_KEY = "BPMYFT-AUMITY-DNXRMZ-JQOSFB-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
