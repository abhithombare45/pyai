from qiskit import Aer
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.circuit.library import ZZFeatureMap
import numpy as np

# Define a Quantum Feature Map
feature_map = ZZFeatureMap(feature_dimension=2, reps=2)

# Define Quantum Kernel
qkernel = QuantumKernel(feature_map=feature_map, quantum_instance=Aer.get_backend("qasm_simulator"))

# Generate simple training data (XOR problem)
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])  # XOR labels

# Train Quantum SVM
qsvc = QSVC(quantum_kernel=qkernel)
qsvc.fit(X_train, y_train)

# Predict using Quantum Kernel SVM
prediction = qsvc.predict([[0, 1]])
print("📊 Quantum SVM Prediction:", prediction)

