
from pydantic import BaseModel


class BotSettings(BaseModel):
    TOKEN: str = '7065341545:AAECpb0R87PNAB0z2Vwl2DgmRrDYFMMIK4M'

config = BotSettings()
