import unittest
import generate_genesis_accounts as genesis

if __name__ == '__main__':
    unittest.main()


class TestEntry(unittest.TestCase):
    def test_get_periods_investors_incentives(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 1000,
            'Vesting UAF': 0,
            'Vesting Entities': 0,
            'Vesting Teammates, Advisors, and Supporters': 0,
            'No Vesting': 0,
            'Total': 1000,
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

    def test_get_periods_teammates_advisors_early_supporters(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 0,
            'Vesting Entities': 0,
            'Vesting Teammates, Advisors, and Supporters': 1000,
            'No Vesting': 0,
            'Total': 1000,
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

    def test_get_periods_uaf(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 1225,
            'Vesting Entities': 0,
            'Vesting Teammates, Advisors, and Supporters': 0,
            'No Vesting': 0,
            'Total': 1225,
        }
        entry = genesis.Entry(row)
        periods = entry.get_periods()

        # 1225 tokens to be vested over 24 months, 4.16% per month
        # 50 + (2.08 * 23) + 2.16
        self.assertListEqual(periods, [
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(50), 1 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(75), 1 * genesis.MONTH_IN_SEC),
        ])

    def test_get_periods_entities(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 0,
            'Vesting Entities': 1225,
            'Vesting Teammates, Advisors, and Supporters': 0,
            'No Vesting': 0,
            'Total': 1225,
        }
        entry = genesis.Entry(row)
        periods = entry.get_periods()

        # 1225 tokens to be vested 25% at the end of the
        self.assertListEqual(periods, [
            genesis.Period(genesis.Coin(306), 39 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(306), 42 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(306), 45 * genesis.MONTH_IN_SEC),
            genesis.Period(genesis.Coin(307), 48 * genesis.MONTH_IN_SEC),
        ])
