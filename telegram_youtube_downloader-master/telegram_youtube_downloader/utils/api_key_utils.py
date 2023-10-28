import os


class ApiKeyUtils:
    TELEGRAM_BOT_ENVIRONMENT_NAME = "6783731179:AAHApTvTjrKtS1tX2BLm9Cq6mmaX6QGdTlE"
    YOUTUBE_API_ENVIRONMENT_NAME = "YOUTUBE_API_KEY"

    @staticmethod
    def get_telegram_bot_key():
        return os.environ.get(ApiKeyUtils.TELEGRAM_BOT_ENVIRONMENT_NAME, None)

    @staticmethod
    def get_youtube_api_key():
        return os.environ.get(ApiKeyUtils.YOUTUBE_API_ENVIRONMENT_NAME, None)
