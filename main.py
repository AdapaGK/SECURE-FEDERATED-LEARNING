import numpy as np
import torch
from client import FederatedClient
from server import FederatedServer

def simulate_federated_learning():
    # Initialize server
    server = FederatedServer()
    
    # Create simulated clients in different regions
    clients = [
        FederatedClient("client1", "EU-WEST"),
        FederatedClient("client2", "US-EAST"),
        FederatedClient("client3", "ASIA-EAST")
    ]
    
    # Register clients with server
    for client in clients:
        server.add_client(client)
    
    # Initialize global model
    server.initialize_global_model()
    
    # Simulate data for each client
    for client in clients:
        # Generate synthetic data
        data = np.random.randn(100, 10)  # 100 samples, 10 features
        labels = np.random.randint(0, 5, 100)  # 5 classes
        client.load_data(data, labels)
    
    # Run federated training for 5 rounds
    print("\nStarting Federated Learning Training:")
    print("=====================================")
    
    for _ in range(5):
        metrics = server.train_round()
        print(f"\nRound {metrics['round']}:")
        print(f"Participating Clients: {metrics['participants']}")
        print(f"Compliance Rate: {metrics['compliance_rate']*100:.1f}%")

if __name__ == "__main__":
    simulate_federated_learning()