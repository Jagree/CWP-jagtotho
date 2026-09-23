def array_of_names(dct):
    arr = []
    for key in dct:
        arr.append(key.capitalize() + " " + dct[key].capitalize())
    return arr

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))