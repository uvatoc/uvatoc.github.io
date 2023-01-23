import NFA
    
def insertConcat(regex):
    """ It was easier for me to parse the regex if I had a operation for concatenation
    rather than just "smushing" the things together.
    Here I add a . everyhwere there should be a concatenation."""
    noConcatAfter = ['(', '|', '.']
    noConcatBefore = [')', '|', '.', '*']
    newRegex = ""
    newRegex += regex[0]
    for i in range(1, len(regex)):
        newRegexEnd = newRegex[-1]
        nextChar = regex[i]
        if not newRegexEnd in noConcatAfter and not nextChar in noConcatBefore:
            newRegex += "."
        newRegex += nextChar
    return newRegex

default_op = '\u2202' # the default is to a character that I wouldn't expect you to ever really want. I picked a random unicode character. Basically, I just need to know when I didn't find an outer-most operation, which I do by checking if the default ever changed.
def tokenize(regex):
    """This is really the most complicated part of building the regex engine.
    This is what takes the regex and converts it into the prefix representation.
    Essentially, it checks that parentheses are balanced, and if so then it 
    finds which operation is not contained in any parenteses (if one exists).
    If there are multiple, it does union, then concatenation, then star
    (this is the reverse of order of operations).
    If there is no out-most operation, this means that the entire regex
    was wrapped in outer-most parentheses, so it removes them."""
    if len(regex) == 1:
        return ('singleton', regex)
    if len(regex) == 0:
        return ('singleton', epsilon)
        
    regex = insertConcat(regex)
    op = default_op
    parens = 0
    currExpr = ""
    tokens = []
    
    # this for loop checks for union
    for i in range(len(regex)):
        c = regex[i]
        if c == '(':
            parens += 1
        elif c == ')':
            parens -= 1
        if parens < 0:
            print("Unbalanced Parentheses!")
            return None
        if c == '|' and parens == 0:
            #we're doing a union
            op = '|'
            tokens.append(tokenize(currExpr))
            currExpr = ""
        else:
            currExpr += c
    if parens != 0:
        print("Unbalanced Parentheses!")
        return None
    if op != default_op:
        tokens.append(tokenize(currExpr))
        return (op, tokens)
    currExpr = ""
    tokens = []
    # this for loop checks for concatenation
    for i in range(len(regex)):
        c = regex[i]
        if c == '(':
            parens += 1
        elif c == ')':
            parens -= 1
        if c == '.' and parens == 0:
            #we're doing a union
            op = '.'
            tokens.append(tokenize(currExpr))
            currExpr = ""
        else:
            currExpr += c
    if op != default_op:
        tokens.append(tokenize(currExpr))
        return (op, tokens)
    if regex[-1] == '*':
        op = '*'
        currExpr = regex[:-1]
        tokens.append(tokenize(currExpr))
        return (op, tokens)
    currExpr = regex[1:-1]
    return tokenize(currExpr)

def singleton_NFA(c):
    """
    Creates a NFA which returns 1 for
    only a single string of length 1
    """
    if c == NFA.epsilon:
        states = {'start'}
        alphabet = set()
        start = 'start'
        finals = {'start'}
        delta = {}
        return NFA.NFA(states, alphabet, delta, start, finals)
    states = {'start', 'end'}
    alphabet = {c}
    finals = {'end'}
    delta = {('start', c):{'end'}}
    start = 'start'
    return NFA.NFA(states, alphabet, delta, start, finals)
    
def token_depth(token):
    """
    determines the "depth" of a regex 
    prefix tree. Used for guaranteeing
    unique node labels.
    """
    if token[0] == 'singleton':
        return 1
    else:
        depth = 0
        for operand in token[1][1:]:
            if token_depth(operand) > depth:
                depth = token_depth(operand)
        return depth + 1
    
def token_to_NFA(token):
    """
    converts a regex prefix tree into
    an equivalent NFA.
    """
    operation = token[0]
    depth = token_depth(token)
    if operation == 'singleton':
        return singleton_NFA(token[1])
    if operation == '|':
        nfa = NFA.copy_nfa(token_to_NFA(token[1][0]), "_d" + str(depth) + "o0")
        for i in range(1, len(token[1])):
            operand = token[1][i]
            nfa = NFA.union(nfa, token_to_NFA(operand), "", "_d" + str(depth) + "o" + str(i))
        return nfa
    elif operation == '.':
        nfa = token_to_NFA(token[1][0])
        for i in range(1, len(token[1])):
            operand = token[1][i]
            nfa = NFA.concat(nfa, token_to_NFA(operand), "", "_d" + str(depth) + "o" + str(i))
        return nfa
    elif operation == '*':
        return NFA.kleene(token_to_NFA(token[1][0]), "_d" + str(depth))


def regex_to_NFA(regex):
    """
    converts a regex from a 
    string to a prefix tree
    representation, then 
    converts the regex into
    a NFA.
    """
    token = tokenize(regex)
    return token_to_NFA(token)


