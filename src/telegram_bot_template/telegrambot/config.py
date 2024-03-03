class TelegramBotConfig():
    def __init__(self, token: str, proxy_url = None) -> None:
        self.token = token
        self.proxy_url = proxy_url