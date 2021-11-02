# setup virtual environment
python -m venv env
ls env -al

# activate virtual environment
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip list