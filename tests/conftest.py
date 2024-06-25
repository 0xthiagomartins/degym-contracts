import pytest, os
from ape import project, accounts


@pytest.fixture
def deployer():
    address = os.environ.get("DEPLOYER_ADDRESS")
    return accounts[address] if address else accounts[0]


@pytest.fixture
def consumer():
    address = os.environ.get("CONSUMER_ADDRESS")
    return accounts[address] if address else accounts[1]


@pytest.fixture
def provider():
    address = os.environ.get("PROVIDER_ADDRESS")
    return accounts[address] if address else accounts[2]


@pytest.fixture
def dGym_token(deployer):
    return os.environ.get("DGYM_ADDRESS", deployer.deploy(project.DeGymToken, 1000000))


@pytest.fixture
def fiat_token(deployer):
    return os.environ.get("USDT_ADDRESS", deployer.deploy(project.DeGymToken, 1000000))


@pytest.fixture
def voucher_contract(deployer, fiat_token):
    return os.environ.get(
        "VOUCHER_ADDRESS", deployer.deploy(project.GymVoucher, fiat_token)
    )


@pytest.fixture
def stake_contract(deployer, dGym_token, fiat_token):
    return os.environ.get(
        "STAKE_ADDRESS",
        deployer.deploy(project.Stake, dGym_token.address, fiat_token.address),
    )


@pytest.fixture
def gym_provider_certificate(deployer, stake_contract):
    return os.environ.get(
        "PROVIDER_CERTIFICATE_ADDRESS",
        deployer.deploy(project.GymProviderCertificate, stake_contract.address, 1000),
    )


@pytest.fixture
def checkin_contract(deployer, gym_provider_certificate, voucher_contract):
    return os.environ.get(
        "",
        deployer.deploy(
            project.Checkin, gym_provider_certificate.address, voucher_contract.address
        ),
    )
