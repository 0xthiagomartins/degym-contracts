// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Stake is Ownable {
    IERC20 public daoToken;
    IERC20 public fiatToken;

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

    constructor(address _daoToken, address _fiatToken) {
        daoToken = IERC20(_daoToken);
        fiatToken = IERC20(_fiatToken);
    }

    function stake(uint256 amount, bool isCompound) public {
        require(amount > 0, "Amount must be greater than 0");
        daoToken.transferFrom(msg.sender, address(this), amount);

        stakes[msg.sender] = StakeInfo(amount, isCompound);
        totalStaked += amount;

        emit Staked(msg.sender, amount, isCompound);
    }

    function unstake(uint256 amount) public {
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        daoToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    function distributeRewards(
        address recipient,
        uint256 amount,
        bool isCompound
    ) external onlyOwner {
        if (isCompound) {
            daoToken.transfer(recipient, amount);
        } else {
            fiatToken.transfer(recipient, amount);
        }

        emit RewardDistributed(recipient, amount, isCompound);
    }
}
