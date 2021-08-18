import json
import sys


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


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception("Please provide the path to the genesis file")

    check_total_genesis_amount(args[0])

    print("Genesis is valid")
