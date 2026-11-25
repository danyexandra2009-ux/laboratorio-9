class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self . titular = titular
        self ._saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self ._saldo += monto
        else:
            print("monto invalido")

    def retirar(self, monto):
        if 0 < monto <= self ._saldo:
            self ._saldo -= monto
            return True
        else:
            print("fondos insuficientes")
            return False
        
    def obtener_saldo(self):
        return self ._saldo
    
    def transferir(self, destino, monto):
        if self.retirar(monto):
            destino.depositar(monto)
        
c1 = CuentaBancaria("Pedro", 100)
c2 = CuentaBancaria("María", 50)

c1.depositar(200)
c1.obtener_saldo()     # → 300

c1.retirar(50)
c1.obtener_saldo()     # → 250

c1.retirar(500)        # → "Fondos insuficientes"

c1.transferir(c2, 100)
c1.obtener_saldo()     # → 150
c2.obtener_saldo()