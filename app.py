from flask import Flask,request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import( InvalidSignatureError )
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage)

app = Flask(__name__)

ACCESS_TOKEN = ""
SECRET = ""
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback",methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app_logger.info("Requestbody: " + body)
    try: handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return'OK'

    @handler.add(MessageEvent,message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://2.blogspot.com/-L_5LpgaI7PM/XAnv87aLv0I/AAAAAAABQtA/e44wVuaan6YsaXcXLltGfifPWX2Bc9aHQCLcBGAs/s400/nigaoe_lovecraft.png', preview_image_url='https://2.bp.blogspot.com/-L_5LpgaI7PM/XAnv87aLv0I/AAAAAAABQtA/e44wVuaan6YsaXcXLltGfifPWX2Bc9aHQCLcBGAs/s400/nigaoe_lovecraft.png'))
