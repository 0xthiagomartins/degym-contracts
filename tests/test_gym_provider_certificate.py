from ape import accounts, project


def test_issue_certificate(provider_certificate_contract, deployer, provider):
    provider = provider.address if type(provider) != str else provider
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=provider).wait()
    initial_balance = provider_certificate_contract.balanceOf(provider)
    tx = provider_certificate_contract.issueCertificate(provider, 2, sender=deployer)
    tx.wait()
    assert provider_certificate_contract.balanceOf(provider) == initial_balance + 1
    assert provider_certificate_contract.certificates(0)["tier"] == 2


def test_validate_certificate(provider_certificate_contract, deployer, provider):
    provider = provider.address if type(provider) != str else provider
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=provider).wait()
    provider_certificate_contract.issueCertificate(provider, 2, sender=deployer).wait()
    assert provider_certificate_contract.validateCertificate(0) == True


def test_revoke_certificate(provider_certificate_contract, deployer, provider):
    provider = provider.address if type(provider) != str else provider
    stake_contract_address = provider_certificate_contract.stakingContract()
    stake_contract = project.Stake.at(stake_contract_address)
    stake_contract.stake(1000, True, sender=provider).wait()
    provider_certificate_contract.issueCertificate(provider, 2, sender=deployer).wait()
    provider_certificate_contract.revokeCertificate(0, sender=deployer).wait()
    assert provider_certificate_contract.validateCertificate(0) == False
