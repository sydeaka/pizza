
## Name of new conda environment that you will create for the avpn analyses
myenv=opencv

## Set up Anaconda environment with Python version 3.6 and latest version of scipy
conda create -n $myenv python=3.6 numpy pandas xlrd jupyter ipykernel nb_conda_kernels \
matplotlib=2.0 requests seaborn

## Activate the conda environment
source activate $myenv

export PATH="/Users/sw659h/.local/bin:$PATH"

## Create kernel for the newly created environment
python -m ipykernel install --user --name $myenv --display-name "Python ($myenv)"

pip install opencv-python

## Tensorflow Object Detection API
## https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md
pip install tensorflow
pip install --user Cython
pip install --user contextlib2
pip install --user pillow
pip install --user lxml
pip install --user jupyter
pip install --user matplotlib


## http://google.github.io/proto-lens/installing-protoc.html
PROTOC_ZIP=protoc-3.3.0-osx-x86_64.zip
curl -OL https://github.com/google/protobuf/releases/download/v3.3.0/$PROTOC_ZIP
sudo unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
rm -f $PROTOC_ZIP

## Change working directory on local machine
wd=~/Documents/korelasi/computer_vision
cd $wd

## Open jupyter notebook
jupyter notebook





############## PYTHON 3.6 CODE #########################

(Run the jupyter notebook)





#########################################################







## Deactivate the conda environment
source deactivate $myenv

