from ape import project, accounts
import os


def main():
    owner = accounts.load("first_account")
    token_address = os.environ.get(
        "DGYM_ADDRESS",
        project.DeGymToken.deploy(1_000_000 * 10**18, sender=owner).address,
    )
    stable_token_address = os.environ.get(
        "USDT_ADDRESS",
        project.DeGymToken.deploy(1_000_000 * 10**18, sender=owner).address,
    )
    stake = owner.deploy(project.Stake, token_address, stable_token_address)
    print(f"Deployed Stake at {stake.address}")
