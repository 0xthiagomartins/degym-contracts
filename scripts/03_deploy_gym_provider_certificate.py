from ape import project, accounts


def main():
    owner = accounts.load("deployer")
    stake_contract = project.Stake.deploy(1_000_000 * 10**18, sender=owner)
    min_stake = 500 * 10**18  # example minimum stake
    provider_certificate = owner.deploy(
        project.GymProviderCertificate, stake_contract.address, min_stake
    )
    print(f"Deployed GymProviderCertificate at {provider_certificate.address}")
