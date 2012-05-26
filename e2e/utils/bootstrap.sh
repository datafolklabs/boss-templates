#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Not running in a virtualenv???  That's just crazy... I'm out."
    exit 1
fi

# Setup the core first
pushd src/@module@.core
    pip install -r requirements.txt
    python setup.py develop
popd
    
for src in $(echo src/*); do
    if [ "$src" != 'src/@module@.core' ]; then
        pushd $src
            pip install -r requirements.txt
            python setup.py develop
        popd
    fi
done
