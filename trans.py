from main import to_cyrillic, to_latin, transliterate

import regex

def latinOrcyrillic(text):
    check = bool(regex.search(r'\p{Iscyrillic}', text))
    if check == True:
        result = to_latin(text)
    else:
        result = to_cyrillic(text)
    return result           

