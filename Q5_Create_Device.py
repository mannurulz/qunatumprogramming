import cirq
from cirq.devices import GridQubit
from cirq.google import XmonGate
class Xmon10Device(cirq.Device):

  def __init__(self):
      self.qubits = [GridQubit(i, 0) for i in range(10)]

  def duration_of(self, operation):
      # Wouldn't it be nice if everything took 10ns?
      return cirq.Duration(nanos=10)

  def validate_operation(self, operation):
      if (not isinstance(operation, cirq.GateOperation) or
              not isinstance(operation.gate, XmonGate)):
          raise ValueError('{!r} is not an XmonGate'.format(operation))
      if len(operation.qubits) == 2:
          p, q = operation.qubits
          if not p.is_adjacent(q):
            raise ValueError('Non-local interaction: {}'.format(repr(operation)))


  def validate_scheduled_operation(self, schedule, scheduled_operation):
      self.validate_operation(scheduled_operation.operation)

  def validate_circuit(self, circuit):
      for moment in circuit:
          for operation in moment.operations:
              self.validate_operation(operation)

  def validate_schedule(self, schedule):
      for scheduled_operation in schedule.scheduled_operations:
          self.validate_scheduled_operation(schedule, scheduled_operation)
print("Done")