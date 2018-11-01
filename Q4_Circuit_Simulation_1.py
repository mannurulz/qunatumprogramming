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