# Program to create Grid Qbits
import cirq
# define the length of the grid.
length = 3
# define qubits on the grid.
qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits)
# prints 
# [GridQubit(0, 0), GridQubit(0, 1), GridQubit(0, 2), GridQubit(1, 0), GridQubit(1, 1), GridQubit(1, 2), GridQubit(2, 0), GridQubit(2, 1), GridQubit(2, 2)]

#Creating a Hadamard Gate

circuit = cirq.Circuit()
circuit.append(cirq.H.on(q) for q in qubits if (q.row + q.col) % 2 == 0)
circuit.append(cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1)
print(circuit)
# prints

# Creating Moment

for i, m in enumerate(circuit):
    print('Moment {}: {}'.format(i, m))
# prints 
# Moment 0: H((0, 0)) and H((0, 2)) and H((1, 1)) and H((2, 0)) and H((2, 2))
# Moment 1: X((0, 1)) and X((1, 0)) and X((1, 2)) and X((2, 1))

circuit = cirq.Circuit()
circuit.append([cirq.H.on(q) for q in qubits if (q.row + q.col) % 2 == 0],
               strategy=cirq.InsertStrategy.EARLIEST)
circuit.append([cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1],
               strategy=cirq.InsertStrategy.EARLIEST)
print("Printing Circuit with even & odd")
print(circuit)
# (0, 0): ───H───
#
# (0, 1): ───X───
#
# (0, 2): ───H───
#
# (1, 0): ───X───
#
# (1, 1): ───H───
#
# (1, 2): ───X───
#
# (2, 0): ───H───
#
# (2, 1): ───X───
#
# (2, 2): ───H───