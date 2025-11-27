from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import logging
import os

# الإعدادات
BOT_TOKEN = os.getenv("BOT_TOKEN", "8511109903:AAGbRv53WwyoerY4-0v-gmObGXQvJYRYNdU")
OWNER_ID = int(os.getenv("OWNER_ID", "5056045687"))

# السجلات
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# الأوامر
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["👥 الجلسات", "📋 المهام"],
        ["📊 الإحصائيات", "ℹ️ المساعدة"]
    ]
    
    await update.message.reply_text(
        f"🎉 مرحباً {update.effective_user.first_name}!\n\n"
        "🤖 بوت إرسال البطاقات الاحترافي\n\n"
        "✅ البوت يعمل بنجاح!\n"
        "📱 استخدم الأزرار بالأسفل 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📚 **الأوامر المتاحة:**

/start - بدء البوت
/help - المساعدة
/ping - فحص البوت
/stats - الإحصائيات

🔧 للدعم: @YourSupport
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 البوت يعمل بشكل ممتاز!")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 **الإحصائيات:**\n\n"
        "👥 المستخدمين: 1\n"
        "📋 المهام: 0\n"
        "✅ المرسل: 0\n"
        "⏱️ وقت التشغيل: متصل",
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "👥 الجلسات":
        await update.message.reply_text("👥 قريباً: إدارة الجلسات")
    elif text == "📋 المهام":
        await update.message.reply_text("📋 قريباً: إدارة المهام")
    elif text == "📊 الإحصائيات":
        await stats(update, context)
    elif text == "ℹ️ المساعدة":
        await help_command(update, context)

def main():
    # إنشاء التطبيق
    app = Application.builder().token(BOT_TOKEN).build()
    
    # إضافة المعالجات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # تشغيل البوت
    logger.info("🚀 البوت يعمل الآن...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
