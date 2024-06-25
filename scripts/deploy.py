from brownie import (
    DeGymToken,
    GymVoucher,
    GymProviderCertificate,
    Checkin,
    Stake,
    accounts,
)


def main():
    admin = accounts[0]

    # Deploy the token
    token = DeGymToken.deploy(1000000, {"from": admin})
    print("Token deployed at:", token.address)

    # Deploy the voucher contract
    voucher = GymVoucher.deploy(token.address, {"from": admin})
    print("Voucher deployed at:", voucher.address)

    # Deploy the staking contract
    stake = Stake.deploy(token.address, token.address, {"from": admin})
    print("Stake deployed at:", stake.address)

    # Deploy the gym provider certificate contract
    provider_certificate = GymProviderCertificate.deploy(
        stake.address, 1000, {"from": admin}
    )
    print("Provider Certificate deployed at:", provider_certificate.address)

    # Deploy the checkin contract
    checkin = Checkin.deploy(
        provider_certificate.address, voucher.address, {"from": admin}
    )
    print("Checkin deployed at:", checkin.address)
