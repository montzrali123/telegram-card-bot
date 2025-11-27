import logging
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from telegram.constants import ParseMode

# إعداد السجلات
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# متغيرات البيئة (يجب ضبط BOT_TOKEN في البيئة)
BOT_TOKEN = os.getenv("8511109903:AAGbRv53WwyoerY4-0v-gmObGXQvJYRYNdU")
OWNER_ID = int(os.getenv("OWNER_ID", "5056045687"))

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN غير مضبوط في متغيرات البيئة. من فضلك أضف BOT_TOKEN وأعد التشغيل."
    )

# الأوامر
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["👥 الجلسات", "📋 المهام"],
        ["📊 الإحصائيات", "ℹ️ المساعدة"],
    ]
    await update.message.reply_text(
        f"🎉 مرحباً {update.effective_user.first_name}!\n\n"
        "🤖 بوت إرسال البطاقات الاحترافي\n\n"
        "✅ البوت يعمل بنجاح!\n"
        "📱 استخدم الأزرار بالأسفل 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "📚 الأوامر المتاحة:\n\n"
        "/start - بدء البوت\n"
        "/help - المساعدة\n"
        "/ping - فحص البوت\n"
        "/stats - الإحصائيات\n\n"
        "🔧 للدعم: @YourSupport"
    )
    await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🟢 البوت يعمل بشكل ممتاز!")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📊 الإحصائيات:\n\n"
        "👥 المستخدمين: 1\n"
        "📋 المهام: 0\n"
        "✅ المرسل: 0\n"
        "⏱️ وقت التشغيل: متصل",
        parse_mode=ParseMode.MARKDOWN,
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    if text == "👥 الجلسات":
        await update.message.reply_text("👥 قريباً: إدارة الجلسات")
    elif text == "📋 المهام":
        await update.message.reply_text("📋 قريباً: إدارة المهام")
    elif text == "📊 الإحصائيات":
        await stats(update, context)
    elif text == "ℹ️ المساعدة":
        await help_command(update, context)
    else:
        await update.message.reply_text("ℹ️ استخدم الأزرار أو اكتب /help لعرض الأوامر.")

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("❓ أمر غير معروف. اكتب /help لعرض الأوامر المتاحة.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    # تسجيل الخطأ لتسهيل تتبعه
    logger.exception("حدث خطأ غير متوقع:", exc_info=context.error)
    # إعلام المستخدم بطريقة لطيفة (إن وجد message)
    try:
        if isinstance(update, Update) and update.effective_message:
            await update.effective_message.reply_text("⚠️ حدث خطأ غير متوقع. حاول لاحقاً.")
    except Exception:
        pass  # تجنب كسر حلقة المعالجة داخل error handler

def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    # معالجات الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("stats", stats))

    # الرسائل النصية
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # أوامر غير معروفة
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # معالج الأخطاء
    app.add_error_handler(error_handler)

    logger.info("🚀 البوت يعمل الآن...")
    app.run_polling()  # لا نحتاج لتحديد allowed_updates يدوياً

if __name__ == "__main__":
    main()
