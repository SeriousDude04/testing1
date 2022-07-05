import os 
from telegram.ext import * 
import response as R

print("Bot Started")

def start_command(update , context):
  update.message.reply_text("Hello")
def help_command(update , context):
  update.message.reply_text("No help")
def otp_command(update , context):
  update.message.reply_text("Checking for Otp")
  response = R.sample_response()
  update.message.reply_text(response,parse_mode = "MarkdownV2")
def error(update , context):
  update.message.reply_text("error try again")
def main():
  updater = Updater(os.environ['api_key'] , use_context = True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("otp", otp_command))
  dp.add_error_handler(error)
  updater.start_polling()
  updater.idle()

main()