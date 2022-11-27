from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

from reply import *


app = Flask(__name__)

line_bot_api = LineBotApi('cI59LiOWPAA/UAqPrpBNk5+OOUUn9jwuzZ2n0xDaoJcx/NYZUD5DDXREs/u6aXc7nJqOqsp6ahnG6UKVCh0AgcQ60/IP8+VEhyksP3E3VcKZ5b9KGC5sDcf8RY6yFY48cdG1hE3Fg3vfd3dZJ+37FQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6ab7589625caf81134de8f0182a29610')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    msg = msg.lower()

    if 'sorry' in msg:
        sticker_message = StickerSendMessage(
            package_id = '446',
            sticker_id = '2016'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    elif 'thank you' in msg:
        sticker_message = StickerSendMessage(
            package_id = '11538',
            sticker_id = '51626496'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    elif msg in ['hi', 'hey', 'hello', 'greetings', 'wassup']:
        r = Reply(msg)
        message = r.greeting_response()

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

    elif msg in ['exit', 'see you', 'bye', 'quit', 'break']:
        message = "Chat with you later !"

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

    elif msg in ['problem', 'question']:
        r = Reply(msg)
        message = r.problem()

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

    elif msg == '':
        message = "Please type something so we can chat :("

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

    else:
        r = Reply(msg)
        message = r.random_response()

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

   

    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))


if __name__ == "__main__":
    app.run()