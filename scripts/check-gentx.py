import json
import sys
import glob
from cosmos_types import *


class GenTx:
    """
    Represents a single genesis transaction.
    """

    def __init__(self, delegator_address: str, self_delegate_amount: Coin):
        self.delegator_address = delegator_address
        self.self_delegate_amount = self_delegate_amount

    @staticmethod
    def from_json(gentx_json: dict):
        return GenTx(
            gentx_json['body']['messages'][0]['delegator_address'],
            Coin.from_json(gentx_json['body']['messages'][0]['value'])
        )


def parse_gentxs(gentxs_folder_path: str) -> [GenTx]:
    """
    Parses the genesis transactions JSON files present inside the folder at the given path.
    :param gentxs_folder_path: Path to the folder containing the genesis transactions to be parsed.
    :return: A list of GenTx objects containing each one the data about a single genesis transaction.
    """
    gentxs_files = glob.glob(f"{gentxs_folder_path}/*.json")
    gen = None
    with open("genesis/genesis.json", 'r') as genesis:
        gen = json.load(genesis)
    txs = []
    for gentx_file_path in gentxs_files:
        with open(gentx_file_path, 'r') as gentx_file:
            gentx_json = json.load(gentx_file)
            address = gentx_json['body']['messages'][0]['delegator_address']
            gen["app_state"]["bank"]["balances"] = {
                "address": address,
                "coins": [
                    {
                        "denom": "ujkl",
                        "amount": "1666666666"
                    }
                ]
            }
            txs.append(GenTx.from_json(gentx_json))
    with open("genesis/genesis.json", 'w') as genesis:
        json.dump(gen, genesis, indent=4)
    return txs


def check_self_delegation_validity(self_delegate: Coin):
    """
    Checks if the given self delegate amount is valid.
    An amount is considered valid only if it does not exceed 10.000 DSM.

    :param self_delegate: Self delegation amount to be checked.
    """
    if self_delegate.get_amount() > 10_000_000_000:
        raise Exception('Self delegation amount exceeds 10.000 DSM')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception("Please provide the path to the gentxs folder")

    gentxs = parse_gentxs(args[0])
    for gentx in gentxs:
        check_self_delegation_validity(gentx.self_delegate_amount)

    print("Genesis transactions are valid")
