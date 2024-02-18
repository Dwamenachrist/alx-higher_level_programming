#!/usr/bin/python3
import dis

# Load the compiled bytecode from 'hidden_4.pyc'
with open('hidden_4.pyc', 'rb') as f:
    bytecode = f.read()[16:]  # Skip the bytecode header

# Disassemble the bytecode
for instruction in dis.get_instructions(bytecode):
    if instruction.opname == 'LOAD_NAME':
        # Ignore names starting with underscores
        if not instruction.argval.startswith('__'):
            print(instruction.argval)
