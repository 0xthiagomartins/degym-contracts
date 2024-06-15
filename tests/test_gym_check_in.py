import pytest
from brownie import GymCheckIn, GymAccessNFT, Token, accounts


def test_check_in_with_nft():
    token = Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts[0]})
    nft = GymAccessNFT.deploy({"from": accounts[0]})
    check_in = GymCheckIn.deploy(token.address, nft.address, {"from": accounts[0]})
    nft.mint(accounts[1], {"from": accounts[0]})
    check_in.checkIn(0, {"from": accounts[1]})
    assert check_in.rewards(accounts[1]) == 1 * 10**18


def test_claim_rewards():
    token = Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts[0]})
    nft = GymAccessNFT.deploy({"from": accounts[0]})
    check_in = GymCheckIn.deploy(token.address, nft.address, {"from": accounts[0]})
    nft.mint(accounts[1], {"from": accounts[0]})
    check_in.checkIn(0, {"from": accounts[1]})
    check_in.claimRewards({"from": accounts[1]})
    assert check_in.rewards(accounts[1]) == 0
