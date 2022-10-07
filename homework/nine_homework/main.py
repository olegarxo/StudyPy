from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd
from comand import *

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher



start_handler = CommandHandler('start', start_game)
del_abv = CommandHandler('del', take_text)   # /del (Удаляет слова, в которых есть буквы из списка)
bot_move = MessageHandler(Filters.text, bot_game)
gamer_move = MessageHandler(Filters.text, gamer)
end = CommandHandler('cancel', end_game)
Game = ConversationHandler(entry_points=[start_handler],
                           states={A: [gamer_move], B: [bot_move]},
                           fallbacks=[end])

# dispatcher.add_handler(start_handler)s
dispatcher.add_handler(del_abv)
# dispatcher.add_handler(bot_move)
# dispatcher.add_handler(gamer_move)
dispatcher.add_handler(Game)

updater.start_polling()
updater.idle()
