from cirq.google.xmon_gates import ExpWGate
circuit = cirq.Circuit()
CZ = Exp11Gate(half_turns=1.0)
X = ExpWGate(half_turns=1.0)
circuit.append([CZ(device.qubits[0], device.qubits[1]), X(device.qubits[0])])
print(circuit)