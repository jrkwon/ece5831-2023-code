# import and_gate as ag

# x1 = 1
# x2 = 0

# print(f'The output of {x1} AND {x2} is {ag.and_gate(x1, x2)}')

import logic_gate as lg

logic_gate = lg.LogicGate()

logic_gate.and_gate(1, 0)
logic_gate.print_output('AND')

logic_gate.or_gate(1, 0)
logic_gate.print_output('OR')