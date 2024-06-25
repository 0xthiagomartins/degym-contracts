from ape import accounts, project
import os


def get_deployer():
    return accounts.load("first_account")


def deploy_degym_token(deployer):
    initial_supply = 1_000_000 * 10**18  # 1 million tokens
    token = deployer.deploy(project.DeGymToken, initial_supply)
    print(f"Deployed DeGymToken at {token.address}")
    return token


def deploy_voucher(deployer, fiat_address):
    voucher = deployer.deploy(project.Voucher, fiat_address)
    print(f"Deployed Voucher at {voucher.address}")
    return voucher


def deploy_stake(deployer, token, fiat_address):
    stake = deployer.deploy(project.Stake, token.address, fiat_address)
    print(f"Deployed Stake at {stake.address}")
    return stake


def deploy_provider_certificate(deployer, stake_contract):
    min_stake = 500 * 10**18  # example minimum stake amount (in $DGYM)
    provider_certificate = deployer.deploy(
        project.ProviderCertificate, stake_contract.address, min_stake
    )
    print(f"Deployed ProviderCertificate at {provider_certificate.address}")
    return provider_certificate


def deploy_checkin(deployer, voucher_contract, provider_certificate_contract):
    checkin = deployer.deploy(
        project.Checkin, provider_certificate_contract.address, voucher_contract.address
    )
    print(f"Deployed Checkin at {checkin.address}")
    return checkin


def main():
    ## setup
    deployer = get_deployer()
    token = deploy_degym_token(deployer)
    fiat_address = os.environ.get(
        "USDT_ADDRESS",
        project.DeGymToken.deploy(1_000_000 * 10**18, sender=deployer).address,
    )

    ### Contracts DEPLOY
    voucher_contract = deploy_voucher(deployer, fiat_address)
    stake_contract = deploy_stake(deployer, token, fiat_address)
    provider_certificate_contract = deploy_provider_certificate(
        deployer, stake_contract
    )
    checkin = deploy_checkin(deployer, voucher_contract, provider_certificate_contract)
    ###

    ## Logs
    print("\n=\n" * 35)
    print("Contracts deployed successfully")
    print("\n=\n" * 35)
    print(f"Token address: {token.address}")
    print(f"Voucher address: {voucher_contract.address}")
    print(f"Certificate address: {provider_certificate_contract.address}")
    print(f"Checkin address: {checkin.address}")
    print(f"Stake address: {stake_contract.address}")
