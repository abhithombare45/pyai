import qiskit
from qiskit import QuantumCircuit, Aer, transpile
import numpy as np

# Define a simple quantum circuit (Generator)
generator = QuantumCircuit(1)
generator.ry(np.pi/4, 0)  # Apply a rotation

# Simulate the quantum circuit
simulator = Aer.get_backend("statevector_simulator")
job = qiskit.execute(generator, simulator)
result = job.result()
statevector = result.get_statevector()

# Print the generated quantum state
print("🧠 Generated Quantum State:", statevector)
