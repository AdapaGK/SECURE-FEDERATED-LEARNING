import React, { useState, useEffect } from 'react';
import ClientNode from './components/ClientNode';
import GlobalModel from './components/GlobalModel';
import SecurityMonitor from './components/SecurityMonitor';
import DataPrivacyDemo from './components/DataPrivacyDemo';
import { Play, Pause, Shield, Lock } from 'lucide-react';

function App() {
  const [isTraining, setIsTraining] = useState(false);
  const [round, setRound] = useState(1);
  const [globalAccuracy, setGlobalAccuracy] = useState(70);
  const [encryptionStatus, setEncryptionStatus] = useState({
    homomorphic: true,
    differential: true,
    secure: true
  });
  
  const clients = [
    { 
      id: 1, 
      dataPoints: 1000, 
      accuracy: 75, 
      isTraining: false,
      location: 'AWS-EU',
      compliance: ['GDPR', 'HIPAA'],
      encryption: 'AES-256'
    },
    { 
      id: 2, 
      dataPoints: 1200, 
      accuracy: 78, 
      isTraining: false,
      location: 'Azure-US',
      compliance: ['HIPAA', 'SOC2'],
      encryption: 'AES-256'
    },
    { 
      id: 3, 
      dataPoints: 800, 
      accuracy: 72, 
      isTraining: false,
      location: 'GCP-ASIA',
      compliance: ['PDPA', 'ISO27001'],
      encryption: 'AES-256'
    },
    { 
      id: 4, 
      dataPoints: 1500, 
      accuracy: 80, 
      isTraining: false,
      location: 'AWS-US',
      compliance: ['HIPAA', 'SOC2'],
      encryption: 'AES-256'
    }
  ];

  useEffect(() => {
    let interval: number;
    
    if (isTraining) {
      interval = setInterval(() => {
        setRound(r => r + 1);
        setGlobalAccuracy(prev => Math.min(prev + Math.random() * 2, 98));
        setEncryptionStatus(prev => ({
          ...prev,
          secure: Math.random() > 0.1
        }));
      }, 3000);
    }
    
    return () => clearInterval(interval);
  }, [isTraining]);

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 py-12">
        <div className="mb-8 flex justify-between items-start">
          <div>
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              Secure Federated Learning System
            </h1>
            <p className="text-gray-600 max-w-2xl">
              Multi-cloud federated learning with end-to-end encryption, differential privacy, 
              and regulatory compliance. Data remains secure and private across all participating nodes.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <Shield className={`w-6 h-6 ${encryptionStatus.secure ? 'text-green-500' : 'text-red-500'}`} />
            <Lock className="w-6 h-6 text-blue-500" />
          </div>
        </div>

        <div className="mb-8 flex gap-4">
          <button
            onClick={() => setIsTraining(!isTraining)}
            className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg ${
              isTraining 
                ? 'bg-red-500 hover:bg-red-600' 
                : 'bg-blue-500 hover:bg-blue-600'
            } text-white transition-colors`}
          >
            {isTraining ? (
              <>
                <Pause className="w-5 h-5" />
                Pause Training
              </>
            ) : (
              <>
                <Play className="w-5 h-5" />
                Start Training
              </>
            )}
          </button>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <div className="grid sm:grid-cols-2 gap-6">
              {clients.map((client, index) => (
                <ClientNode
                  key={client.id}
                  {...client}
                  isTraining={isTraining && index === (round % 4)}
                />
              ))}
            </div>
            <div className="mt-6">
              <DataPrivacyDemo />
            </div>
          </div>
          
          <div className="space-y-6">
            <GlobalModel
              accuracy={Math.round(globalAccuracy * 100) / 100}
              round={round}
              clientsParticipating={isTraining ? 1 : 0}
            />
            <SecurityMonitor
              encryptionStatus={encryptionStatus}
              activeClients={clients.length}
              secureConnections={clients.length}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;