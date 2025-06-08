import os
# import imghdr
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# Set your bot token here
BOT_TOKEN = "7427418593:AAFAnstSz_rCylrcAguNlxe1tYmK10xwPvo"

# Folder to temporarily save files
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def convert_to_pdf(input_path):
    # Uses soffice (LibreOffice) to convert to PDF
    subprocess.run([
        "soffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", DOWNLOAD_FOLDER,
        input_path
    ], check=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me a Word (.docx) file to convert it to PDF.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Just upload a .docx file and I'll convert it to PDF.")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a Word to PDF bot created by J.A.R.V.I.S 😊")

async def handle_docx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document

    if not file.file_name.lower().endswith(".docx"):
        await update.message.reply_text("Please send a .docx file.")
        return

    await update.message.reply_text("Received your file. Converting to PDF...")

    file_path = os.path.join(DOWNLOAD_FOLDER, file.file_name)
    print(f"Downloading to: {file_path}")
    telegram_file = await file.get_file()
    await telegram_file.download_to_drive(file_path)

    try:
        convert_to_pdf(file_path)
        pdf_path = file_path.replace(".docx", ".pdf")
        print(f"Looking for PDF at: {pdf_path}")
        if not os.path.exists(pdf_path):
            print("PDF not found after conversion!")
            await update.message.reply_text("PDF conversion failed: file not found.")
            return
        with open(pdf_path, "rb") as pdf_file:
            await update.message.reply_document(document=pdf_file)
    except Exception as e:
        print(f"Exception: {e}")
        await update.message.reply_text(f"Failed to convert: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.Document.MimeType("application/vnd.openxmlformats-officedocument.wordprocessingml.document"), handle_docx))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()