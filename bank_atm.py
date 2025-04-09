class BankAccount:
    def __init__(self, initial_balance=100):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} eurot lisatud. Uus saldo: {self.balance} eurot.")
        else:
            print("Sisestage korrektne summa.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} eurot välja võetud. Uus saldo: {self.balance} eurot.")
        else:
            print("Tehing ebaõnnestus. Kontrollige summat ja saldo jääki.")

    def check_balance(self):
        print(f"Teie konto saldo: {self.balance} eurot.")


def main():
    username = input("Sisesta kasutajanimi: ")
    password = input("Sisesta parool: ")

    # Lihtne autentimine
    if username != "kasutaja" or password != "parool":
        print("Vale kasutajanimi või parool!")
        return

    print("Sisselogimine edukas! Tere tulemast oma pangakontole.")
    account = BankAccount()

    while True:
        print("\nMenüü:")
        print("1. Sissemakse")
        print("2. Väljamakse")
        print("3. Saldo vaatamine")
        print("4. Välju")

        choice = input("Vali toiming: ")

        if choice == "1":
            amount = float(input("Sisesta sissemakse summa: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Sisesta väljamakse summa: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Väljumine... Head päeva!")
            break
        else:
            print("Vale valik. Palun proovi uuesti.")


if __name__ == "__main__":
    main()
