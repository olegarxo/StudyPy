from turtle import update
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint as rd


def som_comand(update, context):
    context.bot.send_message(update.effective_chat.id, 'Я таких команд не знаю')





def take_text(update, context):
    lang = ['а', 'б', 'в']
    text = update.message.text.split(' ')
    tamp = -1
    for i in text:
        tamp += 1
        count = 0
        for j in i:
            if str(j) in lang:
                count += 1
            if count == 3:
                text[tamp] = ''
    text = list(filter(lambda a: a != '' and a != '/del', text))
    context.bot.send_message(update.effective_chat.id, ' '.join(text))


A = 0
B = 1
C = 2
global snack
snack = 100
global count_win_bot
global count_win_user 
count_win_bot = 0
count_win_user = 0


def start_game(update, context):
    global snack
    snack = 100
    context.bot.send_message(update.effective_chat.id, 'Привет, ну что ж, сыграем)')
    random_number = rd(0, 1)
    if random_number == 0:
        context.bot.send_message(update.effective_chat.id, 'Первым ходит бот)')
        return B
    else:
        context.bot.send_message(update.effective_chat.id, 'Ты первый)')
        return A


def bot_game(update, context):
    global snack
    global count_win_user 
    global count_win_bot
    if snack // 28 > 1:
        take = rd(10, 29)
    elif 0 < snack < 29:
        take = snack
        count_win_bot += 1
        context.bot.send_message(update.effective_chat.id, f'Победил БОТ\nОчки бота:{count_win_bot}\n{update.effective_user.first_name}, вот твои очки:{count_win_user}')
        return ConversationHandler.END
    elif snack < 100:
        take = rd(5, 12)
    else:
        take = snack % 28
    context.bot.send_message(update.effective_chat.id, f'Я беру {take} конфет\nОсталось {snack - take})')
    snack -= take
    return A

def gamer(update, context):
    global snack
    global count_win_user 
    global count_win_bot
    flag = True
    while flag:
        text = update.message.text
        if 0 < int(text) < 29:
            snack -= int(text)
            context.bot.send_message(update.effective_chat.id, f'Осталось {snack} конфет')
            flag = False
        else:  # Впадает в цикл
            context.bot.send_message(update.effective_chat.id, 'Неправильное число, попробуйте еще раз')
    if snack == 0:
        count_win_user += 1
        context.bot.send_message(update.effective_chat.id, f'Победил ТЫ\nОчки бота:{count_win_bot}\n{update.effective_user.first_name}, вот твои очки:{count_win_user}')
        return ConversationHandler.END
    return B


def end_game(update, context):
    global snack
    context.bot.send_message(update.effective_chat.id, 'Победил ')
    snack = 300
def Show_point(update, context):
    context.bot.send_message(update.effective_chat.id, f'Очки бота:{count_win_bot}\nТвои очки:{count_win_user}')
def Null_point(update, context):
    global count_win_bot
    global count_win_user 
    (count_win_bot, count_win_user) = (0, 0) 
