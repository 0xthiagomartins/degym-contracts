from ape import project, accounts


def main():
    owner = accounts.load("deployer")
    token = project.DeGymToken.deploy(1_000_000 * 10**18, sender=owner)
    voucher = owner.deploy(project.GymVoucher, token.address)
    print(f"Deployed GymVoucher at {voucher.address}")
