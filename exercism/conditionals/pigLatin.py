def translate(text):
    def _translate(word):
        if word[0] in "aeiou" or word.startswith("xr") or word.startswith("yt"):
            return word + "ay"

        if word.startswith("squ"):
            return word[3:] + "squay"
        if word.startswith("qu"):
            return word[2:] + "quay"

        for consonant in ["sch", "thr", "ch", "th"]:
            if word.startswith(consonant):
                return word[len(consonant) :] + consonant + "ay"

        if "y" in word and word.index("y") > 0:
            y_index = word.index("y")
            return word[y_index:] + word[:y_index] + "ay"

        return word[1:] + word[0] + "ay"

    return " ".join([_translate(word) for word in text.split()])
