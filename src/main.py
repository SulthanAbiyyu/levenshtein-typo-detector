import pandas as pd
from optimizer import *
from dataset import *
from utils import *
from train import *


def run(text: str) -> str:
    typo_suspect, possible_key = pre_train(text)
    suggestion = train(possible_key, typo_suspect)
    print(suggestion)


if __name__ == "__main__":
    text = input("Masukkan text: ")
    run(text)
