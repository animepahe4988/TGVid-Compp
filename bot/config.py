#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-preset veryfast -c:v libx264 -s 854x480 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Anime Sensei' -metadata:s:v 'title=Anime Sensei' -metadata:s:a 'title=Anime Sensei' -metadata:s:s 'title=Anime Sensei -pix_fmt yuv420p -crf 28 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5"]
    THUMBNAIL = config("THUMBNAIL", default="https://te.legra.ph/file/86e958f9fc0d7cbdf1a28.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
