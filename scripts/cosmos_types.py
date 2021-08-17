class Coin:
    """
    Represent a single coin amount.
    """

    def __init__(self, amount: int, denom: str):
        self.amount = amount
        self.denom = denom

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coin):
            return self.amount == other.amount
        return False

    def is_zero(self) -> bool:
        """
        Tells whether this coin represents a zero amount.
        :return: True iff the coin represents a zero amount.
        """
        return self.amount == 0

    def to_json(self) -> dict:
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return {
            'amount': str(self.amount),
            'denom': str(self.denom)
        }

    @staticmethod
    def from_json(json: dict):
        return Coin(int(json['amount']), json['denom'])


class Coins:
    """
    Represents a list of Coin.
    """

    def __init__(self, coins: [Coin]):
        self.coins = coins

    def is_zero(self) -> bool:
        """
        Tells whether this instance represents a zero amount.
        :return: True iff this instance represents a zero amount.
        """
        return len(self.coins) == 0 or all(map(lambda coin: coin.is_zero(), self.coins))

    def to_json(self) -> [dict]:
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return list(map(lambda coin: coin.to_json(), self.coins))

    @staticmethod
    def from_json(coins: [dict]):
        return Coins(list(map(lambda json: Coin.from_json(json), coins)))


class Balance:
    """
    Represents a single account balance.
    """

    def __init__(self, address: str, balance: Coins):
        self.address = address
        self.balance = balance

    def is_zero(self) -> bool:
        """
        Tells whether this instance represents a zero amount.
        :return: True iff this instance represents a zero amount.
        """
        return self.balance.is_zero()

    def to_json(self) -> dict:
        """
        Gets the JSON representation of this instance.
        :return: A dictionary representing the JSON version of this instance.
        """
        return {
            'address': self.address,
            'coins': self.balance.to_json()
        }

    @staticmethod
    def from_json(json: dict):
        return Balance(json['address'], Coins.from_json(json['coins']))
