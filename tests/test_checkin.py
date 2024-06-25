from brownie import Checkin, GymVoucher, GymProviderCertificate, DeGymToken, accounts


def test_checkin():
    account = accounts[0]
    dGymToken = DeGymToken.deploy(1000000 * 10**18, {"from": account})
    gym_provider_certificate = GymProviderCertificate.deploy(
        dGymToken.address, 1000 * 10**18, {"from": account}
    )
    gym_voucher = GymVoucher.deploy(dGymToken.address, {"from": account})
    checkin_contract = Checkin.deploy(
        gym_provider_certificate.address, gym_voucher.address, {"from": account}
    )

    # Stake tokens and issue a certificate to the gym provider
    dGymToken.approve(
        gym_provider_certificate.address, 1000 * 10**18, {"from": account}
    )
    dGymToken.transfer(
        gym_provider_certificate.address, 1000 * 10**18, {"from": account}
    )
    gym_provider_certificate.issueCertificate(account, 1, {"from": account})

    # Create a voucher
    gym_voucher.createVoucher(account, 1, 30, "UTC", {"from": account})

    # Perform a check-in
    voucher_id = gym_voucher.tokenOfOwnerByIndex(account, 0)
    certificate_id = gym_provider_certificate.tokenOfOwnerByIndex(account, 0)
    checkin_contract.checkin(voucher_id, certificate_id, {"from": account})

    # Validate the voucher's remaining DCP
    details = gym_voucher.getVoucherDetails(voucher_id)
    assert details[2] < 2**1  # remainingDCP should be less than initial
