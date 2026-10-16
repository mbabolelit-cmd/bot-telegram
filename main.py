import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Halo bos {update.effective_user.first_name}! Bot udah jalan! 🔥")

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("Bot running...")
    app.run_polling()
