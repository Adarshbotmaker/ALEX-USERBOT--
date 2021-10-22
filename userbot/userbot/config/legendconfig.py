import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", None)
    # This is required for the modules involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    LOGGER = True
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    TAG_LOG = os.environ.get("TAG_LOG", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1434332284").split())
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get("WHITELIST_USERS", "1311769691").split()
    )
    BLACKLIST_USERS = set(
        int(x) for x in os.environ.get("BLACKLIST_USERS", "1434332284").split()
    )
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1311769691").split())
    SUPPORT_USERS = set(
        int(x) for x in os.environ.get("SUPPORT_USERS", "1232461895").split()
    )
    BEST_USERS = set(int(x) for x in os.environ.get("BEST_USERS", "1754865180").split())
  
    ASSISTANT_START_PIC = os.environ.get(
        "ASSISTANT_START_PIC",
        "https://telegra.ph/file/63abc60224dc567e3d441.jpg",
    )
    TESSDATA_PREFIX = os.environ.get(
        "TESSDATA_PREFIX", "/usr/share/tesseract-ocr/4.00/tessdata"
    )
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    LEGEND_PRO = os.environ.get("LIGHTNING_PRO", "YES")
    ANTISPAM_FEATURE = os.environ.get("ANTISPAM_FEATURE", "ENABLE")
    ANTI_SPAMINC_TOKEN = os.environ.get("ANTI_SPAMINC_TOKEN", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    PMSECURITY = os.environ.get("PMSECURITY", "ON")
    # for autopic
    EMOJI_IN_HELP1 = os.environ.get("EMOJI_IN_HELP1", "🔱 ")
    EMOJI_IN_HELP2 = os.environ.get("EMOJI_IN_HELP2", "🔱 ")
    AUTOPIC_TEXT = os.environ.get(
        "AUTOPIC_TEXT", "Life Is too Short.\n And so is your TG account."
    )
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "DejaVuSans.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    if AUTH_TOKEN_DATA is not None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    UB_BLACK_LIST_CHAT = set(
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    )
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )

    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    BAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None)
    FBAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None)
    if FBAN_GROUP_ID:
        FBAN_GROUP_ID = int(FBAN_GROUP_ID)
    EXCLUDE_FED = os.environ.get("EXCLUDE_FED", None)


class Development(Config):
    LOGGER = True
