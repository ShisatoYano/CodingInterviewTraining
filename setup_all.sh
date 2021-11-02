# install dependencies
sudo apt install -y build-essential libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

# download pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# update .bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# confirm pyenv was insalled
pyenv -v

# install python by pyenv
pyenv install 3.9.7
pyenv versions

# change python version at only this directory
pyenv local 3.9.7

# update .bash_profile
echo 'export PATH="$HOME/.pyenv/shims:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

# confirm python version
python --version
which python

# setup virtual environment
python -m venv env
ls env -al

# activate virtual environment
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip list