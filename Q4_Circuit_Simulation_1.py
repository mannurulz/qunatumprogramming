import cirq
from cirq import Circuit
from cirq.devices import GridQubit
from cirq.google import ExpWGate, Exp11Gate, XmonMeasurementGate

q0 = GridQubit(0, 0)
q1 = GridQubit(1, 0)

def basic_circuit(meas=True):
    sqrt_x = ExpWGate(half_turns=0.5, axis_half_turns=0.0)
    cz = Exp11Gate()
    yield sqrt_x(q0), sqrt_x(q1)
    yield cz(q0, q1)
    yield sqrt_x(q0), sqrt_x(q1)
    if meas:
        yield XmonMeasurementGate(key='q0')(q0), XmonMeasurementGate(key='q1')(q1)
   
circuit = Circuit()
circuit.append(basic_circuit())
print(circuit)


from cirq.google import XmonSimulator
simulator = XmonSimulator()
result = simulator.run(circuit)

print(result)


import numpy as np
circuit = Circuit()
circuit.append(basic_circuit(False))    
result = simulator.simulate(circuit, qubit_order=[q0, q1])

print(np.around(result.final_state, 3))

# Qbit & Amplitude Ordering
outside = [1, 10]
inside = [1, 2]
print(np.kron(outside, inside))

i = 0
for first in [0, 1]:
    for second in [0, 1]:
        print('amps[{}] is for first={}, second={}'.format(i, first, second))
        i += 1
# Printing result as below:
'''
(0, 0): ───X^0.5───@───X^0.5───M('q0')───
                   │
(1, 0): ───X^0.5───@───X^0.5───M('q1')───
q0=0
q1=1
[-0.5-0.j   0. -0.5j  0. -0.5j -0.5+0.j ]
[ 1  2 10 20]
amps[0] is for first=0, second=0
amps[1] is for first=0, second=1
amps[2] is for first=1, second=0
amps[3] is for first=1, second=1
'''