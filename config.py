import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28225332"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a1f0f3dc497eb2bdd545f0be9fc2ef4d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://amanthambani:uxDfKIsZeaTDCyOR@cluster0.18zsm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
