#!/bin/bash

echo "======  input  ======"
echo "Arg 0 ($0)"
echo "Arg 1 ($1)"

echo "======  pycodestyle  ======"
pycodestyle $1

echo "======  pyflakes  ======"
pyflakes $1

echo "======  pylint  ======"
#pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --reports=n $1
#pylint -f parseable -r n $1
pylint_import=$(cat << PYTHON
import sys
import pkg_resources

__requires__ = "pylint"
sys.exit(
    pkg_resources.load_entry_point("pylint", "console_scripts", "pylint")()
)
PYTHON
)
python3 -c "$pylint_import" -f parseable -r n $1
