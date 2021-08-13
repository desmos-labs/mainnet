# Genesis Parameters

DESMOS will be running with the following parameters at genesis. Most of the parameters can be updated by using a `ParameterChangeProposal` and the `x/gov` module. Below we list only the changes to the parameters from the  Cosmos SDK modules. All the other parameters values are going to be the default ones. 

## Base

* `"genesis_time": "2021-08-31T15:00:00Z"`. 31 Aug 2021 3pm UTC
* `"chain_id": "desmos-1"`. The Chain ID of the DESMOS mainnet will be `desmos-1`.

## Consensus

* `"max_gas": "100000000"`. Maximum gas per block is set to `100,000,000`. Considering the default `200,000` gas per transaction, this means `500` transactions should be included inside each block.
* `"max_age_duration": "1209600000000000"`. 2 weeks for double sign evidence.
* `"max_age_num_blocks": "204670"`. This is calculated by `max_age_duration` / `5.91` which is the average block time on `morpheus-apollo-2` testnet.

## Crisis

* `"amount": "13333000000"`. We will need `13333 DSM` to halt the chain if anything goes wrong.

## Distribution

* `"community_tax": "0.200000000000000000"`. The tax on inflation and fees for community pool will be `20%`.

## Governance

* `"min_deposit": 1337000000udesmos`. The minimum deposit to make a proposal turn into voting period will be `1337 DSM`.
* `"max_deposit_period": "259200s"`. The maxmium deposit period for a proposal will be `259,200 seconds` which is `3 days`.
* `"voting_period": "604800s"`. The voting period of a proposal will be `604,800 seconds` which is `7 days`.

## Mint

* `"mint_denom": "udsm"`. The mint denom will be `udsm`. This is the smallest unit of the staking token `DSM`.
* `"inflation_rate_change": "1.000000000000000000"`. Inflation change rate is set to `1` to have the optimum speed to make the inflation rate change to the target inflation.
* `"inflation_max": "0.000000000000000000"` and `"inflation_min": "0.000000000000000000"`. Both parameters are set to `0` at genesis to avoid imbalanced suddenn change of token distribution at launch. These values will be changed by a `ParameterChangePropoal` right after launch. According to the parameters in `Governance` module, the earliest time for the parameter change to happen will be 7 days after the genesis time. This period of zero inflation will give enough time for token holders to stake until inflation is turned on. The `inflation_max` will be set to `0.8` and `inflation_min` will be set to `0.4` as written in the whitepaper.
* `"goal_bonded": "0.9"`. We see staking ratio can reach over 82% on other networks. Setting the `goal_bonded` higher to attract token holders to stake and incentivize early stakers.
* `"blocks_per_year": "5339695"`. Base on `5.91 seconds` of average block time on `morpheus-apollo-2` testnet.

## Slashing

* `"signed_blocks_window": "150000"`. This is around `24 hours` based on `5.91 seconds` block time.
* `"min_signed_per_window": "0.050000000000000000`. Validators will be kept on active set if they sign `5%` of blocks in every `signed_blocks_window`.
* `"downtime_jail_duration": "1800s"`. Down time for uptime jail is `30 minutes`.
* `"slash_fraction_double_sign": "0.050000000000000000"`. Validators and their delegators will encounter `5%` slashing on their staked tokens if the validators double sign.
* `"slash_fraction_downtime": "0.000100000000000000"`. Validators and their delegators will encounter `0.01%` slashing on their staked tokens if the validators cannot meet the uptime requirement.

## Staking

* `"unbonding_time": "1209600s"`. Unbonding period on `DESMOS` is set to `1209600 seconds` which is `14 days`.
* `"bond_denom": "udsm"`. The bond denom is `udsm`. This is the smallest unit of the `DSM`.
