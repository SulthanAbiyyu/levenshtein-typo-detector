import requests


def dataset(path: str) -> dict:
    """
    Generate dataset into dictionary, so can do random access search

    Args:
        path: path to the dataset

    Returns:
        dataset dictionary

    Raises:
        Still None
    """
    # TODO: Add file note found exception

    kbbi = requests.get(
        path).text.split("\n")
    kbbi_map = {
        **{word: "dummy_val" for word in kbbi},
    }
    return kbbi_map
