from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess

TOKEN = "7626770291:AAG3UC1h3vt1aR9h0ALAgq3oo9RlvsMGSzI"
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

# НОВІ КОМАНДИ:
async def galxe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    await update.message.reply_text("Фарм Galxe запущено!")
    # Тут буде логіка для Galxe

async def layer3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    await update.message.reply_text("Фарм Layer3 запущено!")
    # Тут буде логіка для Layer3

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    await update.message.reply_text("Баланс: 0 USDT (фіктивно, API ще не підключено)")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("farm", farm))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("galxe", galxe))
app.add_handler(CommandHandler("layer3", layer3))
app.add_handler(CommandHandler("balance", balance))

app.run_polling()
