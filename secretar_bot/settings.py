
from pydantic import BaseModel


class BotSettings(BaseModel):
    TOKEN: str = '6209095925:AAH0EeJoZfPZh7cIjgSwRoaOhvrYqnhQK00'

config = BotSettings()
