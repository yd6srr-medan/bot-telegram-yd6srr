import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "GANTI_DENGAN_TOKEN_BOT_OM"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo Om YD6SRR! Bot Aktif! /cq /info")

async def cq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CQ CQ CQ de YD6SRR Medan, QRZ? 73!")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("YD6SRR Medan - Amateur Radio - 73!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Om bilang: {update.message.text}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cq", cq))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot YD6SRR Jalan Om!")
    app.run_polling()
