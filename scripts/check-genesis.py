import json
import sys
from datetime import datetime

AUGUST_31_2025_TIMESTAMP = 1756652400


def check_total_genesis_amount(genesis_file_path: str):
    balances_amount = 0
    with open(genesis_file_path, 'r') as genesis_file:
        genesis = json.load(genesis_file)

        balances = genesis['app_state']['bank']['balances']
        for balance in balances:
            for coin in balance['coins']:
                balances_amount += int(coin['amount'])

    if balances_amount != 100_000_000_000_000:
        raise Exception(f"Balances amount is not 100MM DSM: {balances_amount}")


def check_accounts_vesting_end_time(genesis_file_path: str):
    with open(genesis_file_path, 'r') as genesis_file:
        genesis = json.load(genesis_file)

        accounts = genesis['app_state']['auth']['accounts']
        for account in accounts:
            if account['@type'] == '/cosmos.vesting.v1beta1.PeriodicVestingAccount':
                base_vesting_account = account['base_vesting_account']
                end_time = int(base_vesting_account['end_time'])
                if end_time > AUGUST_31_2025_TIMESTAMP:
                    address = base_vesting_account['base_account']['address']
                    date = datetime.fromtimestamp(end_time)
                    raise Exception(f"Account {address} has vesting end date set to {date}")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception("Please provide the path to the genesis file")

    check_total_genesis_amount(args[0])
    check_accounts_vesting_end_time(args[0])

    print("Genesis is valid")
