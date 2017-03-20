
upperalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    words = word.split(' ')
    res = ""
    for c in word:
        if c not in upperalpha:
            return word
    for w in words:
        for c in word:
            if c not in upperalpha:
                return w
        res += numeric(w) + " "
    return "(" + res[:-1] + ")" # needs more formatting

def numeric(w):
    "return unchanged arg if non [A-Z] chars exist in arg, else return numeric version"
    for c in w:
        if c not in upperalpha:
            return w
    "Over here, w has no non-[A-Z] chars. Proceed to numerify"
    r = ""
    l = len(w)
    if l == 1:
        return w
    r = ""
    for index, c in enumerate(w):
        r += c + '*{} + '.format(str(10**(l - index - 1)))
    return r[:-3]
