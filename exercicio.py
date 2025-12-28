class contabancaria:
    def __init__(self, titular, saldo ):
        self.titular = titular 
        self._saldo = saldo 
        self.ativo = False
    @property
    
    def saldo(self):
        return self._saldo 

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo =  True
    

    def __str__(self):
        return f"titular: {self.titular} | saldo: R$ {self.saldo}"
        
    
        
conta1 = contabancaria("João", 500)
contabancaria.ativar_conta(conta1)
print ("conta 1 ativo")
conta2 = contabancaria("Maria", 1200)       
        
print(conta1)
print(conta2)
        

        