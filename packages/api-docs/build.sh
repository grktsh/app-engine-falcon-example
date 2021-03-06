#!/bin/sh
#
# Usage: ./build.sh > openapi.yaml
#

src=$(dirname $0)/src

echo '# This file was auto-generated by build.sh.'
cat $src/base.yaml

(
    cd $src/paths
    echo 'paths:'
    for file in $(find . -name '*.yaml' | sort); do
        echo "  ${file:1:${#file}-6}:"
        sed 's/^/    /' $file
    done
)

(
    cd $src/components
    echo 'components:'
    for component in $(ls); do
        (
            cd $component
            echo "  $component:"
            for file in $(ls *.yaml); do
                echo "    ${file::${#file}-5}:"
                sed 's/^/      /' $file
            done
        )
    done
)
