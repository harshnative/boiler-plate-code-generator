# set up virtual env
virtualenv myvirtual

sleep 3

# activate virtual env
. myvirtual/bin/activate


# install jupyter notebook and related packages
pip install ipykernel

pip install numpy

pip install pandas

pip install nbconvert

pip install notebook

# install and activate dark theme
pip install jupyterthemes

jt -t onedork