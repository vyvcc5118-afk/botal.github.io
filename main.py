from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI

BOT_TOKEN = "TOKEN_BOT"
OPENAI_KEY = "API_KEY"

client = OpenAI(api_key=OPENAI_KEY)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": text}
        ]
    )

    ai = response.choices[0].message.content

    await update.message.reply_text(ai)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot đang chạy...")
app.run_polling()
