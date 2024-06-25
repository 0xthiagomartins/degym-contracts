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

2.1 Add Account (if not exists)
    ```bash
    ape accounts list
    ape accounts generate account_alias
    ```

3. Run tests:
    ```bash
    ape test --network taraxa:testnet
    ```

4. Deploy contracts:
    ```bash
    ape run deploy/00_deploy_token.py
    ape run deploy/01_deploy_voucher.py
    ape run deploy/02_deploy_stake.py
    ape run deploy/03_deploy_gym_provider_certificate.py
    ape run deploy/04_deploy_checkin.py
    ```

## Configuration

Update the `ape-config.yaml` file with your specific configuration needs.
