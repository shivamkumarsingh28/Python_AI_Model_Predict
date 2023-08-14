from pydantic import BaseModel

# check input variable is only number not other through this BankNote Class
class BankNote(BaseModel):
    variance : float
    skewness : float
    curtosis : float
    entropy : float
