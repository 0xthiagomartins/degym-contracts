from ape import project


def test_create_voucher(voucher_contract, provider, consumer):
    consumer = consumer.address if type(consumer) != str else consumer
    initial_balance = voucher_contract.balanceOf(consumer)
    tx = voucher_contract.createVoucher(consumer, 1, 30, "UTC", sender=provider)
    tx.wait()
    assert voucher_contract.balanceOf(consumer) == initial_balance + 1
    assert voucher_contract.getVoucherDetails(0)["tier"] == 1


def test_upgrade_voucher(voucher_contract, provider, consumer):
    consumer = consumer.address if type(consumer) != str else consumer
    voucher_contract.createVoucher(consumer, 1, 30, "UTC", sender=provider).wait()
    initial_dcp = voucher_contract.getVoucherDetails(0)["remainingDCP"]
    tx = voucher_contract.upgradeVoucher(0, 2, sender=consumer, value="0.1 ether")
    tx.wait()
    assert voucher_contract.getVoucherDetails(0)["tier"] == 2
    assert voucher_contract.getVoucherDetails(0)["remainingDCP"] > initial_dcp


def test_renew_voucher(voucher_contract, provider, consumer):
    consumer = consumer.address if type(consumer) != str else consumer
    voucher_contract.createVoucher(consumer, 1, 30, "UTC", sender=provider).wait()
    initial_duration = voucher_contract.getVoucherDetails(0)["duration"]
    tx = voucher_contract.renewVoucher(0, 15, sender=consumer, value="0.05 ether")
    tx.wait()
    assert voucher_contract.getVoucherDetails(0)["duration"] == initial_duration + 15


def test_downgrade_voucher(voucher_contract, provider, consumer):
    consumer = consumer.address if type(consumer) != str else consumer
    voucher_contract.createVoucher(consumer, 2, 30, "UTC", sender=provider).wait()
    initial_tier = voucher_contract.getVoucherDetails(0)["tier"]
    tx = voucher_contract.downgradeVoucher(0, 1, sender=consumer)
    tx.wait()
    assert voucher_contract.getVoucherDetails(0)["tier"] == 1
    assert voucher_contract.getVoucherDetails(0)["tier"] < initial_tier
