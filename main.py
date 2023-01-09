
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import *




app = ApplicationBuilder().token("5960077643:AAFqad48rpy-XXS9h0AeTmg5zhzTYUC0Sj0").build()
print('сервер запущен')
app.add_handler(CommandHandler("plus", addition))
app.add_handler(CommandHandler("minus", subtraction))
app.add_handler(CommandHandler("mult", multiplication))
app.add_handler(CommandHandler("div", division))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("comp", compl))
app.run_polling()
