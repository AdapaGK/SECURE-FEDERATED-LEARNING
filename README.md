# Secure Federated Learning System

This project implements a secure federated learning system for multi-cloud environments with privacy-preserving features and compliance monitoring.

## Features

- Encrypted data storage and transmission
- Differential privacy in model training
- Compliance verification for data locality
- Secure model aggregation
- Multi-cloud support with region awareness

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the simulation:
```bash
python src/main.py
```

## Architecture

- `client.py`: Implements secure client-side operations
- `server.py`: Manages federated learning coordination
- `main.py`: Simulation runner

## Security Features

- Data Encryption: Uses Fernet symmetric encryption
- Differential Privacy: Adds noise to model updates
- Compliance Checking: Verifies data locality and privacy requirements
- Secure Aggregation: Implements secure model averaging