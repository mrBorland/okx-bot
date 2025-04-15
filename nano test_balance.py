from okx.Account import Account

api_key = "8ce4bd62-9328-495e-9556-2bf1107b3ac2"
secret_key = "AB2C36344430A6080F3C5645155074B3"
passphrase = "Slipknot221989@"

accountAPI = Account(
    api_key=api_key,
    api_secret_key=secret_key,
    passphrase=passphrase,
    use_server_time=False,
    flag='0'
)

try:
    balance = accountAPI.get_account_balance("USDT")
    print(balance)
except Exception as e:
    print("Помилка:", e)
