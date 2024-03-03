import logging
import sys
from dependency_injector.wiring import Provide

from telegram_bot_template.dependencyinjection.containers import Container
from telegram_bot_template.telegrambot.config import TelegramBotConfig
from telegram_bot_template.telegrambot.engine import TelegramBotEngine


def main(bot_config: TelegramBotConfig = Provide[Container.bot_config]) -> None:
    try:
        TelegramBotEngine.run(bot_config)
    except Exception as exp:
        logging.fatal(exp)
        raise


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main(*sys.argv[1:])
