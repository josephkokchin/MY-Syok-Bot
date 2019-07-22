##
 # @author Joseph Goh
 # @email [joseph.kokchin.goh@outlook.com]
 # @create date 2019-07-20 15:09:24
 # @modify date 2019-07-20 15:09:24
 # @desc [The following code will extract the 4D Results]
 #/

 # Import Libraries
import os
import logging
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job, CallbackQueryHandler, RegexHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from emoji import emojize  # emojize(random.choice(text_bot), use_aliases=True)
from functools import wraps
from time import sleep
import datetime
from credentials import *
import draw
import petrol

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def magnum4dresults(update,context):
    """ Send results from 4D """
    context.bot.sendChatAction(update.message.chat_id, action=ChatAction.TYPING)
    final_string = draw.Magnum4D()
    context.bot.sendMessage(update.message.chat_id,
                    text=final_string, parse_mode='HTML')

def totoresults(update,context):
    """ Send results from TOTO """
    context.bot.sendChatAction(update.message.chat_id, action=ChatAction.TYPING)
    final_string = draw.TOTO4D()
    context.bot.sendMessage(update.message.chat_id,
                    text=final_string, parse_mode='HTML')

def petrolprice(update,context):
    """ Send results from TOTO """
    context.bot.sendChatAction(update.message.chat_id, action=ChatAction.TYPING)
    final_string = petrol.PetrolPrice()
    context.bot.sendMessage(update.message.chat_id,
                    text=final_string, parse_mode='HTML')


def start(update, context):
    """ Start Text """

    context.bot.sendMessage(update.message.chat_id,
                    text='''Hello {}! I am @MY_AutoBot!
                     \nThe helpful Malaysian bot!
                     \nAvailable Commands
                     \n/share - Easily Share Shiokbot!
                     \n/weather - Report the latest weather lah
                     \n/myr - Latest MYR Rates!
                     \n/petrol - Latest Petrol Prices!
                     \n/magnum4d - Give you latest 4D results wor
                     \n/toto - Give you latest toto results huat ar!
                     '''.format(update.message.from_user.first_name))


def help(update,context):
    """ Help Text"""
    context.bot.sendMessage(update.message.chat_id,
                    text='''Hello {}! I am @MY_AutoBot!
                     \nThe helpful Malaysian bot!
                     \nAvailable Commands
                     \n/share - Easily Share Shiokbot!
                     \n/weather - Report the latest weather lah
                     \n/myr - Latest MYR Rates!
                     \n/petrol - Latest Petrol Prices!
                     \n/magnum4d - Give you latest 4D results wor
                     \n/toto - Give you latest toto results huat ar!
                     '''.format(update.message.from_user.first_name))


def share(update, context):
    """ Share Text"""

    share_text = """
                 MYAutoBot thanks you for sharing the love
                 \nSend this link to your friends to start using!
                 """
    share_link= """
                <a href="https://t.me/MY_AutoBot?start">https://t.me/MY_AutoBot?start</a>
                """
    context.bot.sendMessage(update.message.chat_id,
                    text=share_text, parse_mode='HTML')
    context.bot.sendMessage(update.message.chat_id,
                    text=share_link, parse_mode='HTML')
    # bot.sendMessage(update.message.chat_id,
    #                text=version_text, parse_mode='HTML')

def error(bot, update, error):
    """ Log Errors"""
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def main():
    """ This is where the bot starts from! """

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=telegram_token,use_context=True)
    #j = updater.job_queue

    # Get the dispatcher to register handlers
    dispatch = updater.dispatcher

    # on different commands - answer in Telegram
    dispatch.add_handler(CommandHandler("start", start))
    dispatch.add_handler(CommandHandler("help", help))
    #dispatch.add_handler(CommandHandler("psi", psi3hour))
    #dispatch.add_handler(CommandHandler("weather", weathernow))
    dispatch.add_handler(CommandHandler("magnum4d", magnum4dresults))
    dispatch.add_handler(CommandHandler("toto", totoresults))
    dispatch.add_handler(CommandHandler("petrol", petrolprice))
    #dispatch.add_handler(CommandHandler("ridepromos", taxipromos2))
    #dispatch.add_handler(CommandHandler("airlinepromos", airline_promos))
    #dispatch.add_handler(CommandHandler("deliverypromos", deliverypromos))
    #dispatch.add_handler(CommandHandler("shoppingpromos", shopping_promos))
    #dispatch.add_handler(CommandHandler("train_timing_changes", train_timing_changes))
    #dispatch.add_handler(CommandHandler("sg_news", get_news_st))
    #dispatch.add_handler(CommandHandler("traffic", traffic, pass_args=True))
    # dispatch.add_handler(CommandHandler("sti", sti_level))
    #dispatch.add_handler(CommandHandler("myr", myr_level))
    #dispatch.add_handler(CommandHandler("hotel_promos", hotel_promos))
    #dispatch.add_handler(CommandHandler("sibor", sibor_level))
    #dispatch.add_handler(CommandHandler("taxi_near_me", taxi_around_me))
    #dispatch.add_handler(CommandHandler("subscribe", subscribe))
    #dispatch.add_handler(CommandHandler("unsubscribe", unsubscribe))
    #dispatch.add_handler(CommandHandler("subscribe_train", subscribe_train))
    #dispatch.add_handler(CommandHandler("unsubscribe_train", unsubscribe_train))
    #dispatch.add_handler(CommandHandler("admin_force_promo_check", force_promo_check))
    #dispatch.add_handler(CommandHandler("admin_clear_db", clear_db))
    #dispatch.add_handler(CommandHandler("admin_list_users", list_users))
    #dispatch.add_handler(CommandHandler("admin_push_notification_promo", push_notification_promo, pass_args=True))
    #dispatch.add_handler(CommandHandler("admin_push_notification_msg", push_notification_msg, pass_args=True))
    dispatch.add_handler(CommandHandler("share", share))
    #dispatch.add_handler(CommandHandler("secret_sauce", secret_sauce))
    #dispatch.add_handler(CommandHandler("admin_list_users_train", list_users_train))
    #dispatch.add_handler(MessageHandler(Filters.location, taxi_around_me))
    #dispatch.add_handler(CallbackQueryHandler(call_handler))

    # create jobs
    # job_minute = Job(monitor_promo, 900)
    # j.put(job_minute, next_t=60)

    # Uber Discontinued
    #j.run_repeating(monitor_promo, 600, 15)
    #j.run_repeating(monitor_train, 300, 60)

    # log all errors
    #dispatch.add_error_handler(error)

    updater.start_polling()
    # Start the Bot
    """
    #DEV
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    """

    # PROD
    #port_number = int(os.environ.get('PORT', '5000'))
    #updater.start_webhook(listen="0.0.0.0",
    #                      port=port_number,
    #                      url_path=telegram)
    #updater.bot.setWebhook("https://shiokbot.herokuapp.com/" + telegram)
    #updater.idle()


if __name__ == '__main__':
    main()
