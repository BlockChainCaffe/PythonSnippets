#!/usr/bin/python3
import sys
import json
import time
import csv

from web3.auto import Web3
from web3 import IPCProvider
from web3.middleware import geth_poa_middleware
import web3

import config as cfg

#################################################################################
# GLOBALS
NONCE = 0
WALLET = Web3.toChecksumAddress(cfg.web3["wallet"])
PASSWD = cfg.web3["password"]
CC_ADD = Web3.toChecksumAddress(cfg.web3["contract-address"])
CC_ABI = ""

web3 = False
contract = False

#################################################################################
# FUNCTIONS

def getNonce():
    '''gets the NONCE to be used for the next transaction'''
    newnonce = web3.eth.getTransactionCount(WALLET)
    n = newnonce if newnonce > (NONCE+1) else NONCE+1
    print("nonce: {}".format(NONCE))
    return n


def makeTxOptions():
    '''Prepares options to be passed in the tx'''
    return {"from" : WALLET, "gas" : cfg.web3["gas"], "gasPrice" : cfg.web3["gasprice"], "nonce" :  getNonce()}


def makeTX(method,*args):
    '''makes a tx
    method is the method of the smart contract
    args are the args of the call'''

    ## Unlock Wallet
    if (web3.geth.personal.unlockAccount(WALLET,PASSWD,cfg.web3["unlockSecs"])):
        n=len(args)
        if n==1:
            tx_hash = method(args[0]).transact(makeTxOptions())
        elif n==2:
            tx_hash = method(args[0],args[1]).transact(makeTxOptions())
        elif n==3:
            tx_hash = method(args[0],args[1],args[2]).transact(makeTxOptions())
        elif n==4:
            tx_hash = method(args[0],args[1],args[2],args[3]).transact(makeTxOptions())
        elif n==5:
            tx_hash = method(args[0],args[1],args[2],args[3],args[4]).transact(makeTxOptions())
        elif n==6:
            tx_hash = method(args[0],args[1],args[2],args[3],args[4],args[5]).transact(makeTxOptions())
        else:
            print("wrong nmber of parameters")
    else:
        print("ERROR unlocking wallet")
    return False


def makeCall(method, *args):
    '''Makes a call (read) to the contract'''
    n=len(args)
    if n==1:
        return method(args[0]).call()
    elif n==2:
        return method(args[0],args[1]).call()
    elif n==3:
        return method(args[0],args[1],args[2]).call()
    elif n==4:
        return method(args[0],args[1],args[2],args[3]).call()
    elif n==5:
        return method(args[0],args[1],args[2],args[3],args[4]).call()
    else:
        return False


def main ():
    # print (contract.functions.name_of_the_function("param", param1).call())
    print (makeCall(contract.functions.name_of_function, "param", param1))


#################################################################################
# MAIN

if __name__ == "__main__" :
    # Load ABI from file
    with open(cfg.web3["abi-file"]) as f:
        CC_ABI = json.load(f)

    # Connect to RPC
    web3 = Web3(Web3.HTTPProvider(cfg.web3["provider"])) # web3 = Web3(IPCProvider(cfg.web3["ipcMiddleware"]))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Instantiate Contract
    contract = web3.eth.contract(address=CC_ADD, abi=CC_ABI)
    
    main()