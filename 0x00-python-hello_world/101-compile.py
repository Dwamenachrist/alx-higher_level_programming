#!/bin/bash

# Check if PYFILE environment variable is set
if [[ -z "$PYFILE" ]]; then
    echo "Error: PYFILE environment variable is not set."
    exit 1  
fi

# Check if the Python source file exists
if [[ ! -f "$PYFILE" ]]; then
    echo "Error: File '$PYFILE' not found."
    exit 1
fi

python3 -m compileall -b $PYFILE