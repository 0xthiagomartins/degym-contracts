// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract GymStaking {
    IERC20 public token;
    mapping(address => uint) public stakes;
    mapping(address => uint) public unstakeRequests;
    mapping(address => uint) public unstakeTimestamps;
    address public admin;
    uint public unstakeDelay = 30 days;

    constructor(IERC20 _token) {
        token = _token;
        admin = msg.sender;
    }

    function stake(uint amount) external {
        require(amount > 0, "amount should be greater than zero");
        token.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] += amount;
    }

    function requestUnstake(uint amount) external {
        require(stakes[msg.sender] >= amount, "not enough staked");
        unstakeRequests[msg.sender] = amount;
        unstakeTimestamps[msg.sender] = block.timestamp + unstakeDelay;
    }

    function finalizeUnstake() external {
        require(
            block.timestamp >= unstakeTimestamps[msg.sender],
            "unstake delay not passed"
        );
        uint amount = unstakeRequests[msg.sender];
        require(amount > 0, "no unstake request found");
        token.transfer(msg.sender, amount);
        stakes[msg.sender] -= amount;
        unstakeRequests[msg.sender] = 0;
        unstakeTimestamps[msg.sender] = 0;
    }

    function cancelUnstake() external {
        unstakeRequests[msg.sender] = 0;
        unstakeTimestamps[msg.sender] = 0;
    }
}
