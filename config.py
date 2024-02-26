import os

API_ID = API_ID = 27803618

API_HASH = os.environ.get("API_HASH", "2cdaef9643189f6bd9c7b31a70257356")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6947816816:AAGTwQcuxuQxPFKEhSW_IQRoJ8D9Sr05AoI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 745084259))

LOG = -1002085617089,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "745084259").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


