from telegram.ext import ApplicationBuilder, Application
from telegram_bot_template.telegrambot.config import TelegramBotConfig
from telegram_bot_template.telegrambot.command_hanlders.start_command_handler import StartCommandHandler


class TelegramBotEngine:
    @staticmethod
    def create_app(bot_conifg: TelegramBotConfig) -> Application:
        app_builder = ApplicationBuilder().token(bot_conifg.token)
        proxy_url = bot_conifg.proxy_url
        if proxy_url is not None:
            app_builder = app_builder.proxy_url(proxy_url).get_updates_proxy_url(
                proxy_url
            )
        return app_builder.build()

    @staticmethod
    def run(bot_conifg: TelegramBotConfig) -> None:
        app: Application = TelegramBotEngine.create_app(bot_conifg)
        app.add_handler(StartCommandHandler())
        app.run_polling(drop_pending_updates=True)
