from ape import project, accounts


def main():
    owner = accounts.load("deployer")
    token = project.DeGymToken.deploy(1_000_000 * 10**18, sender=owner)
    usdt_token = project.DeGymToken.deploy(1_000_000 * 10**18, sender=owner)
    stake = owner.deploy(project.Stake, token.address, usdt_token.address)
    print(f"Deployed Stake at {stake.address}")
