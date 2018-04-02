#!/bin/bash
# Activate virtual environment
. /appenv/bin/Activate

# Install application test requirements
pip install -r requirements_test.txt

# Run test.sh arguments
exec $@