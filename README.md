# 📄 Word to PDF Telegram Bot

A simple and efficient Telegram bot that allows users to convert `.doc` or `.docx` Word files to `.pdf` format directly through chat.

## ✨ Features

- 📥 Accepts Word files (`.doc`, `.docx`)
- ⚙️ Converts them to high-quality PDF
- 📤 Sends back the PDF file instantly
- 🕹️ Easy to use via Telegram chat
- 🛡️ Safe: files are not stored permanently

## 🚀 How to Use

1. Open Telegram and search for your bot (e.g., `@Ts246_bot`)
2. Start a conversation with `/start`
3. Upload a `.doc` or `.docx` file
4. Wait a moment while it converts...
5. Get your `.pdf` file back!

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.8+
- A Telegram Bot Token from [BotFather](https://t.me/BotFather)
- `python-docx` and `reportlab` (or `docx2pdf` for Windows/Mac only)
- `python-telegram-bot` library

### Clone the repository

```bash
git clone https://github.com/yourusername/word-to-pdf-bot.git
cd word-to-pdf-bot


### Create a `.env` file:**
    ```
    BOT_TOKEN=your-telegram-bot-token
    ```

### Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ``
### Run locally (LibreOffice must be installed and in PATH):**
    ```bash
    python PDF_converted.py
    ```

## License

MIT

---

**Made with ❤️ using python-telegram-bot and LibreOffice**
