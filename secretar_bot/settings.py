
from pydantic import BaseModel


class BotSettings(BaseModel):
    TOKEN: str = '7322700222:AAHLDJ3Ie7gJdeObu4ETj2ukfrXt_aN-bpQ'

config = BotSettings()
