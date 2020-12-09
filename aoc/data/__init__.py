import os

def load_data():
    with open("data/data.txt") as f:
        return f.read()
