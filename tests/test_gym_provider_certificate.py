import pytest
from brownie import GymProviderCertificate, DeGymToken, accounts


@pytest.fixture
def token():
    return DeGymToken.deploy(1000000, {"from": accounts[0]})


@pytest.fixture
def staking_contract(token):
    return Stake.deploy(token.address, {"from": accounts[0]})


@pytest.fixture
def certificate(staking_contract):
    return GymProviderCertificate.deploy(
        staking_contract.address, 1000, {"from": accounts[0]}
    )


def test_issue_certificate(certificate, staking_contract, token, accounts):
    token.transfer(accounts[1], 2000, {"from": accounts[0]})
    token.approve(staking_contract.address, 2000, {"from": accounts[1]})
    staking_contract.stake(2000, True, {"from": accounts[1]})
    certificate.issueCertificate(accounts[1], 3, {"from": accounts[0]})
    assert certificate.balanceOf(accounts[1]) == 1


def test_validate_certificate(certificate, staking_contract, token, accounts):
    token.transfer(accounts[1], 2000, {"from": accounts[0]})
    token.approve(staking_contract.address, 2000, {"from": accounts[1]})
    staking_contract.stake(2000, True, {"from": accounts[1]})
    certificate.issueCertificate(accounts[1], 3, {"from": accounts[0]})
    assert certificate.validateCertificate(0) == True


def test_revoke_certificate(certificate, accounts):
    certificate.issueCertificate(accounts[1], 3, {"from": accounts[0]})
    certificate.revokeCertificate(0, {"from": accounts[0]})
    assert certificate.validateCertificate(0) == False
