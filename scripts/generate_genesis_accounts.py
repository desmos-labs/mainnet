import csv
import json
import sys
import iso8601
from cosmos_types import *

MONTH_IN_SEC: int = 2629743
COIN_DENOM: str = 'udsm'


class Period:
    """
    Defines a vesting period.
    The amount is expressed in Coin, and the length is expressed in seconds
    """

    def __init__(self, amount: Coin, length: int):
        self._amount = amount
        self._length = length

    def __eq__(self, other):
        """
        Overrides the default implementation
        """
        if isinstance(other, Period):
            return self._amount == other._amount and self._length == other._length
        return False

    def add_amount(self, amount: int):
        """
        Adds a given amount to this period's amount.
        :param amount: integer amount to be added.
        :return: A new Period having the amount that is equals to this period's amount plus the given amount.
        """
        return Period(self._amount.add_int(amount), self._length)

    def to_json(self):
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return {
            'length': str(self._length),
            'amount': [self._amount.to_json()]
        }


class Account:
    """
    Represents a single account.
    """

    def __init__(self, address: str, balance: Coins, periods: [Period]):
        self._address = address
        self._balance = balance
        self._periods = periods

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Account):
            return self._address == other._address and self._periods == other._periods
        return False

    def get_address(self) -> str:
        return self._address

    def get_balance(self):
        return self._balance

    def get_periods(self):
        return self._periods

    def to_json(self, genesis_time: str) -> dict:
        """
        Returns this instance as a JSON element.
        :return: A dictionary containing this information as a JSON object.
        """

        if len(self._periods) > 0:
            return self._get_periodic_vesting_account(genesis_time)
        else:
            return self._get_base_account()

    def _get_base_account(self):
        return {
            '@type': '/cosmos.auth.v1beta1.BaseAccount',
            'address': self._address,
            'pub_key': None,
            'account_number': '0',
            'sequence': '0'
        }

    def _get_end_time(self) -> int:
        end_time = 0
        for period in self._periods:
            end_time += period._length
        return end_time

    def _get_periodic_vesting_account(self, genesis_time: str):
        json_periods = []
        for period in self._periods:
            json_periods.append(period.to_json())
        start_time = int(iso8601.parse_date(genesis_time).timestamp())
        return {
            '@type': '/cosmos.vesting.v1beta1.PeriodicVestingAccount',
            'base_vesting_account': {
                'base_account': {
                    "address": self._address,
                    "pub_key": None,
                    "account_number": '0',
                    "sequence": '0'
                },
                'original_vesting': self._balance.to_json(),
                'delegated_free': [],
                'delegated_vesting': [],
                'end_time': str(start_time + self._get_end_time())
            },
            'start_time': str(start_time),
            'vesting_periods': json_periods,
        }


class Entry:
    """
    Represents a single entry inside the CSV Files containing the overall allocations of all the tokens.
    """

    def __init__(self, csv_row):
        self._address = csv_row['Address']
        self._investors_incentives = int(csv_row['Vesting Investors Incentives'])
        self._uaf = int(csv_row['Vesting UAF'])
        self._foundation_ventures = int(csv_row['Vesting Entities'])
        self._teammates_advisors_early_supporters = int(csv_row['Vesting Teammates/Advisors/Supporters'])
        self._no_vesting = int(csv_row['No Vesting'])
        self._total = int(csv_row['Total'])

    def get_address(self) -> str:
        return self._address

    def get_balance(self) -> Coins:
        return Coins([Coin(self._total, COIN_DENOM)])

    def get_periods(self) -> [Period]:
        periods = []

        # If there are no tokens to be vested, return an empty slice of periods
        if self._total == self._no_vesting:
            return []

        # Amount of tokens that will not be vested
        no_vested = self._no_vesting
        if no_vested > 0:
            periods.append(Period(Coin(no_vested, COIN_DENOM), 0))

        # Amount of tokens that will be vested:
        # - 33% at end of 12th month
        # - 5.58% each month for 11 months
        # - 5.62% at the end of the 24th month
        vested_33 = self._investors_incentives
        if vested_33 > 0:
            # Append the first period for the 12th month
            vested_33_month_12 = int(vested_33 * 0.33)
            periods.append(Period(Coin(vested_33_month_12, COIN_DENOM), 12 * MONTH_IN_SEC))

            # Append 11 periods for months 13 to 23 included
            vested_33_month_13_23 = int(vested_33 * 0.0558)
            periods.extend(
                map(lambda x: Period(Coin(vested_33_month_13_23, COIN_DENOM), 1 * MONTH_IN_SEC), list(range(13, 24))))

            # Append the last period for the 24th month
            vested_33_month_24 = vested_33 - vested_33_month_12 - (vested_33_month_13_23 * 11)
            periods.append(Period(Coin(vested_33_month_24, COIN_DENOM), 1 * MONTH_IN_SEC))

        # Amount of tokens that will be vested:
        # - 50% at the end of the 24th month
        # - 2.08% each month for 23 months
        # - 2.16% at the end of the 48th month
        vested_50 = self._teammates_advisors_early_supporters
        if vested_50 > 0:
            vested_50_month_24 = int(vested_50 * 0.5)

            if self._investors_incentives > 0:
                # The user has some tokens also as an investor.
                # This means we need to merge together the 24th period
                periods[-1] = periods[-1].add_amount(vested_50_month_24)
            else:
                # Append the first period for the 24th month
                periods.append(Period(Coin(vested_50_month_24, COIN_DENOM), 24 * MONTH_IN_SEC))

            # Append 23 periods for month 25 to 47 included
            vested_50_month_25_47 = int(vested_50 * 0.0208)
            periods.extend(
                map(lambda x: Period(Coin(vested_50_month_25_47, COIN_DENOM), 1 * MONTH_IN_SEC), list(range(25, 48))))

            # Append the last period for the 48th month
            vested_50_month_48 = vested_50 - vested_50_month_24 - (vested_50_month_25_47 * 23)
            periods.append(Period(Coin(vested_50_month_48, COIN_DENOM), 1 * MONTH_IN_SEC))

        # Amount of tokens that will be vested:
        # - 4.16% each month for 23 months
        # - 4.32% at the 24th month
        vested_uaf = self._uaf
        if vested_uaf > 0:
            # Append 23 periods for month 1 to 23 included
            vested_uaf_month_1_23 = int(vested_uaf * 0.0416)
            periods.extend(
                map(lambda x: Period(Coin(vested_uaf_month_1_23, COIN_DENOM), 1 * MONTH_IN_SEC), list(range(1, 24))))

            # Append the last period for the 24th month
            vested_uaf_month_24 = vested_uaf - (vested_uaf_month_1_23 * 23)
            periods.append(Period(Coin(vested_uaf_month_24, COIN_DENOM), 1 * MONTH_IN_SEC))

        # Amount of tokens that will be vested in the 4th year:
        # - 25% at end of 39th month
        # - 25% at end of 42th month
        # - 25% at end of 45th month
        # - 25% at end of 48th month
        vested_entities = self._foundation_ventures
        if vested_entities > 0:
            amount = int(vested_entities * 0.25)
            periods.extend([
                Period(Coin(amount, COIN_DENOM), 39 * MONTH_IN_SEC),
                Period(Coin(amount, COIN_DENOM), 3 * MONTH_IN_SEC),
                Period(Coin(amount, COIN_DENOM), 3 * MONTH_IN_SEC),
                Period(Coin(vested_entities - (amount * 3), COIN_DENOM), 3 * MONTH_IN_SEC),
            ])

        return periods


def convert_entry(entry: Entry) -> Account:
    """
    Allows to convert the given entry to an Account instance.
    """
    return Account(
        entry.get_address(),
        entry.get_balance(),
        entry.get_periods(),
    )


def read_csv(file_path: str) -> [Account]:
    """
    Reads the CSV file at the given path as a list of accounts.
    :param file_path: Path to the CSV file that should be read.
    :return: A list of Account representing each row of the file.
    """
    accounts = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Read the lines
        for line in csv_reader:
            accounts.append(convert_entry(Entry(line)))

    return accounts


def write_accounts(accounts: [Account], genesis_file_path: str):
    """
    Writes the given accounts inside the genesis file at the provided path.
    :param accounts: Accounts to be written.
    :param genesis_file_path: Path to the genesis file.
    :return: None
    """
    with open(genesis_file_path, mode='r') as genesis_file:
        genesis = json.load(genesis_file)
        genesis_time = genesis['genesis_time']

        json_accounts = list(map(lambda account: account.to_json(genesis_time), accounts))
        genesis['app_state']['auth']['accounts'] = json_accounts

        balances = list(map(lambda account: Balance(account.get_address(), account.get_balance()), accounts))
        json_balances = list(map(lambda balance: balance.to_json(), balances))
        genesis['app_state']['bank']['balances'] = json_balances

    with open(genesis_file_path, mode='w') as genesis_file:
        json.dump(genesis, genesis_file, indent=2)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception("Please provide the path to the allocation CSV file")

    if len(args) == 1:
        raise Exception("Please provide the path to the genesis file")

    accounts = read_csv(args[0])
    write_accounts(accounts, args[1])
