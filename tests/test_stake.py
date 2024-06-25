from brownie import Stake, DeGymToken, accounts


def test_stake():
    account = accounts[0]
    dGymToken = DeGymToken.deploy(1000000 * 10**18, {"from": account})
    usdtToken = DeGymToken.deploy(
        1000000 * 10**18, {"from": account}
    )  # Using DeGymToken as USDT for simplicity
    stake_contract = Stake.deploy(
        dGymToken.address, usdtToken.address, {"from": account}
    )

    # Stake tokens
    dGymToken.approve(stake_contract.address, 1000 * 10**18, {"from": account})
    stake_contract.stake(1000 * 10**18, True, {"from": account})
    assert stake_contract.totalStaked() == 1000 * 10**18

    # Unstake tokens
    stake_contract.unstake(500 * 10**18, {"from": account})
    assert stake_contract.totalStaked() == 500 * 10**18

    # Distribute rewards
    stake_contract.distributeRewards(account, 100 * 10**18, True, {"from": account})
    assert dGymToken.balanceOf(account) == 100 * 10**18

    stake_contract.distributeRewards(account, 100 * 10**18, False, {"from": account})
    assert usdtToken.balanceOf(account) == 100 * 10**18
