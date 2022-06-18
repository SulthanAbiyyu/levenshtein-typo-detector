# Levenshtein Typo Detector

This project is assigned by my data structure and algorithm course lecturer, Pak Imam Cholissodin, S.Si., M.Kom. as a final project.
The main task basically is to implement a searching algorithm and determine if the input word is present in KBBI (Kamus Besar Bahasa Indonesia) or not. If the input word is not present in KBBI, it means that the input is a typo.

I think that the way a word is classified as a typo is too broad. There are several possibilities:

1. The input word is in fact typo
2. The input word is just not in the formal form of Bahasa Indonesia

To solve this problem I tried many methods, such as cosine similarity, euclidean distance, and Levenshtein ratio (See
[experiment](https://github.com/SulthanAbiyyu/levenshtein-typo-detector/blob/master/notebooks/experiments.ipynb)). Turns out that the Levenshtein ratio is the best method to solve the problem. By getting the ratio score, we can extract correction suggestions from the similarity ratio score.

## Flowchart

![flowchart](https://i.imgur.com/hb1eMrx.png)

## Optimizations

KBBI dataset has at least ±72k rows, of course, it will be so slow if we calculate Levenshtein ratio for all words linearly. To optimize this, I eliminate a lot of impossible keys with two methods: word_ngram and tolerated_word_ngram.

### word_ngram

This method basically is just like a normal n-gram (in my case the best configuration is to use trigram only) but at the word level.

**Example:**

```plain
"biyu" -> ["biy", "iyu"]
"ubed" -> ["ube", "bed"]
```

This list will be used for eliminating all keys that is doesn't contain the list's elements. This optimization could decrease the amount of possible keys from ±72k to ±13k possibilities.

### tolerated_word_ngram

This is an improvisation from word_ngram. The main different is when eliminating keys, it will even eliminating keys that contain the list's element but not in tolerated word length. The lower the threshold, the stricter the elimination

**Example:**

```plain
typo_suspect = ["biyu"]
possible_key = ["biy", "iyu"]
tolerated_length_threshold = 2
upper_bound_tolerence = typo_suspect[0].length + tolerated_length_threshold
lower_bound_tolerence = typo_suspect[0].length - tolerated_length_threshold

key = [words in kbbi that contain possible_key
       && words length is in between upper and lower bound]
```

With this optimization, the amount of possible keys decrease from ±72k to ±11k
