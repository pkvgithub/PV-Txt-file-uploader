import os

API_ID = API_ID = 24709391

API_HASH = os.environ.get("API_HASH", "cb1ba6bba27a3c68d219e5e34419cb5e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7148960116:AAHmmwTof2WIyKPPyV4oFZUIPYxeicBYYds")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1923238241))

LOG = -1001931388060,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1923238241").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


