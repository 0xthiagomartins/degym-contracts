// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

interface IGymProviderCertificate {
    function checkCertificate(
        uint256 certificateId
    ) external view returns (uint256, uint256, bool);
}

interface IGymVoucher {
    function checkin(uint256 tokenId, uint256 gymTier) external;
}

contract Checkin is Ownable {
    IGymProviderCertificate public providerCertificate;
    IGymVoucher public gymVoucher;

    event CheckinSuccessful(
        uint256 voucherId,
        uint256 certificateId,
        uint256 tier
    );

    constructor(address providerCertificateAddress, address gymVoucherAddress) {
        providerCertificate = IGymProviderCertificate(
            providerCertificateAddress
        );
        gymVoucher = IGymVoucher(gymVoucherAddress);
    }

    function checkin(uint256 voucherId, uint256 certificateId) public {
        (uint256 gymTier, , bool isActive) = providerCertificate
            .checkCertificate(certificateId);
        require(isActive, "Gym certificate is not active");

        gymVoucher.checkin(voucherId, gymTier);
        emit CheckinSuccessful(voucherId, certificateId, gymTier);
    }
}
