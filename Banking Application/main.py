class InsufficientFundsException(Exception):
    pass

class InvalidAccountNumberException(Exception):
    pass

def print_account_balances(accounts):
    #print("Updated Account Balances:")
    for account, balance in accounts.items():
        print(f"Account No: {account}, Balance: ₹{balance}")

def load_accounts(filename):
    accounts = {}
    with open(filename, 'r') as file:
        for line in file:
            account_number, balance = line.strip().split(',')
            accounts[account_number] = float(balance)
    return accounts

def transfer_funds(accounts, from_account, to_account, amount):
    if from_account not in accounts:
        raise InvalidAccountNumberException(f"Invalid account number: {from_account}")
    if to_account not in accounts:
        raise InvalidAccountNumberException(f"Invalid account number: {to_account}")
    if accounts[from_account] < amount:
        raise InsufficientFundsException("Insufficient funds for the transfer.")
    print(f"Transferred ₹{amount} from Account No: {from_account} to Account No: {to_account}")
    accounts[from_account] -= amount
    accounts[to_account] += amount

def main():
    accounts = load_accounts('accounts.txt')

    try:
        transfer_funds(accounts, '12345678', '87654321', 1000)
        print("Transfer successful.")
    except InsufficientFundsException as e:
        print(e)
    except InvalidAccountNumberException as e:
        print(e)
    #print(f"Transferred {amount} from Account No: {from_account} to Account No: {to_account}")
    print(f"Updated Account Balances: {print_account_balances(accounts)}")

if __name__ == "__main__":
    main()
