import pandas as pd
from optimizer import *
from dataset import *
from utils import *


def pre_train(text: str) -> tuple[list[str], list[str]]:
    corpus = list(set(text_cleaning(text).split()))
    kbbi_map = dataset("data\\raw\\kbbi.txt")

    print("mencari typo suspect...")
    typo_suspect = []
    for word in corpus:
        if word not in kbbi_map:
            typo_suspect.append(word)

    print("mencari possible key..")
    search_key = word_ngram_suspect(typo_suspect)
    possible_key = tolerated_word_ngram(search_key, typo_suspect, kbbi_map)

    return possible_key


def train(possible_key: list[str], typo_suspect: list[str], threshold=60) -> dict:
    suggestion = {}
    THRESHOLD = threshold

    if len(typo_suspect) == 0:
        return "Tidak ada typo"

    for typo in typo_suspect:
        similarity_word = []
        similarity_ratio = []
        for key in possible_key:
            similarity_word.append(key)
            similarity_ratio.append(levenshtein_ratio(typo, key))
        sim_df = pd.DataFrame(
            {"word": similarity_word, "similarity": similarity_ratio})
        sim_df = sim_df.sort_values(by="similarity", ascending=False)

        if all(sim_df["similarity"] < THRESHOLD):
            suggestion[typo] = ["Kata tidak ditemukan di kamus"]
        else:
            suggestion[typo] = [
                (sim_df.iloc[i]["word"], sim_df.iloc[i]["similarity"]) for i in range(3)]
        hasil = ""

        for typo, _ in suggestion.items():
            if suggestion[typo] == ["Kata tidak ditemukan di kamus"]:
                hasil += f"{typo} tidak ditemukan di kamus\n"
            else:
                hasil += f"'{typo}' dapat ditulis sebagai:\n"
                idx = 1
                for i in suggestion[typo]:
                    hasil += f"{idx}. {i[0]} ({round(i[1])} %)\n"
                    idx += 1
                hasil += "\n"

    return hasil
