// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./GymRegistration.sol";

contract GymAccessNFT is ERC721 {
    uint public nextTokenId;
    address public admin;
    GymRegistration public gymRegistration;

    constructor(
        address gymRegistrationAddress
    ) ERC721("GymAccessNFT", "GANFT") {
        admin = msg.sender;
        gymRegistration = GymRegistration(gymRegistrationAddress);
    }

    function mint(address to, address gymAddress) external payable {
        GymRegistration.Gym memory gym = gymRegistration.getGymDetails(
            gymAddress
        );
        require(
            msg.value >= gym.minPrice,
            "Payment below the gym's minimum price"
        );
        _safeMint(to, nextTokenId);
        nextTokenId++;
    }

    function withdrawFunds() external {
        require(msg.sender == admin, "Only admin can withdraw funds");
        payable(admin).transfer(address(this).balance);
    }
}
