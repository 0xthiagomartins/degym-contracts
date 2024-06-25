// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

interface IProviderCertificate {
    function checkCertificate(
        uint256 certificateId
    ) external view returns (uint256, uint256, bool);
}

interface IVoucher {
    function checkin(uint256 tokenId, uint256 tier) external;
}

contract Checkin is Ownable {
    IProviderCertificate public providerCertificate;
    IVoucher public voucher;

    event CheckinSuccessful(
        uint256 voucherId,
        uint256 certificateId,
        uint256 tier
    );

    constructor(address providerCertificateAddress, address voucherAddress) {
        providerCertificate = IProviderCertificate(providerCertificateAddress);
        voucher = IVoucher(voucherAddress);
    }

    function checkin(uint256 voucherId, uint256 certificateId) public {
        (uint256 tier, , bool isActive) = providerCertificate.checkCertificate(
            certificateId
        );
        require(isActive, "Provider certificate is not active");

        voucher.checkin(voucherId, tier);
        emit CheckinSuccessful(voucherId, certificateId, tier);
    }
}
