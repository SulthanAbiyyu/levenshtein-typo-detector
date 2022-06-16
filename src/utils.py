import re


def text_cleaning(text: str) -> str:
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")
    text = text.replace("  ", " ")
    text = text.lower()
    text = re.sub(r"\[[^\]]*\]", "", text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r"\([^\)]*,[^\)]*\)", "", text)

    # remove extra white space
    text = re.sub(r'\s+', ' ', text)
    return text


def levenshtein_ratio(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_ratio(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return ((max(len(s1), len(s2)) - previous_row[-1]) / max(len(s1), len(s2))) * 100
