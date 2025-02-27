import os


class Config:
    API_ID = int(os.environ.get("API_ID", 20187096))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", "eddbf671894e0729a62339079fef44b2")  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8060028176:AAEdQYX8GAmJA_KSLjLC_KWhg8Mxfbxhn1c")  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 1434595544))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", "ᴛᴇᴀᴍx")  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
