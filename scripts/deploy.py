from ape import accounts, project


def main():
    # Load the deployer account
    deployer = accounts.load("deployer")

    # Deploy the DeGymToken contract
    token = deployer.deploy(project.DeGymToken, initial_supply=1000000)

    # Deploy the GymVoucher contract
    voucher = deployer.deploy(project.GymVoucher, token.address)

    # Deploy the GymProviderCertificate contract
    certificate = deployer.deploy(
        project.GymProviderCertificate,
        staking_contract_address=token.address,
        min_stake=1000,
    )

    # Deploy the Checkin contract
    checkin = deployer.deploy(
        project.Checkin,
        provider_certificate_address=certificate.address,
        gym_voucher_address=voucher.address,
    )

    # Deploy the Stake contract
    stake = deployer.deploy(
        project.Stake, dGymToken=token.address, usdtToken=token.address
    )

    print("Contracts deployed successfully")
    print(f"Token address: {token.address}")
    print(f"Voucher address: {voucher.address}")
    print(f"Certificate address: {certificate.address}")
    print(f"Checkin address: {checkin.address}")
    print(f"Stake address: {stake.address}")
