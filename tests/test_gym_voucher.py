import pytest
from brownie import GymVoucher, DeGymToken, accounts, chain


@pytest.fixture
def token():
    return DeGymToken.deploy(1000000, {"from": accounts[0]})


@pytest.fixture
def voucher(token):
    return GymVoucher.deploy(token.address, {"from": accounts[0]})


def test_create_voucher(voucher, accounts):
    voucher.createVoucher(accounts[1], 3, 30, "UTC", {"from": accounts[0]})
    assert voucher.balanceOf(accounts[1]) == 1


def test_upgrade_voucher(voucher, token, accounts):
    voucher.createVoucher(accounts[1], 3, 30, "UTC", {"from": accounts[0]})
    token.transfer(accounts[1], 1000, {"from": accounts[0]})
    token.approve(voucher.address, 1000, {"from": accounts[1]})
    voucher.upgradeVoucher(0, 4, {"from": accounts[1]})
    assert voucher.getVoucherDetails(0)["tier"] == 4


def test_renew_voucher(voucher, token, accounts):
    voucher.createVoucher(accounts[1], 3, 30, "UTC", {"from": accounts[0]})
    token.transfer(accounts[1], 1000, {"from": accounts[0]})
    token.approve(voucher.address, 1000, {"from": accounts[1]})
    voucher.renewVoucher(0, 30, {"from": accounts[1]})
    assert voucher.getVoucherDetails(0)["duration"] == 60


def test_downgrade_voucher(voucher, accounts):
    voucher.createVoucher(accounts[1], 3, 30, "UTC", {"from": accounts[0]})
    voucher.downgradeVoucher(0, 2, {"from": accounts[1]})
    assert voucher.getVoucherDetails(0)["tier"] == 2
