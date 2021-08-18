import unittest
from generate_genesis_accounts import *

if __name__ == '__main__':
    unittest.main()


class TestEntry(unittest.TestCase):
    def test_get_periods_investors_incentives(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 1000,
            'Vesting UAF': 0,
            'Vesting Entities': 0,
            'Vesting Teammates/Advisors/Supporters': 0,
            'No Vesting': 0,
            'Total': 1000,
        }
        entry = Entry(row)
        periods = entry.get_periods()

        # 1000 tokens to be vested using the formula
        # 33 + (5.58 * 11) + 5.62
        self.assertListEqual(periods, [
            Period(Coin(330, COIN_DENOM), 12 * MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(55, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(65, COIN_DENOM), MONTH_IN_SEC),
        ])

    def test_get_periods_teammates_advisors_early_supporters(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 0,
            'Vesting Entities': 0,
            'Vesting Teammates/Advisors/Supporters': 1000,
            'No Vesting': 0,
            'Total': 1000,
        }
        entry = Entry(row)
        periods = entry.get_periods()

        # 1000 tokens to be vested using the formula
        # 50 + (2.08 * 23) + 2.16
        self.assertListEqual(periods, [
            Period(Coin(500, COIN_DENOM), 24 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(40, COIN_DENOM), 1 * MONTH_IN_SEC),
        ])

    def test_get_periods_uaf(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 1225,
            'Vesting Entities': 0,
            'Vesting Teammates/Advisors/Supporters': 0,
            'No Vesting': 0,
            'Total': 1225,
        }
        entry = Entry(row)
        periods = entry.get_periods()

        # 1225 tokens to be vested over 24 months, 4.16% per month
        # 50 + (2.08 * 23) + 2.16
        self.assertListEqual(periods, [
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(50, COIN_DENOM), 1 * MONTH_IN_SEC),
            Period(Coin(75, COIN_DENOM), 1 * MONTH_IN_SEC),
        ])

    def test_get_periods_entities(self):
        row = {
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 0,
            'Vesting Entities': 1225,
            'Vesting Teammates/Advisors/Supporters': 0,
            'No Vesting': 0,
            'Total': 1225,
        }
        entry = Entry(row)
        periods = entry.get_periods()

        # 1225 tokens to be vested 25% at the end of the
        self.assertListEqual(periods, [
            Period(Coin(306, COIN_DENOM), 39 * MONTH_IN_SEC),
            Period(Coin(306, COIN_DENOM), 42 * MONTH_IN_SEC),
            Period(Coin(306, COIN_DENOM), 45 * MONTH_IN_SEC),
            Period(Coin(307, COIN_DENOM), 48 * MONTH_IN_SEC),
        ])

    def test_convert_entry(self):
        entry = Entry({
            'Address': 'desmos1kztpzafhwx7ymv65fw79cqhyz07fes6hxfvfm9',
            'Vesting Investors Incentives': 0,
            'Vesting UAF': 0,
            'Vesting Entities': 0,
            'Vesting Teammates/Advisors/Supporters': 990,
            'No Vesting': 10,
            'Total Vested': 990,
            'Total Not Vested': 10,
            'Total': 1000,
        })

        account = convert_entry(entry)
        self.assertEqual(account.get_balance(), Coins([Coin(1000, COIN_DENOM)]))
        self.assertListEqual(account.get_periods(), [
            Period(Coin(10, COIN_DENOM), 0),
            Period(Coin(495, COIN_DENOM), 24 * MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(20, COIN_DENOM), MONTH_IN_SEC),
            Period(Coin(35, COIN_DENOM), MONTH_IN_SEC),
        ])
