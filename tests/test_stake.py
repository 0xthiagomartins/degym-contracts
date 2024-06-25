from ape import accounts, project


def test_stake_tokens(stake_contract, dGym_token, owner, provider):
    provider = provider.address if type(provider) != str else provider
    initial_balance = dGym_token.balanceOf(provider)
    dGym_token.approve(stake_contract.address, 1000, sender=provider)
    tx = stake_contract.stake(1000, True, sender=provider)
    tx.wait()
    assert dGym_token.balanceOf(provider) == initial_balance - 1000
    assert stake_contract.stakes(provider)["amount"] == 1000
    assert stake_contract.stakes(provider)["isCompound"] == True


def test_unstake_tokens(stake_contract, dGym_token, owner, user1):
    provider = provider.address if type(provider) != str else provider
    dGym_token.approve(stake_contract.address, 1000, sender=user1)
    stake_contract.stake(1000, True, sender=user1).wait()
    initial_balance = dGym_token.balanceOf(user1)
    tx = stake_contract.unstake(500, sender=user1)
    tx.wait()
    assert dGym_token.balanceOf(user1) == initial_balance + 500
    assert stake_contract.stakes(user1)["amount"] == 500


def test_distribute_rewards(stake_contract, dGym_token, usdt_token, owner, provider):
    provider = provider.address if type(provider) != str else provider
    dGym_token.approve(stake_contract.address, 1000, sender=provider)
    stake_contract.stake(1000, True, sender=provider).wait()
    initial_balance = dGym_token.balanceOf(provider)
    tx = stake_contract.distributeRewards(provider, 100, True, sender=owner)
    tx.wait()
    assert dGym_token.balanceOf(provider) == initial_balance + 100
    assert stake_contract.stakes(provider)["amount"] == 1100
