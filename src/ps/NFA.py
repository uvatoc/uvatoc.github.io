epsilon = "\u03b5"

class NFA:
    
    def __init__(self, states=set(), alphabet=set(), delta={}, start="", finals=set()):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.start = start
        self.finals = finals
        self.delta_domain = [(state, char) for state in states for char in alphabet]
        self.chars_seen = ""
        self.active = {start}
        self.epsilon_spread()
    
    def add_transition(self, state, character, destination):
        """ Adds a new destination for a state-character pair,
        works regardless of if there was already a previous
        destination.
        """
        if (state, character) in self.delta:
            self.delta[(state, character)].add(destination)
        else:
            self.delta[(state, character)] = {destination}
    
    def epsilon_spread(self):
        """ Activates all states reachable from an active state
        by only epsilon-transitions.
        """
        expanded = True
        while expanded:
            expanded = False
            additional_active = set()
            for state in self.active:
                if not (state, epsilon) in self.delta.keys():
                    continue
                for dest in self.delta[(state,epsilon)]:
                    expanded = expanded or not dest in self.active
                    additional_active.add(dest)
            self.active.update(additional_active)
            
    def return_value(self):
        """ If the NFA stops here, what does it return?
        """
        for state in self.active:
            if state in self.finals:
                return True
        return False
        
    
    def step(self, c):
        """Take a transition on a single character
        """
        next_active = set()
        for state in self.active:
            if (state, c) in self.delta:
                next_active.update(self.delta[(state, c)])
        self.active = next_active
        self.epsilon_spread()
        self.chars_seen += c
        return self.return_value()
    
    def reset(self):
        """ Resets the nfa to start another execution
        """
        self.active = {self.start}
        self.epsilon_spread()
        self.chars_seen = ""
        return self.return_value()
    
    def execute(self, input_string):
        """Run the nfa on an entire input string"""
        result = self.return_value()
        for c in input_string:
            result = self.step(c)
        self.reset()
        return result
    
    def __str__(self):
        display = "Start state: " + self.start + "\n"
        if len(self.active) == 0:
            curr_state = 'empty set'
        else:
            curr_state = str(self.active)
        display += "Current state: " + curr_state + "\n"
        display += "delta function: \n"
        for tup in self.delta.keys():
            display += "\t" + str(tup) + " -> " + str(self.delta[tup]) + "\n"
        display += "Final states: \n"
        for state in self.finals:
            display += "\t" + state + "\n"
        return display
    
    def toDot(self):
        '''
        * Prints out a description of the automaton in dot,
        * which is a graph specification language.
        * I recommend going to this url to convert it into
        * an image: https://dreampuf.github.io/GraphvizOnline/
        '''
        print("digraph G {")
        
        start_shape = ""
        if (self.start in self.finals):
            start_shape = "doubleoctagon"
        else:
            start_shape = "octagon"

        print("node [shape = " + start_shape + "]; " + self.start + ";")
        
        double_circled = "node [shape = doublecircle];"
        additional_finals = False
        for s in self.finals:
            if s == self.start:
                continue
            double_circled += " " + s
            additional_finals = True
        if additional_finals:
            print(double_circled + ";")
        
        single_circled = "node [shape = circle];"
        additional_states = False
        for s in self.states:
            if s == self.start or s in self.finals:
                continue
            single_circled += " " + s
            additional_states = True
        if additional_states:
            print(single_circled)
        
        for source in self.states:
            for dest in self.states:
                matching = ""
                for c in self.alphabet | {epsilon}:
                    if ((source, c) in self.delta) and (dest in self.delta[(source, c)]):
                        matching += c + ','
                if len(matching) > 0:
                    transition = source + " -> " + dest + " [ label = \"" + matching[:-1] + "\" ];"
                    print(transition)
        print("}")

def merge(nfa1, nfa2, suffix1 = "_1", suffix2 = "_2"):
    """
    creates a new nfa from two source nfas. This new nfa has all the states
    and transitions from the original 2 nfas (with distinct suffixes added
    to each state label to guarantee unique names). The start state is set
    as the start state from the first nfa given. The nfa has no final
    states.
    """
    states = set()
    finals = set()
    for state in nfa1.states:
        states.add(state + suffix1)
    for state in nfa1.finals:
        states.add(state + suffix1)
    for state in nfa2.states:
        states.add(state + suffix2)
    for state in nfa2.finals:
        states.add(state + suffix2)
    alphabet = nfa1.alphabet | nfa2.alphabet
    delta = {}
    for match, destinations in nfa1.delta.items():
        state, char = match
        match = (state + suffix1, char)
        delta[match] = set()
        for dest in destinations:
            delta[match].add(dest + suffix1)
    for match, destinations in nfa2.delta.items():
        state, char = match
        match = (state + suffix2, char)
        delta[match] = set()
        for dest in destinations:
            delta[match].add(dest + suffix2)
    start = nfa1.start + suffix1
    return NFA(states, alphabet, delta, start, finals)
        

def union(nfa1, nfa2, suffix1="_1", suffix2="_2"):
    """ creates a new nfa whose language is the
    union of the given nfas'. A different suffix is added
    onto then end of each nfa's states' label to make it
    more likely that state labels are unique.
    """
    merged = merge(nfa1, nfa2, suffix1, suffix2)
    merged.states.add("new")
    merged.start = "new"
    merged.add_transition("new", epsilon, nfa1.start + suffix1)
    merged.add_transition("new", epsilon, nfa2.start + suffix2)
    for state in nfa1.finals:
        merged.finals.add(state + suffix1)
    for state in nfa2.finals:
        merged.finals.add(state + suffix2)
    return merged

def concat(nfa1, nfa2,  suffix1="_1", suffix2="_2"):
    """ creates a new nfa whose language is the
    concatenation of the given nfas'. A different suffix is added
    onto then end of each nfa's states' label to make it
    more likely that state labels are unique.
    """
    merged = merge(nfa1, nfa2, suffix1, suffix2)
    merged.start = nfa1.start + suffix1
    for state in nfa1.finals: 
        state += suffix1
        merged.add_transition(state, epsilon, nfa2.start + suffix2)
    for state in nfa2.finals:
        merged.finals.add(state + suffix2)
    return merged
    
def copy_nfa(nfa1, suffix=""):
    """ creates a new nfa whose language is the
    the same as the given nfa's. A different suffix is added
    onto then end of each state's label to make it
    more likely that state labels are unique.
    """
    states = set()
    for state in nfa1.states:
        states.add(state + suffix)
    alphabet = set(nfa1.alphabet)
    delta = {}
    for match, dest in nfa1.delta.items():
        new_match = (match[0] + suffix, match[1])
        delta[new_match] = set()
        for state in dest:
            delta[new_match].add(state + suffix)
            
    start = nfa1.start + suffix
    finals = set()
    for state in nfa1.finals:
        finals.add(state + suffix)
    return NFA(states, alphabet, delta, start, finals)

def kleene(nfa1, suffix=""):
    """ creates a new nfa whose language is the
    the kleene start of the given nfa's. A different suffix is added
    onto then end of each state's label to make it
    more likely that state labels are unique.
    """
    copy = copy_nfa(nfa1, suffix)
    #eps_state = 'eps_state' + suffix
    new_start = 'new_start' + suffix
    for final in nfa1.finals:
        copy.add_transition(final  + suffix, epsilon, copy.start)
    #copy.states.add(eps_state)
    copy.states.add(new_start)
    copy.add_transition(new_start, epsilon, copy.start)
    copy.finals.add(new_start)
    copy.start = new_start
    #copy.add_transition(new_start, epsilon, eps_state)
    #copy.finals.add(eps_state)
    return copy
