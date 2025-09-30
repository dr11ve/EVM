from web3 import Web3
import os

# Количество кошельков для создания
NUM_WALLETS = 155

# Инициализация Web3
w3 = Web3()

# Списки для хранения приватных ключей и адресов
private_keys = []
addresses = []

# Генерация кошельков
for _ in range(NUM_WALLETS):
    # Создаём новый аккаунт
    account = w3.eth.account.create()
    # Сохраняем приватный ключ (в формате hex с префиксом 0x)
    private_keys.append(account.key.hex())
    # Сохраняем адрес кошелька
    addresses.append(account.address)

# Сохранение приватных ключей в private.txt
with open('private.txt', 'w') as f:
    for key in private_keys:
        f.write(f"{key}\n")

# Сохранение адресов в address.txt
with open('address.txt', 'w') as f:
    for addr in addresses:
        f.write(f"{addr}\n")

print(f"Создано {NUM_WALLETS} кошельков.")
print("Приватные ключи сохранены в private.txt")
print("Адреса сохранены в address.txt")