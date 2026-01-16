#!/bin/bash
set -e

echo "------------------------------------------------"
echo `pwd`
echo "------------------------------------------------"

cd_prefix="./hwrs564b_course_*"
dirs=( $cd_prefix )
if [ ${#dirs[@]} -eq 1 ] && [ -d "${dirs[0]}" ]; then
    cd "${dirs[0]}"
else
    echo "Error: expected exactly one directory matching $cd_prefix, found ${#dirs[@]}"
fi


echo "------------------------------------------------"
echo `pwd`
echo "------------------------------------------------"

uv venv
uv sync
source ./.venv/bin/activate
cd ..
mkdir -p ./modflow
python -c "from flopy.utils import get_modflow; get_modflow('./modflow')"
python -m ipykernel install --user --name hwrs564b
