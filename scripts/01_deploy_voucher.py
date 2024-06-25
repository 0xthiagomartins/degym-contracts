from ape import project, accounts
import os


def main():
    owner = accounts.load("first_account")
    stable_token_address = os.environ.get(
        "USDT_ADDRESS",
        project.DeGymToken.deploy(1_000_000 * 10**18, sender=owner).address,
    )
    voucher = owner.deploy(project.GymVoucher, stable_token_address)
    print(f"Deployed GymVoucher at {voucher.address}")
