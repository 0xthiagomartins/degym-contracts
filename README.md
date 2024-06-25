# DeGym Smart Contracts

This repository contains the smart contracts for the DeGym project. The project includes several contracts to manage tokens, vouchers, certificates, check-ins, and staking.

## Contracts

- `DeGymToken`: ERC20 token for DeGym
- `GymVoucher`: NFT for gym memberships
- `GymProviderCertificate`: Certificates for gym providers
- `Checkin`: Contract to handle gym check-ins
- `Stake`: Staking contract for $DGYM tokens

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
    ```

2. Compile contracts:
    ```bash
    ape compile
    ```

2.1 Add Account (generate or import if not exists)
    ```bash
    ape accounts list
    ape accounts generate account_alias
    ```

2.2 Make sure your account has some testnet TARA for deploying contracts and running tests. You can use the Taraxa testnet faucet to get testnet TARA.


1. Run tests:
    ```bash
    ape test --network taraxa:testnet
    ```

2. Deploy contracts:
    ```bash
    ape run --network taraxa:testnet deploy/00_deploy_token.py
    ape run --network taraxa:testnet deploy/01_deploy_voucher.py
    ape run --network taraxa:testnet deploy/02_deploy_stake.py
    ape run --network taraxa:testnet deploy/03_deploy_gym_provider_certificate.py
    ape run --network taraxa:testnet deploy/04_deploy_checkin.py
    ```

## Configuration

Update the `ape-config.yaml` file with your specific configuration needs.
