import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("TOKEN")

# Храним этап пользователя
user_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_state[user_id] = 1

    await update.message.reply_text(
        "Ответь на пару вопросов)\n"
        "1: Ты любишь флаверса?"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.lower()

    state = user_state.get(user_id, 0)

    # ВОПРОС 1
    if state == 1:
        if text == "да":
            user_state[user_id] = 2
            await update.message.reply_text(
                "2: Наш любимый сериал?"
            )
        else:
            await update.message.reply_text(
                "Пасхалко, 67 хэй гёрл я лавки чмавки тебя). Нужен другой ответ"
            )

    # ВОПРОС 2
    elif state == 2:
        if text == "универ":
            user_state[user_id] = 3
            await update.message.reply_text(
                "3: Раз во сколько секунд я о тебе думаю?\n0.1 / 1 / 10"
            )
        else:
            await update.message.reply_text(
                "Либо попробуй по другому написать ответ, либо ты близко)"
            )

    # ВОПРОС 3
    elif state == 3:
        if text in ["0.1", "0,1"]:
            await update.message.reply_text(
                "Поздравляю! Обожаю тебя ❤️\n"
                "Вот тебе третья подсказка:\n"
                "Ключ спрятан там где мир отражается, "
                "там где ты готовишься сиять, "
                "там где свет копируется, "
                "там где правила зеркальны, "
                "но стоит лишь попробовать заглянуть за этот мир..."
            )
            user_state[user_id] = 0  # сброс
        elif text in ["1", "10"]:
            await update.message.reply_text(
                "Ты думаешь я могу позабыть на так долго такое счастье как ты?)"
            )
        else:
            await update.message.reply_text(
                "Выбери один из вариантов: 0.1 / 1 / 10"
            )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
