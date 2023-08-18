import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def start(update, context):
    update.message.reply_text(
        "Hello Welcome to Sad Sad Bot. where we take away your sadness")


def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome Message
    /help -> This Message
    /content -> Information about Happiness and Passion
    /contact -> Our contact information for personal outreach
    """)


def content(update, context):
    update.message.reply_text(
        "We have alot of videos, Audios, Trained experts to help you overcome sadness and pull you into the world of hapiness")


def contact(update, context):
    update.message.reply_text(
        "You can contact us on our Discord Server, YouTube, Facebook, Twitter and Messenger if you have any questions, suggestions and donations")


def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(
        f"The current price of {ticker} is {price:.2f}$!")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text} right?")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_message))

updater.start_polling()
print("Telegram Bot connected")
updater.idle()
