# Sunbasket Mock API

## Testing
- Step 1: Clone this repo with the following command `git clone https://github.com/Christiantav/sunbasket`.
- Step 2: Switch directories into the repo in your terminal.
- Step 3: Create a .env file for the db connection credentials and paste in your credentials. These will be provided to you.
- Step 4: Create & activate a virtual environment in this repo. On Mac OS, the commands are as follows: Create virtual env `python3 -m venv env`, Activate virtual env `. env/bin/activate`. These commands can vary depending on your platform. Check this link for reference: [Python Doc](https://docs.python.org/3/library/venv.html)
- Step 5: Enter the command `pip3 install -r requirements.txt` followed by `export FLASK_APP=routes`
- Step 6: Enter the command `flask run`, it will start on port 5000 by default.
- Step 7: Test the route with a command in this format `curl http://localhost:5000/menu/YYYY-MM-DD/MEAL_TYPE`. An example of this request is `curl http://localhost:5000/menu/2021-03-27/MEAL_KIT`.
- Step 8: You should have an array of the available meals returned.
