import os

API_ID = API_ID = 28828325

API_HASH = os.environ.get("API_HASH", "8d51af51dcf293bb94c20f7f22988412")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5524982791:AAFhzOROCDty0VS4C5W-1T8kF355eY1vHx8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5116782991))

LOG = -1001976032350,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5116782991").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


