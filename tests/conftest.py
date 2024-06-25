import pytest
from ape import project, accounts


@pytest.fixture
def owner():
    return accounts[0]


@pytest.fixture
def user1():
    return accounts[1]


@pytest.fixture
def dGym_token(owner):
    return owner.deploy(project.DeGymToken, 1000000)


@pytest.fixture
def usdt_token(owner):
    return owner.deploy(
        project.DeGymToken, 1000000
    )  # Assuming USDT is another ERC20 token


@pytest.fixture
def voucher_contract(owner, dGym_token):
    return owner.deploy(
        project.GymVoucher, "0x063F255689b00A877F6be55109b3ECA24e266809"  # HERB
    )


@pytest.fixture
def gym_provider_certificate(owner):
    staking_contract_address = "0xYourStakingContractAddressHere"
    return owner.deploy(project.GymProviderCertificate, staking_contract_address, 1000)


@pytest.fixture
def checkin_contract(owner, gym_provider_certificate, voucher_contract):
    return owner.deploy(
        project.Checkin, gym_provider_certificate.address, voucher_contract.address
    )


@pytest.fixture
def stake_contract(owner, dGym_token, usdt_token):
    return owner.deploy(project.Stake, dGym_token.address, usdt_token.address)
