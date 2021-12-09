from Crypto import *

class Transaction:
    amount:int=0
    payer:str=""
    payee:str=""
    def __init__(self,amount:int,payer:str,payee:str):
        self.amount=amount
        self.payer=payer
        self.payee=payee
    