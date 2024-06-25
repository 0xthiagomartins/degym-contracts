import pytest
from brownie import DeGymToken, Stake, accounts

@pytest.fixture
def token():
    return DeGymToken.deploy(1000000, {"from": accounts[0]})

@pytest.fixture
def usdt():
    return DeGymToken.deploy(1000000, {"from": accounts[0]})

@pytest.fixture
def stake(token, usdt):
    return Stake.deploy(token.address, usdt.address, {"from": accounts[0]})

def test_stake(stake, token, accounts):
    token.transfer(accounts[1], 2000, {"from": accounts[0]})
    token.approve(stake.address, 2000, {"from": accounts[1]})
    stake.stake(2000, True, {"from": accounts[1]})
    assert stake.totalStaked() == 2000

def test_unstake(stake, token, accounts):
    token.transfer(accounts[1], 2000, {"from": accounts[0]})
    token.approve(stake.address, 2000, {"from": accounts[1]})
    stake.stake(2000, True, {"from": accounts[1]})
    stake.unstake(1000, {"from": accounts[1]})
    assert stake.totalStaked() == 1000

def test_distribute_rewards(stake, token, usdt, accounts):
    token.transfer(accounts[1], 2000, {"from": accounts[0]})
    token.approve(stake.address, 2000, {"from": accounts[1]})
    stake.stake(2000, True, {"from": accounts[1]})
    stake.distributeRewards(accounts[1], 100, True, {"from": accounts[0]})
    assert token.balanceOf(accounts[1]) == 100
    stake.distributeRewards(accounts[1], 50, False, {"from": accounts[0]})
    assert usdt.balanceOf(accounts[1]) == 50
