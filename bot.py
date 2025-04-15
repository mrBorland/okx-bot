
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess
import time
import requests
import hmac
import hashlib
import base64
from datetime import datetime

TOKEN = "7626770291:AAG3UC1h3vt1aR9h0ALAqg3oo9RlvsMGSzI"
ALLOWED_CHAT_ID = 6821675571

API_KEY = "8ce4bd62-9328-495e-9556-2bf1107b3ac2"
SECRET_KEY = "AB2C36344430A6080F3C5645155074B3"
PASSPHRASE = "Slipknot221989@"
BASE_URL = "https://www.okx.com"

def sign_okx(timestamp, method, request_path, body, secret_key):
    message = f"{timestamp}{method}{request_path}{body}"
    mac = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256)
    return base64.b64encode(mac.digest()).decode()

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

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    try:
        timestamp = datetime.utcnow().isoformat("T", "seconds") + "Z"
        method = "GET"
        path = "/api/v5/account/balance"
        body = ""
        signature = sign_okx(timestamp, method, path, body, SECRET_KEY)

        headers = {
            "OK-ACCESS-KEY": API_KEY,
            "OK-ACCESS-SIGN": signature,
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": PASSPHRASE,
            "Content-Type": "application/json"
        }

        resp = requests.get(BASE_URL + path, headers=headers)
        data = resp.json()
        usdt = next((x for x in data['data'][0]['details'] if x['ccy'] == 'USDT'), None)
        balance = usdt['cashBal'] if usdt else "0.0"
        await update.message.reply_text(f"Баланс USDT: {balance}")
    except Exception as e:
        await update.message.reply_text(f"Помилка отримання балансу: {e}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("farm", farm))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("balance", balance))
app.run_polling()
