import torch
import numpy as np
from typing import List, Dict
from client import FederatedClient

class FederatedServer:
    def __init__(self):
        self.clients: List[FederatedClient] = []
        self.global_model = None
        self.round = 0
        
    def add_client(self, client: FederatedClient):
        """Register a new client"""
        self.clients.append(client)
        print(f"Client {client.client_id} from {client.location} registered")
        
    def initialize_global_model(self):
        """Initialize global model parameters"""
        # Simple linear model for demonstration
        self.global_model = {
            'weights': torch.randn(10, 5),
            'bias': torch.randn(5)
        }
        
    def aggregate_models(self, client_updates: List[Dict[str, torch.Tensor]]) -> Dict[str, torch.Tensor]:
        """Secure aggregation of client models"""
        aggregated_model = {}
        
        # Simple FedAvg algorithm with secure aggregation
        for param_name in self.global_model.keys():
            # Stack all client updates for the current parameter
            stacked_updates = torch.stack([
                update[param_name] for update in client_updates
            ])
            
            # Compute secure average (FedAvg)
            aggregated_model[param_name] = torch.mean(stacked_updates, dim=0)
            
        return aggregated_model
    
    def train_round(self) -> Dict[str, float]:
        """Execute one round of federated training"""
        self.round += 1
        client_updates = []
        compliance_status = []
        
        # Collect updates from each client
        for client in self.clients:
            # Verify client compliance
            client_compliance = client.verify_compliance()
            compliance_status.append(client_compliance)
            
            if all(client_compliance.values()):
                # Train on client and get model updates
                updates = client.train_local_model(self.global_model)
                client_updates.append(updates)
        
        # Aggregate model updates
        if client_updates:
            self.global_model = self.aggregate_models(client_updates)
        
        # Calculate training metrics
        metrics = {
            'round': self.round,
            'participants': len(client_updates),
            'compliance_rate': sum(all(c.values()) for c in compliance_status) / len(self.clients)
        }
        
        return metrics