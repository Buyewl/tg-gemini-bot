# bot.py

import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Ganti dengan token bot Telegram Anda yang sebenarnya.
# Disarankan untuk menggunakan variabel lingkungan atau GitHub Secrets.
# Contoh: TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE" # Ganti ini dengan token Anda!

# Fungsi untuk menangani perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mengirim pesan sambutan saat perintah /start diterima."""
    await update.message.reply_text(f'Halo {update.effective_user.first_name}! Saya adalah bot Gemini Anda.')

# Fungsi untuk menangani pesan teks
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mengulang kembali pesan teks yang diterima."""
    # Anda akan mengintegrasikan API Gemini di sini
    await update.message.reply_text(update.message.text)

# Fungsi utama untuk menjalankan bot
def main() -> None:
    """Menjalankan bot."""
    # Buat instance Application dan berikan token bot Anda
    application = Application.builder().token(TOKEN).build()

    # Tambahkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    # Tambahkan handler untuk semua pesan teks
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Jalankan bot sampai Ctrl-C ditekan
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()