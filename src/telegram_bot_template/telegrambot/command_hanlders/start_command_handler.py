# from typing import override
from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot_template.telegrambot.command_hanlders.base import BaseCommandHandler


class StartCommandHandler(BaseCommandHandler):
    def __init__(self):
        super().__init__("start")

    # @override
    async def handle_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = self.__get_message(update)
        await update.message.reply_html(message)

    def __get_message(self, update: Update) -> str:
        return f"Hi {update.effective_user.username}"
