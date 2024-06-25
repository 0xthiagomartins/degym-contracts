// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Stake is Ownable {
    IERC20 public dGymToken;
    IERC20 public usdtToken;

    struct StakeInfo {
        uint256 amount;
        bool isCompound;
    }

    mapping(address => StakeInfo) public stakes;
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount, bool isCompound);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(
        address indexed user,
        uint256 amount,
        bool isCompound
    );

    constructor(address _dGymToken, address _usdtToken) {
        dGymToken = IERC20(_dGymToken);
        usdtToken = IERC20(_usdtToken);
    }

    function stake(uint256 amount, bool isCompound) public {
        require(amount > 0, "Amount must be greater than 0");
        dGymToken.transferFrom(msg.sender, address(this), amount);

        stakes[msg.sender] = StakeInfo(amount, isCompound);
        totalStaked += amount;

        emit Staked(msg.sender, amount, isCompound);
    }

    function unstake(uint256 amount) public {
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        dGymToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    function distributeRewards(
        address recipient,
        uint256 amount,
        bool isCompound
    ) external onlyOwner {
        if (isCompound) {
            dGymToken.transfer(recipient, amount);
        } else {
            usdtToken.transfer(recipient, amount);
        }

        emit RewardDistributed(recipient, amount, isCompound);
    }
}
