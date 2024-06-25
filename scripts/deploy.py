from brownie import (
    accounts,
    DeGymToken,
    GymVoucher,
    GymProviderCertificate,
    Checkin,
    Stake,
)


def main():
    # Load account
    account = accounts.load("deployment_account")

    # Deploy DeGymToken
    token = DeGymToken.deploy(1000000 * 10**18, {"from": account})
    print(f"DeGymToken deployed at {token.address}")

    # Deploy GymVoucher
    gym_voucher = GymVoucher.deploy(token.address, {"from": account})
    print(f"GymVoucher deployed at {gym_voucher.address}")

    # Deploy GymProviderCertificate
    gym_provider_certificate = GymProviderCertificate.deploy(
        token.address, 1000 * 10**18, {"from": account}
    )
    print(f"GymProviderCertificate deployed at {gym_provider_certificate.address}")

    # Deploy Checkin
    checkin = Checkin.deploy(
        gym_provider_certificate.address, gym_voucher.address, {"from": account}
    )
    print(f"Checkin deployed at {checkin.address}")

    # Deploy Stake
    stake = Stake.deploy(token.address, token.address, {"from": account})
    print(f"Stake deployed at {stake.address}")

    return token, gym_voucher, gym_provider_certificate, checkin, stake
