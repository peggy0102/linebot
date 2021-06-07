from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('7fuQKw2bGnSebFFtfz2lTfmL9hB5PLxsmc87BtCP3dXKpzYyM6qwKOwZZV2Vz/t/edk5LsjJciKifyAePhVGZgSI56mWIP7VJCAQ5b69mQE+1aNAc8oJnAsI7k4kVFt+r12C+v7R9s7wTD/vf+ccyAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66704e054c16243853d1ecafd3461c0b')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃了飽了嗎?'))


if __name__ == "__main__":
    app.run()