from telegram import Update
from telegram.ext import ChatMemberHandler, ContextTypes

class GreetChatMemberHandler(ChatMemberHandler):
    def __init__(self):
        super().__init__(self.greet_chatmember_handler)

    async def greet_chatmember_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass