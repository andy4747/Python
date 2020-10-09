"""
Given aaaabbbbcccdddeeefffhhhjdjfjfhd
find out how many times each letter is repeated
"""


def repetition_counter(string):
    counter = dict()
    for i in string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter


if __name__ == "__main__":
    out = repetition_counter(("aaaaassssdddffg"))
    print(out)