# Implements a Quantum-Classical Classifier (Quantum Neural Network).
# Uses PennyLane to create a quantum circuit for classification tasks.
# Next Step: Train this model using gradient descent for AI tasks.

import pennylane as qml
import numpy as np

# Define a 2-qubit quantum device
dev = qml.device("default.qubit", wires=2)

# Define a quantum circuit
@qml.qnode(dev)
def quantum_circuit(weights, x):
    qml.RY(x[0], wires=0)
    qml.RY(x[1], wires=1)
    qml.Rot(weights[0], weights[1], weights[2], wires=0)
    qml.Rot(weights[3], weights[4], weights[5], wires=1)
    return qml.expval(qml.PauliZ(0))

# Generate random weights
weights = np.random.randn(6)

# Sample input data
x = np.array([0.5, -0.3])

# Get quantum prediction
prediction = quantum_circuit(weights, x)
print("🔮 Quantum Prediction:", prediction)

