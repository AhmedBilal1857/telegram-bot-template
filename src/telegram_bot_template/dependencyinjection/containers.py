
import logging.config
from dependency_injector import containers, providers

from telegram_bot_template.telegrambot.config import TelegramBotConfig

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    bot_config = providers.Singleton(
        TelegramBotConfig,
        config.telegram.bot_token
    )

    # db = providers.Singleton(Database, db_url=config.db.url)

    # user_repository = providers.Factory(
    #     GroupUserRepository,
    #     session_factory=db.provided.session,
    # )

    # user_service = providers.Factory(
    #     GroupUserService,
    #     user_repository=user_repository,
    # )