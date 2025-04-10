class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount}€ sur le compte de {self.account_holder}.")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Retrait de {amount}€ depuis le compte de {self.account_holder}.")
        else:
            print("Le montant du retrait doit être positif et ne pas dépasser le solde.")

    def display_balance(self):
        print(f"Compte de {self.account_holder}: {self.balance}€")
    

account = BankAccount("Elodie", 1000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
account.withdraw(2000.0)
account.deposit(-100.0)## Écrivez votre code ici !
