from brownie import GymProviderCertificate, DeGymToken, accounts


def test_gym_provider_certificate():
    account = accounts[0]
    dGymToken = DeGymToken.deploy(1000000 * 10**18, {"from": account})
    staking_contract = dGymToken  # Assuming staking contract for simplicity
    gym_provider_certificate = GymProviderCertificate.deploy(
        staking_contract.address, 1000 * 10**18, {"from": account}
    )

    # Stake tokens to be eligible for certificate
    dGymToken.approve(
        gym_provider_certificate.address, 1000 * 10**18, {"from": account}
    )
    staking_contract.transfer(
        gym_provider_certificate.address, 1000 * 10**18, {"from": account}
    )

    # Issue a certificate
    gym_provider_certificate.issueCertificate(account, 1, {"from": account})
    assert gym_provider_certificate.balanceOf(account) == 1

    certificate_id = gym_provider_certificate.tokenOfOwnerByIndex(account, 0)
    is_valid = gym_provider_certificate.validateCertificate(certificate_id)
    assert is_valid

    # Revoke the certificate
    gym_provider_certificate.revokeCertificate(certificate_id, {"from": account})
    is_valid = gym_provider_certificate.validateCertificate(certificate_id)
    assert not is_valid
