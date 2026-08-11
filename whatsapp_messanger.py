import pywhatkit
from datetime import datetime, timedelta


def whatsapp_messenger_fun(caption):

    send_time = datetime.now() + timedelta(minutes=2)

    hour = send_time.hour
    minute = send_time.minute

    pywhatkit.sendwhatmsg(
        "Your_phone_number",
        caption,
        hour,
        minute
    )