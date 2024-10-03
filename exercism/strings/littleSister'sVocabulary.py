def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return prefix + " :: " + " :: ".join([prefix + i for i in vocab_words[1:]])


def remove_suffix_ness(word):
    new_word = word[:-4]
    if new_word.endswith("i"):
        new_word = new_word[:-1]
        new_word = new_word + "y"
        return new_word
    else:
        return new_word



def adjective_to_verb(sentence, index):
    adjective = sentence.split()[index]
    if adjective[-1] == "." or adjective[-1] == "!" or adjective[-1] == ",":
        adjective = adjective[:-1]
        verb = adjective + "en"
    else:
        verb = adjective + "en"
    return verb

