import brownie
from brownie import config, network, FlashLoanArbitrage
from scripts.helper_scripts import get_account, toWei, fromWei, approve_erc20, FORKED_BLOCHCHAINS
from scripts.get_weth import get_weth

ETHERSCAN_TX_URL = "https://kovan.etherscan.io/tx/{}"

weth_token = config["networks"][network.show_active()]["weth-token"]
dai_token = config["networks"][network.show_active()]["dai-token"]

uni_router_address = config["networks"][network.show_active()]["uniswap-router"]
sushi_router_address = config["networks"][network.show_active()]["sushiswap-router"]
aave_address_provider = config["networks"][network.show_active()]["provider"]

def deploy():

    account = get_account()

    if network.show_active() in FORKED_BLOCHCHAINS:
        get_weth(account, 10)
    
    arbitrage = FlashLoanArbitrage.deploy(
        aave_address_provider,
        uni_router_address,
        sushi_router_address,
        weth_token,
        dai_token,
        {"from": account}
    )

    amount = toWei(5)

    approve_erc20(weth_token, arbitrage.address, amount, account)

    deposit_tx = arbitrage.deposit(amount, {"from": account})
    deposit_tx.wait(1)

    weth_balance = arbitrage.getERC20Balance(weth_token)
    print("amount deposited: ", fromWei(weth_balance))

    flash_tx = arbitrage.flashloan['address,uint'](weth_token, toWei(20), {"from": account})
    flash_tx.wait(1)

    print("View your flashloan tx here: " + ETHERSCAN_TX_URL.format(flash_tx.txid))



        

def main():
    deploy()