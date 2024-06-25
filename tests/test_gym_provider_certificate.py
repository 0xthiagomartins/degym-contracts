from ape import accounts, project


def test_issue_certificate(provider_certificate_contract, owner, user1):
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=user1).wait()
    initial_balance = provider_certificate_contract.balanceOf(user1)
    tx = provider_certificate_contract.issueCertificate(user1, 2, sender=owner)
    tx.wait()
    assert provider_certificate_contract.balanceOf(user1) == initial_balance + 1
    assert provider_certificate_contract.certificates(0)["tier"] == 2


def test_validate_certificate(provider_certificate_contract, owner, user1):
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=user1).wait()
    provider_certificate_contract.issueCertificate(user1, 2, sender=owner).wait()
    assert provider_certificate_contract.validateCertificate(0) == True


def test_revoke_certificate(provider_certificate_contract, owner, user1):
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=user1).wait()
    provider_certificate_contract.issueCertificate(user1, 2, sender=owner).wait()
    provider_certificate_contract.revokeCertificate(0, sender=owner).wait()
    assert provider_certificate_contract.validateCertificate(0) == False
