from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os
import scrape

ACCESS_TOKEN = os.environ['ENV_ACCESS_TOKEN']
USER_ID = os.environ['ENV_USER_ID']

line_bot_api = LineBotApi(ACCESS_TOKEN)

result = scrape.getNews("浦和")

try:
    line_bot_api.push_message(USER_ID, TextSendMessage(text=result))
    print ("成功です")
except LineBotApiError as e:
    print ("エラーです")
