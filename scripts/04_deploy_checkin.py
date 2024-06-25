from ape import project, accounts


def main():
    owner = accounts.load("first_account")
    provider_certificate = project.GymProviderCertificate.deploy(
        1_000_000 * 10**18, sender=owner
    )
    voucher = project.GymVoucher.deploy(1_000_000 * 10**18, sender=owner)
    checkin = owner.deploy(
        project.Checkin, provider_certificate.address, voucher.address
    )
    print(f"Deployed Checkin at {checkin.address}")
