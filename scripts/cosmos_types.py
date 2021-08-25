class Coin:
    """
    Represent a single coin amount.
    """

    def __init__(self, amount: int, denom: str):
        self._amount = amount
        self._denom = denom

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coin):
            return self._amount == other._amount
        return False

    def get_amount(self) -> int:
        return self._amount

    def get_denom(self) -> str:
        return self._denom

    def is_zero(self) -> bool:
        """
        Tells whether this coin represents a zero amount.
        :return: True iff the coin represents a zero amount.
        """
        return self._amount == 0

    def to_json(self) -> dict:
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return {
            'amount': str(self._amount),
            'denom': str(self._denom)
        }

    @staticmethod
    def from_json(json: dict):
        return Coin(int(json['amount']), json['denom'])


class Coins:
    """
    Represents a list of Coin.
    """

    def __init__(self, coins: [Coin]):
        self._coins = coins

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coins):
            return self._coins == other._coins
        return False

    def is_zero(self) -> bool:
        """
        Tells whether this instance represents a zero amount.
        :return: True iff this instance represents a zero amount.
        """
        return len(self._coins) == 0 or all(map(lambda coin: coin.is_zero(), self._coins))

    def to_json(self) -> [dict]:
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return list(map(lambda coin: coin.to_json(), self._coins))

    @staticmethod
    def from_json(coins: [dict]):
        return Coins(list(map(lambda json: Coin.from_json(json), coins)))


class Balance:
    """
    Represents a single account balance.
    """

    def __init__(self, address: str, balance: Coins):
        self._address = address
        self._balance = balance

    def is_zero(self) -> bool:
        """
        Tells whether this instance represents a zero amount.
        :return: True iff this instance represents a zero amount.
        """
        return self._balance.is_zero()

    def to_json(self) -> dict:
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return {
            'address': self._address,
            'coins': self._balance.to_json()
        }

    @staticmethod
    def from_json(json: dict):
        return Balance(json['address'], Coins.from_json(json['coins']))
