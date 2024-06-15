import pytest
from brownie import GymAccessNFT, accounts


def test_mint_nft():
    account = accounts[0]
    nft = GymAccessNFT.deploy({"from": account})
    nft.mint(accounts[1], {"from": account})
    assert nft.ownerOf(0) == accounts[1]
