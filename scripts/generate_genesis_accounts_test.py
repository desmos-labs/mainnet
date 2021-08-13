import unittest
import generate_genesis_accounts as genesis

if __name__ == '__main__':
    unittest.main()


class TestEntry(unittest.TestCase):
    def test_get_periods_vested_33(self):
        row = {
            'address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'angel': 200,
            'seed': 200,
            'primer': 200,
            'validator': 200,
            'genesis_invite': 200,
            'teammate': 0,
            'total': 0,
        }
        entry = genesis.Entry(row)
        periods = entry.get_periods()

        # 1000 tokens to be vested using the formula
        # 33 + (5.58 * 11) + 5.62
        self.assertListEqual(periods, [
            genesis.Period(genesis.Coin(330), 12 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(55), genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(65), genesis.MONTH_IN_SEC),
        ])

    def test_get_periods_vested_50(self):
        row = {
            'address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'angel': 0,
            'seed': 0,
            'primer': 0,
            'validator': 0,
            'genesis_invite': 0,
            'teammate': 1000,
            'total': 0,
        }
        entry = genesis.Entry(row)
        periods = entry.get_periods()

        # 1000 tokens to be vested using the formula
        # 50 + (2.08 * 23) + 2.16
        self.assertListEqual(periods, [
            genesis.Period(genesis.Coin(500), 24 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(20), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(40), 1 * genesis.MONTH_IN_SEC),
        ])
