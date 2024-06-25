from ape import accounts, project


def test_checkin_successful(
    checkin_contract,
    provider_certificate_contract,
    voucher_contract,
    owner,
    consumer,
    provider,
):
    consumer = consumer.address if type(consumer) != str else consumer
    provider = provider.address if type(provider) != str else provider
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=provider).wait()
    provider_certificate_contract.issueCertificate(provider, 2, sender=owner).wait()
    voucher_contract.createVoucher(consumer, 2, 30, "UTC", sender=owner).wait()
    tx = checkin_contract.checkin(0, 0, sender=consumer)
    tx.wait()
    assert tx.events["CheckinSuccessful"].voucherId == 0
    assert tx.events["CheckinSuccessful"].certificateId == 0
    assert tx.events["CheckinSuccessful"].tier == 2
