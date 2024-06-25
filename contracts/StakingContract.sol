// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract StakingContract {
    IERC20 public token;
    mapping(address => uint256) public stakes;

    constructor(address tokenAddress) {
        token = IERC20(tokenAddress);
    }

    function getStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    function stake(uint256 amount) external {
        token.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] += amount;
    }

    function unstake(uint256 amount) external {
        require(
            stakes[msg.sender] >= amount,
            "Insufficient balance to unstake"
        );
        stakes[msg.sender] -= amount;
        token.transfer(msg.sender, amount);
    }
}
