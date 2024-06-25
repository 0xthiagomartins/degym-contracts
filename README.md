![alt text](assets/imgs/brand.png)

# # DeGym Smart Contracts

This repository contains the smart contracts for the DeGym project, including the token contract, voucher NFT contract, gym provider certificate contract, check-in contract, and staking contract.

## Setup

1. Install Ape and dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Compile the contracts:
    ```bash
    ape compile
    ```

3. Run tests:
    ```bash
    ape test
    ```

4. Deploy contracts:
    ```bash
    ape run deploy/deploy_degym_token.py
    ape run deploy/deploy_gym_voucher.py
    ape run deploy/deploy_gym_provider_certificate.py
    ape run deploy/deploy_checkin.py
    ape run deploy/deploy_stake.py
    ```

## Contracts

### DeGymToken.sol
ERC20 token for the DeGym project.

### GymVoucher.sol
NFT contract for gym membership vouchers with functionality for upgrades, renewals, and downgrades.

### GymProviderCertificate.sol
NFT contract for issuing certificates to gym providers based on their staked DGYM tokens.

### Checkin.sol
Contract for validating and recording gym check-ins.

### Stake.sol
Contract for staking DGYM tokens and receiving rewards in DGYM or USDT.
---

## License

This project is licensed under the MIT License.