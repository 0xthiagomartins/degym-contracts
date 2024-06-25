from ape import project, accounts


def main():
    owner = accounts.load("first_account")  # deployer
    initial_supply = 1_000_000 * 10**18  # 1 million tokens
    token = owner.deploy(project.DeGymToken, initial_supply)
    print(f"Deployed DeGymToken at {token.address}")
