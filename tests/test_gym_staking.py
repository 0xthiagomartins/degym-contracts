import pytest
from brownie import GymStaking, Token, accounts, chain


def test_stake_tokens():
    token = Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts[0]})
    staking = GymStaking.deploy(token.address, {"from": accounts[0]})
    token.approve(staking.address, 1000, {"from": accounts[0]})
    staking.stake(1000, {"from": accounts[0]})
    assert staking.stakes(accounts[0]) == 1000


def test_unstake_tokens():
    token = Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts[0]})
    staking = GymStaking.deploy(token.address, {"from": accounts[0]})
    token.approve(staking.address, 1000, {"from": accounts[0]})
    staking.stake(1000, {"from": accounts[0]})
    staking.requestUnstake(500, {"from": accounts[0]})
    chain.sleep(30 * 24 * 60 * 60)  # Simulate 30 days
    staking.finalizeUnstake({"from": accounts[0]})
    assert staking.stakes(accounts[0]) == 500
