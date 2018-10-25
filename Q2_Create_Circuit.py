# Program to create Grid Qbits
import cirq
# define the length of the grid.
length = 3
# define qubits on the grid.
qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits)
# prints 
# [GridQubit(0, 0), GridQubit(0, 1), GridQubit(0, 2), GridQubit(1, 0), GridQubit(1, 1), GridQubit(1, 2), GridQubit(2, 0), GridQubit(2, 1), GridQubit(2, 2)]

#print(criq.Circuit())

circuit = cirq.Circuit()
circuit.append(cirq.H.on(q) for q in qubits if (q.row + q.col) % 2 == 0)
circuit.append(cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1)
print(circuit)
# prints
