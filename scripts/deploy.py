from brownie import GymAccessNFT, GymStaking, GymCheckIn, Token, accounts


def main():
    account = accounts[0]
    token = Token.deploy("Test Token", "TST", 18, 1e21, {"from": account})
    nft = GymAccessNFT.deploy({"from": account})
    staking = GymStaking.deploy(token.address, {"from": account})
    check_in = GymCheckIn.deploy(token.address, nft.address, {"from": account})
    return nft, staking, check_in, token
