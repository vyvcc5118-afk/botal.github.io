from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI
import os

BOT_TOKEN = os.getenv("8948614500:AAEAmVQDqCGl66KG4vo4pCdqkNA5ARWD_xk")
OPENAI_API_KEY = os.getenv("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")

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
