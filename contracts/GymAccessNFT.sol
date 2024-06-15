// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract GymAccessNFT is ERC721 {
    uint public nextTokenId;
    address public admin;

    constructor() ERC721("GymAccessNFT", "GANFT") {
        admin = msg.sender;
    }

    function mint(address to) external {
        require(msg.sender == admin, "only admin can mint");
        _safeMint(to, nextTokenId);
        nextTokenId++;
    }
}
