from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": text}
        ]
    )

    reply = response.choices[0].message.content

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot đang chạy...")

app.run_polling()
