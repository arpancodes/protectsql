# Contribute to protectsql

Steps to install locally
1. Clone the repo
```
git clone https://github.com/arpancodes/protectsql.git
```
2. `cd` into the cloned directory and create virtual env, activate it
```
cd protectsql
python3 -m venv venv
source venv/bin/activate
```
3. Install every package from requirements.txt using `pip`
```
pip install -r reqruirements.txt
```
4. Install the protectsql package locally
```
pip install -e .
```
5. Initialise pysa configs
```
protectsql init
```

Now you should have the protectsql tool working locally, you can make your changes in a new branch and create PR!
