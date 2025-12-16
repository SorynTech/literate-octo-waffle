import os
from random import randint, random

def load_env_file(filepath='.env'):
    """Load variables from .env file into a dictionary"""
    env_vars = {}

    if not os.path.exists(filepath):
        return env_vars

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                # Split on first = sign
                if '=' in line:
                    key, value = line.split('=', 1)
                    # Remove quotes if present
                    value = value.strip().strip('"').strip("'")
                    env_vars[key.strip()] = value

    return env_vars


# Usage
env_vars = load_env_file()
password = env_vars.get('PASSWORD')

if password:
    print("Password found!")
else:
    print("Password not found")
#test useage
print(password)
open ("diceroll.txt",'w').close()
def d4():
    diceroll=random.randint(1,4)
    print(diceroll)
    diceroll2=str(diceroll)
    with open ("diceroll.txt",'a') as f:
        f.write(f" {diceroll2} \n")
def d6():
    diceroll=randint(1,6)
    diceroll2=str(diceroll)
    print(diceroll)
    with open ("diceroll.txt",'a') as f:
        f.write(f" {diceroll2} \n")
def d8():
    diceroll=randint(1,8)
    print(diceroll)
    diceroll2=str(diceroll)
    with open ("diceroll.txt",'a') as f:
        f.write(f" {diceroll2} \n")
def d12():
    diceroll=randint(1,12)
    print(diceroll)
    diceroll2=str(diceroll)
    with open ("diceroll.txt",'a') as f:
        f.write(f" {diceroll2} \n")
def d20():
    diceroll=randint(1,20)
    print(diceroll)
    diceroll2=str(diceroll)
    with open ("diceroll.txt",'a') as f:
        f.write(f" {diceroll2} \n")

passwordinput=input("What is the password")
passwordinput=passwordinput.strip()
if passwordinput != password:
    print("You cannot use this dice please contact soryntech")
    exit()

else:
    dicetype=input("What dice do you want to roll?")
    dicetype=dicetype.strip()
    if dicetype=="d4":
        d4()
        with open( "diceroll.txt",'a') as f:
            f.write(dicetype)
    elif dicetype=="d6":
        d6()
        with open( "diceroll.txt",'a') as f:
            f.write(dicetype)
    elif dicetype=="d8":
        d8()
        with open( "diceroll.txt",'a') as f:
            f.write(dicetype)
    elif dicetype=="d12":
        d12()
        with open( "diceroll.txt",'a') as f:
            f.write(dicetype)
    elif dicetype=="d20":
        d20()
        with open( "diceroll.txt",'a') as f:
            f.write(dicetype)
#haiii