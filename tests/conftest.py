import pytest, os
from ape import project, accounts


def __get_contract(Contract, key, deployer, contract, *args, **kwargs):
    address = os.environ.get(key)
    contract = (
        Contract[address] if address else deployer.deploy(contract, *args, **kwargs)
    )
    return contract


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
def voucher_contract(Contract, deployer, fiat_token):
    return __get_contract(
        Contract, "VOUCHER_ADDRESS", deployer, project.GymVoucher, fiat_token
    )


@pytest.fixture
def stake_contract(Contract, deployer, dGym_token, fiat_token):
    return __get_contract(
        Contract,
        "STAKE_ADDRESS",
        deployer,
        project.Stake,
        dGym_token.address,
        fiat_token.address,
    )


@pytest.fixture
def gym_provider_certificate(Contract, deployer, stake_contract):
    return __get_contract(
        Contract,
        "PROVIDER_CERTIFICATE_ADDRESS",
        deployer,
        project.GymProviderCertificate,
        stake_contract.address,
        1000,
    )


@pytest.fixture
def checkin_contract(Contract, deployer, gym_provider_certificate, voucher_contract):
    return __get_contract(
        Contract,
        "CHECKIN_ADDRESS",
        deployer,
        project.Checkin,
        gym_provider_certificate.address,
        voucher_contract.address,
    )
