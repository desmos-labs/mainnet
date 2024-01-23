[![Website](.img/cover.jpg)](https://desmos.network)

# Desmos Mainnet
This is the official repository used to launch the first Desmos mainnet. 

In here you will find the description and motivation of the various on-chain parameters values that we have decided to use.
You can also check for the used genesis state as well as get all the info about the version of Desmos that has been used to launch the mainnet.

## Binary version
The Desmos version used to start the mainnet is the following: 

```shell
$ desmos version --long
name: Desmos
server_name: desmos
version: 1.0.1
commit: 852bfd12f234126f1c9e48e785c5bb8fbcd96647
```

To checkout this version run: 

```
git checkout tags/v1.0.1
```

## State sync 
Please note that if you want to use the state sync option to create a new validator node, 
you will have to choose the following Desmos versions based on the state sync height you choose: 

|  State sync height  | Desmos version | How to checkout the tag    |
|:-------------------:|:--------------:|:---------------------------|
|    `0 - 1149679`    |    `v1.0.1`    | `git checkout tags/v1.0.1` |
| `1149680 - 1347304` |    `v2.3.0`    | `git checkout tags/v2.3.0` |
|     `> 1347305`     |    `v2.3.1`    | `git checkout tags/v2.3.1` |

## Genesis file 
The mainnet genesis file has been generated using the genesis state and transactions present inside the [`data` folder](data).  

The result genesis state is the one named [`genesis.json`](genesis.json) and has the following hashsum:

```shell
$ jq -S -c -M '' genesis.json | shasum -a 256
9b0f233e0e6f5ca0190468f43e655a07431ef9acc0c0124789bb094b9340e6a4  -
```

#### Parameters
Desmos will be running with the following parameters at genesis. 

Most of the parameters can be updated by using a `ParameterChangeProposal` and the `x/gov` module. 
Below we list only the changes to the parameters from the Cosmos SDK modules. 
All the other parameters values are going to be the default ones. 

#### Base
* `"genesis_time": "2021-08-31T16:15:00Z"`
* `"chain_id": "desmos-mainnet"`

#### Auth
* `"tx_sig_limit": "10"`  
   Maximum signatures per transaction is increased to `10`.


#### Consensus
* `"max_gas": "100000000"`  
   Maximum gas per block is set to `100,000,000`. Considering the default `200,000` gas per transaction, this means `500` transactions should be included inside each block.
* `"max_age_duration": "1209600000000000"`  
   2 weeks for double sign evidence.
* `"max_age_num_blocks": "204670"`  
   This is calculated by `max_age_duration` / `5.91` which is the average block time on `morpheus-apollo-2` testnet.

#### Crisis
* `"amount": "13333000000"`  
   We will need `13333 DSM` to halt the chain if anything goes wrong.

#### Distribution
* `"community_tax": "0.200000000000000000"`  
   The tax on inflation and fees for community pool will be `20%`.

#### Governance
* `"min_deposit": 500000000udesmos`  
   The minimum deposit to make a proposal turn into voting period will be `500 DSM`.
* `"max_deposit_period": "259200s"`  
   The maxmium deposit period for a proposal will be `259,200 seconds` which is `3 days`.
* `"voting_period": "604800s"`  
   The voting period of a proposal will be `604,800 seconds` which is `7 days`.

#### Mint
* `"mint_denom": "udsm"`  
   The mint denom will be `udsm`. This is the smallest unit of the staking token `DSM`.
* `"inflation_rate_change": "1.000000000000000000"`  
   Inflation change rate is set to `1` to have the optimum speed to make the inflation rate change to the target inflation.
* `"inflation": "0.000000000000000000"` <sup>1</sup>
* `"inflation_max": "0.000000000000000000"` <sup>1</sup>
* `"inflation_min": "0.000000000000000000"` <sup>1</sup>
* `"goal_bonded": "0.9"`  
   We see staking ratio can reach over 82% on other networks. We are setting a higher `goal_bonded` to attract token holders to stake and incentivize early stakers.
* `"blocks_per_year": "5339695"`  
   Based on `5.91 seconds` of average block time on `morpheus-apollo-2` testnet.

<sup>1</sup> All these parameters are set to `0` at genesis to avoid an imbalanced sudden change of token distribution at launch. 
These values will be changed by a `ParameterChangePropoal` right after launch.   
According to the parameters inside the _Governance_ module, the earliest time for the parameter change to happen will be 7 days after the genesis time. 
This period of zero inflation will give enough time for token holders to stake until inflation is turned on.   
The `inflation_max` will be set to `0.8` and `inflation_min` will be set to `0.4` as written in the whitepaper.
The `inflation` will be computed based on the percentage of tokens delegated at that time.

#### Slashing
* `"signed_blocks_window": "150000"`  
   This is around `24 hours` based on `5.91 seconds` block time.
* `"min_signed_per_window": "0.050000000000000000`  
   Validators will be kept on active set if they sign `5%` of blocks in every `signed_blocks_window`.
* `"downtime_jail_duration": "1800s"`  
   Down time for uptime jail is `30 minutes`.
* `"slash_fraction_double_sign": "0.050000000000000000"`  
   Validators and their delegators will encounter `5%` slashing on their staked tokens if the validators double sign.
* `"slash_fraction_downtime": "0.000100000000000000"`  
   Validators and their delegators will encounter `0.01%` slashing on their staked tokens if the validators cannot meet the uptime requirement.

#### Staking
* `"unbonding_time": "1209600s"`  
   Unbonding period on `DESMOS` is set to `1209600 seconds` which is `14 days`.
* `"bond_denom": "udsm"`  
   The bond denom is `udsm`. This is the smallest unit of the `DSM`.

#### Transfer
* `"send_enabled": false` <sup>1</sup>
* `"receive_enabled": false` <sup>1</sup>

<sup>1</sup> Both the sending and receiving of tokens using IBC will be disabled at genesis. 
We will enable them after the chain start with a governance proposal.  

## Seed Nodes
While connecting to the Desmos mainnet, you can use the following seed nodes to bootstrap your node:

```sh
9bde6ab4e0e00f721cc3f5b4b35f3a0e8979fab5@seed-1.mainnet.desmos.network
5c86915026093f9a2f81e5910107cf14676b48fc@seed-2.mainnet.desmos.network
45105c7241068904bdf5a32c86ee45979794637f@seed-3.mainnet.desmos.network
b9ae3a5871e3d9699f339b0af2e38f6095491ab3@desmos-seed.artifact-staking.io:26656
```

## State sync nodes
If you wish to bootrap a node using state sync, you can use the following nodes:
```sh
```

## Endpoints
### RPC
```
https://rpc.mainnet.desmos.network:443
```

### Web socket
```
wss://ws.mainnet.desmos.network:443
```

### gRPC
```
https://grpc.mainnet.desmos.network:443
```

### Legacy APIs
```
https://lcd.mainnet.desmos.network:443
```

### GraphQL
```
https://gql.mainnet.desmos.network/v1/graphql
```
