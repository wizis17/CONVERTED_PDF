# Telegram Word to PDF Bot

A Telegram bot that converts `.docx` files to PDF and sends them back to the user or group.  
Powered by [python-telegram-bot](https://python-telegram-bot.org/) and LibreOffice.

## Features

- Converts `.docx` files to PDF
- Works in groups and private chats
- Cleans up files after sending

## Requirements

- Python 3.8+
- LibreOffice (installed automatically on Railway)
- Telegram Bot Token

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. **Create a `.env` file:**
    ```
    BOT_TOKEN=your-telegram-bot-token
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run locally (LibreOffice must be installed and in PATH):**
    ```bash
    python PDF_converted.py
    ```

## Deploy on Railway

1. Push your code to GitHub.
2. Create a new project on [Railway](https://railway.app/).
3. Add your `BOT_TOKEN` as a variable in the Railway dashboard.
4. Use the provided `start.sh` as your start command:
    ```
    bash start.sh
    ```
5. Deploy and monitor logs for `Bot is running...`.

## File Structure

```
PDF_converted.py
requirements.txt
.env
start.sh
downloads/   # (created automatically)
```

## License

MIT

---

**Made with ❤️ using python-telegram-bot and LibreOffice**