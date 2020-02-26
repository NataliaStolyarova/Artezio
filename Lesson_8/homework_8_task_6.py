"""Pattern finds repetitive words in sentence."""
import re


def find_repeat():
    """Finds the word which repeats four or more times."""
    text = r"""What is what your what name what?"""
    match = re.findall(r'(\b\w{2,}\b)(?=.*\1){4,}', text, flags=re.IGNORECASE)
    print(match)


find_repeat()
