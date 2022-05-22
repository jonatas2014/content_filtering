DIR=".venv"

if [ ! -d "$DIR" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
sleep 1
pip install -r requirements.txt
FLASK_APP=app.py
flask run