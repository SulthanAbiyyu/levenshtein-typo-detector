import pandas as pd


def word_ngram(text: str) -> list:
    unigram = [t for t in text]
    trigram = [list(unigram[i:i+3]) for i in range(len(unigram)-2)]
    trigram_join = [''.join(t) for t in trigram]
    ngram = trigram_join
    return list(set(ngram))


def word_ngram_suspect(typo_suspect: list[str]) -> list:
    return [word_ngram(gram) for gram in typo_suspect]


def tolerated_word_ngram(search_key: list[str], typo_suspect: list[str], kbbi_map: dict, tolerated_len=2) -> list:
    possible_key = []
    idx = 0
    for i in search_key:
        for kb in kbbi_map.keys():
            for j in i:
                if j in kb and (len(kb) <= tolerated_len + len(typo_suspect[idx])) and (len(kb) >= tolerated_len - len(typo_suspect[idx])):
                    possible_key.append(kb)
        idx += 1

    return possible_key
