from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd
from comand import *

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher



start_handler = CommandHandler('start', start_game)
del_abv = CommandHandler('del', take_text)   # /del (Удаляет слова, в которых есть буквы из списка)
null = CommandHandler('null', Null_point)
points = CommandHandler('point', Show_point)
bot_move = MessageHandler(Filters.all, bot_game)
gamer_move = MessageHandler(Filters.all, gamer)
end = MessageHandler(Filters.all, end_game)
Game = ConversationHandler(entry_points=[start_handler],
                           states={A: [gamer_move], B: [bot_move]},
                           fallbacks=[end])


# dispatcher.add_handler(start_handler)s
dispatcher.add_handler(del_abv)
# dispatcher.add_handler(bot_move)
# dispatcher.add_handler(gamer_move)
dispatcher.add_handler(Game)
dispatcher.add_handler(null)
dispatcher.add_handler(points)
dispatcher.add_handler(end)

updater.start_polling()
updater.idle()
