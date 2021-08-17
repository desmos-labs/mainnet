import json
import sys


def check_total_genesis_amount(genesis_file_path: str):
    total_amount = 0
    with open(genesis_file_path, 'r') as genesis_file:
        genesis = json.load(genesis_file)

        accounts = genesis['app_state']['auth']['accounts']
        for account in accounts:
            if account['@type'] == '/cosmos.vesting.v1beta1.PeriodicVestingAccount':
                total_amount += int(account['base_vesting_account']['original_vesting'][0]['amount'])

        balances = genesis['app_state']['bank']['balances']
        for balance in balances:
            total_amount += int(balance['coins'][0]['amount'])

    if total_amount != 100_000_000_000_000:
        raise Exception(f"Amount is not 100MM DSM. Total amount: {total_amount}")


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception("Please provide the path to the genesis file")

    check_total_genesis_amount(args[0])

    print("Genesis is valid")
