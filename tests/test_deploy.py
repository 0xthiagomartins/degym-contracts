from brownie import (
    DeGymToken,
    GymVoucher,
    GymProviderCertificate,
    Checkin,
    Stake,
    accounts,
)


def test_deploy():
    deployer = accounts[0]

    token = DeGymToken.deploy(1_000_000, {"from": deployer})
    assert token.name() == "DeGym Token"
    assert token.symbol() == "DGYM"

    gym_voucher = GymVoucher.deploy(token.address, {"from": deployer})
    assert gym_voucher.name() == "Gym Voucher"

    staking_contract = Stake.deploy(
        token.address, "0x..USDT_ADDRESS..", {"from": deployer}
    )
    gym_certificate = GymProviderCertificate.deploy(
        staking_contract.address, 1000, {"from": deployer}
    )
    assert gym_certificate.name() == "Gym Provider Certificate"

    checkin_contract = Checkin.deploy(
        gym_certificate.address, gym_voucher.address, {"from": deployer}
    )
    assert checkin_contract.owner() == deployer
