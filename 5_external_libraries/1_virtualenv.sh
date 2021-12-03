# create a new virtual environment, an isolated python environment for your project
python3 -m venv venv

source venv/bin/activate

# install an external library
pip3 install plotly==5.4.0

# use pip3 freeze to create a requirements file
pip3 freeze > requirements.txt

# to install images from the requirements file, use pip3 -r
pip3 install -r requirements.txt