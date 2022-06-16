def dataset(path: str) -> dict:
    kbbi = open(path, 'rb').read().lower().decode('utf-8').split("\r\n")
    kbbi_map = {
        **{word: "dummy_val" for word in kbbi},
    }
    return kbbi_map
