from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import logging
import os

# استخدم توكن البوت الخاص بك هنا أو من متغيرات البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN", "8511109903:AAGbRv53WwyoerY4-0v-gmObGXQvJYRYNdU")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🎉 مرحباً {update.effective_user.first_name}!\n"
        "بوت تيليجرام يعمل بنجاح 🚀"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 أوامر:\n"
        "/start - بدء البوت\n"
        "/help - المساعدة\n"
        "/ping - فحص حالة البوت"
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 البوت شغال تمام!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))

    logger.info("🚀 البوت شغال الآن!")
    app.run_polling()

if __name__ == "__main__":
    main()
