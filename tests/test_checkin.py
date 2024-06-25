import pytest
from brownie import Checkin, GymProviderCertificate, GymVoucher, DeGymToken, accounts


@pytest.fixture
def token():
    return DeGymToken.deploy(1000000, {"from": accounts[0]})


@pytest.fixture
def provider_certificate(token):
    return GymProviderCertificate.deploy(token.address, 1000, {"from": accounts[0]})


@pytest.fixture
def voucher(token):
    return GymVoucher.deploy(token.address, {"from": accounts[0]})


@pytest.fixture
def checkin(provider_certificate, voucher):
    return Checkin.deploy(
        provider_certificate.address, voucher.address, {"from": accounts[0]}
    )


def test_successful_checkin(checkin, provider_certificate, voucher, token, accounts):
    token.transfer(accounts[1], 2000, {"from": accounts[0]})
    token.approve(voucher.address, 2000, {"from": accounts[1]})
    voucher.createVoucher(accounts[1], 3, 30, "UTC", {"from": accounts[0]})
    provider_certificate.issueCertificate(accounts[2], 3, {"from": accounts[0]})
    checkin.checkin(0, 0, {"from": accounts[1]})
    assert voucher.getVoucherDetails(0)["remainingDCP"] == 7
