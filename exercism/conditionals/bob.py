def response1(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."


# Second Verison

def bob_response2(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    return "Whatever."


# Thrid version

def response3(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if not hey_bob:
        return "Fine. Be that way!"
    return "Whatever."
