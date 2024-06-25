import pytest, os
from ape import project, accounts


@pytest.fixture
def owner():
    return accounts[0]


@pytest.fixture
def consumer():
    return accounts[1]


@pytest.fixture
def provider():
    return accounts[2]


@pytest.fixture
def dGym_token(owner):
    return os.environ.get("DGYM_ADDRESS", owner.deploy(project.DeGymToken, 1000000))


@pytest.fixture
def fiat_token(owner):
    return os.environ.get("USDT_ADDRESS", owner.deploy(project.DeGymToken, 1000000))


@pytest.fixture
def voucher_contract(owner, fiat_token):
    return os.environ.get("", owner.deploy(project.GymVoucher, fiat_token))


@pytest.fixture
def stake_contract(owner, dGym_token, fiat_token):
    return os.environ.get(
        "", owner.deploy(project.Stake, dGym_token.address, fiat_token.address)
    )


@pytest.fixture
def gym_provider_certificate(owner, stake_contract):
    return os.environ.get(
        "", owner.deploy(project.GymProviderCertificate, stake_contract.address, 1000)
    )


@pytest.fixture
def checkin_contract(owner, gym_provider_certificate, voucher_contract):
    return os.environ.get(
        "",
        owner.deploy(
            project.Checkin, gym_provider_certificate.address, voucher_contract.address
        ),
    )
