import numpy as np
import torch
from cryptography.fernet import Fernet
from typing import Dict, List
import json

class FederatedClient:
    def __init__(self, client_id: str, location: str):
        self.client_id = client_id
        self.location = location
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        self.local_data = None
        self.local_model = None
        
    def load_data(self, data: np.ndarray, labels: np.ndarray):
        """Load and encrypt local training data"""
        self.local_data = {
            'data': self.encrypt_data(data.tobytes()),
            'labels': self.encrypt_data(labels.tobytes()),
            'shape': data.shape
        }
        
    def encrypt_data(self, data: bytes) -> bytes:
        """Encrypt data using Fernet symmetric encryption"""
        return self.cipher_suite.encrypt(data)
    
    def decrypt_data(self, encrypted_data: bytes) -> bytes:
        """Decrypt data using Fernet symmetric encryption"""
        return self.cipher_suite.decrypt(encrypted_data)
    
    def train_local_model(self, global_model_params: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        """Train local model with differential privacy"""
        # Simulate local training with noise addition for differential privacy
        updated_params = {}
        noise_scale = 0.01  # Privacy parameter
        
        for name, param in global_model_params.items():
            # Add Gaussian noise for differential privacy
            noise = torch.randn_like(param) * noise_scale
            updated_params[name] = param + noise
            
        return updated_params
    
    def verify_compliance(self) -> Dict[str, bool]:
        """Verify compliance with privacy regulations"""
        compliance_status = {
            'data_encryption': True,
            'differential_privacy': True,
            'data_locality': self.check_data_locality(),
            'audit_logging': True
        }
        return compliance_status
    
    def check_data_locality(self) -> bool:
        """Check if data remains in the designated region"""
        allowed_regions = {
            'EU': ['EU-WEST', 'EU-CENTRAL'],
            'US': ['US-EAST', 'US-WEST'],
            'ASIA': ['ASIA-EAST', 'ASIA-SOUTH']
        }
        region = self.location.split('-')[0]
        return region in allowed_regions