import slack_sdk
from datetime import datetime
from config import cfg

SLACK_TOKEN = cfg.SLACK.KEY
SLACK_CHANNEL = "#notion"
CLASSIFICATION = "N2T"

def slack_message(msg):
    client = slack_sdk.WebClient(token = SLACK_TOKEN)
    client.chat_postMessage(
        channel=SLACK_CHANNEL,
        text=msg
        )
    
def slack_message_with_time(msg):
    datetime_format = datetime.today().strftime("%Y-%m-%d %H:%M")
    client = slack_sdk.WebClient(token = SLACK_TOKEN)
    client.chat_postMessage(
        channel=SLACK_CHANNEL,
        text="["+datetime_format+"] " +"{}".format("["+CLASSIFICATION+"]" if CLASSIFICATION !="" else "")+ msg
        )

if __name__ == "__main__":
    datetime_format = datetime.today().strftime("%Y-%m-%d %H:%M")
    text = "slack 메세지 테스트"
    slack_message("["+datetime_format+"] "+text)