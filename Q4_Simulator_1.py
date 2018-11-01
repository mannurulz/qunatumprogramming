from cirq.google import XmonSimulator
simulator = XmonSimulator()
result = simulator.run(circuit)

print(result)