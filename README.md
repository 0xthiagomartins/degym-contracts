![alt text](assets/imgs/brand.png)

# # DeGym Smart Contracts

This repository contains the smart contracts for the DeGym project, including the token contract, voucher NFT contract, gym provider certificate contract, check-in contract, and staking contract.

## Prerequisites

- [Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)
- Python 3.6+
- Node.js

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/degym-contracts.git
cd degym-contracts
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Update the brownie-config.yaml file with your settings.

## Deployment

1. Load your account:

```bash
brownie accounts new deployment_account
```

2. Deploy the contracts:

```bash
brownie run scripts/deploy.py
```

## Testing

Run the tests:

```bash
brownie test
```

---

## Contracts

### DeGymToken

ERC20 token contract for $DGYM.

### GymVoucher

NFT contract for gym membership vouchers.

### GymProviderCertificate

Contract for issuing and validating gym provider certificates.

### Checkin

Contract for validating and recording gym check-ins.

### Stake

Contract for staking $DGYM tokens and receiving rewards.

---

## License

This project is licensed under the MIT License.