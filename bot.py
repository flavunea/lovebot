import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "Вот тебе третья подсказка: "
        "Ключ спрятан там где мир отражается, "
        "там где ты готовишься сиять, "
        "там где свет копируется, "
        "там где правила зеркальны, "
        "но стоит лишь попробовать заглянуть за этот мир..."
    )
    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()