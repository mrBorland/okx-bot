from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess

TOKEN = "ТВОЙ_ТОКЕН"
ALLOWED_CHAT_ID = 6821675571

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    await update.message.reply_text("OKXFarmBot: Привіт, Тоні! Я готовий до команд.")

async def farm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    subprocess.Popen(["python3", "main.py"])
    await update.message.reply_text("Фарм запущено!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    await update.message.reply_text("Бот працює, все добре!")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    await update.message.reply_text("Виведення буде реалізовано найближчим часом.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("farm", farm))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("withdraw", withdraw))
app.run_polling()
