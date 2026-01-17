#!/bin/bash
set -e

# Note, this step is needed because students will fork the repo
# and the directory name will change from hwrs564b_course_materials
# to hwrs564b_course_materials_<their_github_username> or similar.
cd_prefix="./hwrs564b_course_*"
dirs=( $cd_prefix )
if [ ${#dirs[@]} -eq 1 ] && [ -d "${dirs[0]}" ]; then
    cd "${dirs[0]}"
else
    echo "Error: expected exactly one directory matching $cd_prefix, found ${#dirs[@]}"
fi

# Create/update conda environment from environment.yml
echo "Creating/updating conda environment..."
conda env update --file environment.yml --prune

# Initialize conda for bash shell
echo "Initializing conda for bash shell..."
conda init

# Activate the conda environment
echo "Activating conda environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate hwrs564b

# Download MODFLOW binaries
cd ..
mkdir -p ./modflow
echo "Downloading MODFLOW binaries..."
python -c "from flopy.utils import get_modflow; get_modflow('./modflow')"

# Install Jupyter kernel
echo "Installing Jupyter kernel..."
python -m ipykernel install --user --name hwrs564b

# Clone LPR_redux repository if it doesn't exist
if [ ! -d "LPR_redux" ]; then
    echo "Cloning LPR_redux repository..."
    git clone https://github.com/mnfienen/LPR_redux.git
else
    echo "LPR_redux repository already exists, skipping clone..."
fi

echo "------------------------------------------------"
echo "Setup complete!"
echo "------------------------------------------------"