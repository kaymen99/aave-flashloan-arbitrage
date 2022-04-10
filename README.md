# aave-flashloan-arbitrage
This a smart contract for performing arbitrage with AAVE flashloan between Uniswap &amp; Sushiswap

## Features:
The smart contract FlashloanArbitrage alows a user to deposit WETH and make an arbitrage between the 2 exchanges and ensures that the operation is always profitable by checking that the price difference is always higher than the payed fees

## Usage:

### Installation & Setup:

1. Installing Brownie: Brownie is a python framework for smart contracts development,testing and deployments. It's quit like [HardHat](https://hardhat.org) but it uses python for writing test and deployements scripts instead of javascript.
   Here is a simple way to install brownie.
   ```
    pip install --user pipx
    pipx ensurepath
    # restart your terminal
    pipx install eth-brownie
   ```
   Or if you can't get pipx to work, via pip (it's recommended to use pipx)
    ```
    pip install eth-brownie
    ```
   
3. Clone the repo:
   ```sh
   git clone https://github.com/Aymen1001/aave-flashloan-arbitrage.git
   cd aave-flashloan-arbitrage
   ```

4. Set your environment variables:

   To be able to deploy to real testnets you need to add your PRIVATE_KEY (You can find your PRIVATE_KEY from your ethereum wallet like metamask) and the infura project Id (just create an infura account it's free) to the .env file:
   ```
   PRIVATE_KEY=<PRIVATE_KEY>
   WEB3_INFURA_PROJECT_ID=<< YOUR INFURA PROJECT ID >>
   ```
### How to run:

To start an arbitrage on the mainnet fork (for testing purposes only, you can also use the kovan testnet) you just need to run the command :
   ```sh
   brownie run scripts/flashloan_arbitrage.py --network=mainnet-fork
   ```
   ```

