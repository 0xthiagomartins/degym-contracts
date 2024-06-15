// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WellnessProgram {
    struct Program {
        uint id;
        string name;
        string description;
        uint duration; // in days
        uint reward;
    }

    Program[] public programs;
    mapping(address => mapping(uint => bool)) public userEnrollments;
    mapping(address => mapping(uint => uint)) public userProgress;

    function createProgram(
        string memory _name,
        string memory _description,
        uint _duration,
        uint _reward
    ) external {
        programs.push(
            Program({
                id: programs.length,
                name: _name,
                description: _description,
                duration: _duration,
                reward: _reward
            })
        );
    }

    function enrollInProgram(uint _programId) external {
        require(_programId < programs.length, "Program does not exist");
        userEnrollments[msg.sender][_programId] = true;
        userProgress[msg.sender][_programId] = 0;
    }

    function completeDay(uint _programId) external {
        require(
            userEnrollments[msg.sender][_programId],
            "Not enrolled in this program"
        );
        require(
            userProgress[msg.sender][_programId] <
                programs[_programId].duration,
            "Program already completed"
        );

        userProgress[msg.sender][_programId]++;
    }

    function claimReward(uint _programId) external {
        require(
            userEnrollments[msg.sender][_programId],
            "Not enrolled in this program"
        );
        require(
            userProgress[msg.sender][_programId] ==
                programs[_programId].duration,
            "Program not yet completed"
        );

        // Implement reward mechanism, e.g., transferring tokens
        userEnrollments[msg.sender][_programId] = false;
        userProgress[msg.sender][_programId] = 0;
    }
}
