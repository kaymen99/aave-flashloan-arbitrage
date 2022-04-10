from brownie import config, network, accounts, Contract, interface
from web3 import Web3


LOCAL_BLOCKCHAINS = ["ganache-local", "development"]

FORKED_BLOCHCHAINS = ["mainnet-fork", "mainnet-fork-dev"]

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

def get_account(index=None):
    if network.show_active() in LOCAL_BLOCKCHAINS or network.show_active() in FORKED_BLOCHCHAINS:
        if index is not None:
            return accounts[index]
        else:
            return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def toWei(amount):
    return Web3.toWei(amount, "ether")

def fromWei(amount):
    return Web3.fromWei(amount, "ether")


def get_contract(_contract, contract_address):
    contract = Contract.from_abi(_contract._name, contract_address, _contract.abi)

def approve_erc20(erc20_address, spender, amount, account):
    erc20 = interface.IERC20(erc20_address)
    approve_tx = erc20.approve(spender, amount, {"from": account})
    approve_tx.wait(1)

    print("----- Erc20 approved -----")