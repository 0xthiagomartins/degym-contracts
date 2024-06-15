// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "./GymAccessNFT.sol";

contract GymCheckIn {
    IERC20 public token;
    GymAccessNFT public nft;
    mapping(uint => bool) public checkedIn;
    mapping(address => uint) public rewards;
    uint public rewardAmount = 1 * 10 ** 18; // 1 token

    constructor(IERC20 _token, GymAccessNFT _nft) {
        token = _token;
        nft = _nft;
    }

    function checkIn(uint tokenId) external {
        require(nft.ownerOf(tokenId) == msg.sender, "not the owner");
        require(!checkedIn[tokenId], "already checked in");
        checkedIn[tokenId] = true;
        rewards[msg.sender] += rewardAmount;
    }

    function claimRewards() external {
        uint reward = rewards[msg.sender];
        require(reward > 0, "no rewards to claim");
        token.transfer(msg.sender, reward);
        rewards[msg.sender] = 0;
    }
}
