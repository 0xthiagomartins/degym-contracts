// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

interface IProviderCertificate {
    function validateCertificate(uint256 tokenId) external view returns (bool);
    function getTier(uint256 tokenId) external view returns (uint256);
}

interface IVoucher {
    function checkin(
        uint256 voucherId,
        uint256 gymId,
        uint256 dcpUsed
    ) external;
    function canAccessGym(
        uint256 voucherId,
        uint256 gymId
    ) external view returns (bool);
    function resetDailyLedger(uint256 voucherId) external;
}

contract Checkin is Ownable {
    IProviderCertificate public providerCertificate;
    IVoucher public voucher;

    event CheckinSuccessful(
        uint256 voucherId,
        uint256 certificateId,
        uint256 gymId,
        uint256 dcpUsed
    );

    constructor(address providerCertificateAddress, address voucherAddress) {
        providerCertificate = IProviderCertificate(providerCertificateAddress);
        voucher = IVoucher(voucherAddress);
    }

    function checkin(
        uint256 voucherId,
        uint256 certificateId,
        uint256 gymId
    ) public {
        require(
            providerCertificate.validateCertificate(certificateId),
            "Provider certificate is not active"
        );
        uint256 tier = providerCertificate.getTier(certificateId);
        require(
            voucher.canAccessGym(voucherId, gymId),
            "Access limit reached for today"
        );
        uint256 dcpUsed = 2 ** tier;
        voucher.checkin(voucherId, gymId, dcpUsed);
        emit CheckinSuccessful(voucherId, certificateId, gymId, dcpUsed);
    }
}
