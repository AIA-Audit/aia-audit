import requests

from aia_audit.lib.database import Database
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup

class Telegram:

    token = None
    chats_id = []
    update_queue = None
    updater = None
    dispatcher = None

    def start(self, update, context):
        print("Telegram bot started for chat_id: " + str(update.effective_chat.id))
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text="You have been registered to receive notifications from AIA Audit")
        self.register_chat(chat_id)

    def echo(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def open(self):
        self.token = self.get_token()
        self.get_chats_id()
        self.updater = Updater(self.token)
        self.dispatcher = self.updater.dispatcher
        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)
        echo_handler = MessageHandler(None, self.echo)
        self.dispatcher.add_handler(echo_handler)
        self.updater.start_polling()
        self.mass_send_message("Telegram bot started")

    def stop(self):
        self.updater.stop()

    def mass_send_message(self, text):
        for chat_id in self.chats_id:
            self.updater.bot.send_message(chat_id=chat_id[0], text=text)

    def notify_scan_finished(self, device_count, vulnerability_count):
        database = Database()
        last_scan_id = database.query_select("SELECT id FROM scans ORDER BY id DESC LIMIT 1")[0][0]
        scan_url = "http://"
        scan_url += database.query_select("SELECT value FROM settings WHERE name = 'website_address'")[0][0] + ":" + database.query_select("SELECT value FROM settings WHERE name = 'website_port'")[0][0] + "/scan/" + str(last_scan_id)
        message = "🔍 Scan finished! ✅\n\n"
        message += f"{device_count} devices 📱🖥️ were scanned, and {vulnerability_count} vulnerabilities 🛡️ were found.\n\n"
        message += f"🔗 You can access the scan results: {scan_url}.\n\n"
        message += "Thank you for using our scanning service! If you have any questions or need further assistance, feel free to contact us. 💪😊"
        self.mass_send_message(message)

    def get_token(self):
        database = Database()
        self.token = database.query_select("SELECT value FROM settings WHERE name = 'telegram_token'")[0][0]
        return self.token
    
    def check_enabled(self):
        database = Database()
        self.enabled = database.query_select("SELECT value FROM settings WHERE name = 'telegram_notify'")[0][0]
        return self.enabled

    def get_chats_id(self):
        database = Database()
        self.chats_id = database.query_select("SELECT chat_id FROM telegram_chats")
        return self.chats_id
    
    def register_chat(self, chat_id):
        database = Database()
        if database.query_select("SELECT chat_id FROM telegram_chats WHERE chat_id = " + str(chat_id)) == []:
            database.query("INSERT INTO telegram_chats (chat_id) VALUES (" + str(chat_id) + ")")
            self.get_chats_id()
            print ("[*] Chat_id " + str(chat_id) + " registered")
    
telegram = Telegram()