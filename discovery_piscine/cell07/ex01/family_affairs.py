def find_the_redheads(dct):
    arr = []
    for key in dct:
        if dct[key] == "red":
            arr.append(key)
    return arr

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))