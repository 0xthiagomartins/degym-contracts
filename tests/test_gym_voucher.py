from brownie import GymVoucher, DeGymToken, accounts


def test_gym_voucher():
    account = accounts[0]
    dGymToken = DeGymToken.deploy(1000000 * 10**18, {"from": account})
    gym_voucher = GymVoucher.deploy(dGymToken.address, {"from": account})

    # Create a voucher
    gym_voucher.createVoucher(account, 1, 30, "UTC", {"from": account})
    assert gym_voucher.balanceOf(account) == 1

    voucher_id = gym_voucher.tokenOfOwnerByIndex(account, 0)
    details = gym_voucher.getVoucherDetails(voucher_id)
    assert details[0] == 1  # tier
    assert details[1] == 30  # duration
    assert details[2] == 2**1  # remainingDCP
    assert details[3] > 0  # lastReset
    assert details[4] == "UTC"  # timezone

    # Upgrade the voucher
    gym_voucher.upgradeVoucher(voucher_id, 2, {"from": account, "value": 10**18})
    details = gym_voucher.getVoucherDetails(voucher_id)
    assert details[0] == 2  # new tier

    # Renew the voucher
    gym_voucher.renewVoucher(voucher_id, 30, {"from": account, "value": 10**18})
    details = gym_voucher.getVoucherDetails(voucher_id)
    assert details[1] == 60  # new duration

    # Downgrade the voucher
    gym_voucher.downgradeVoucher(voucher_id, 1, {"from": account})
    details = gym_voucher.getVoucherDetails(voucher_id)
    assert details[0] == 1  # downgraded tier
