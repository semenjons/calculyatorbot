from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"/Сумма - /plus число\n/разница - /minus число\n/умножение - /mult число \n/Деление - /div число\n/Комплексное сложение - /comp комплексное число")


async def addition(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} + {num2} = {float(num1) + float(num2)}')


async def subtraction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} - {num2} = {float(num1) - float(num2)}')


async def multiplication(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} * {num2} = {float(num1) * float(num2)}')


async def division(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    num1 = msg_split[1]
    num2 = msg_split[2]
    await update.message.reply_text(f'{num1} / {num2} = {float(float(num1) / float(num2))}')


async def compl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_split = update.message.text.split(" ")
    print(msg_split)
    num1 = msg_split[1]
    num2 = complex(msg_split[2])
    await update.message.reply_text(f'{num1} + {num2} = {abs((float(num1) + num2))}')
