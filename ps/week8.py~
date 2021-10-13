import regex
import NFA


    
def example1(the_string):
    """ A function that determines whether the string matches (a|b|c)*d"""
    the_regex = "(a|b|c)*d"  # string representing a regex
    equivalent_nfa = regex.regex_to_NFA(the_regex) # convert the regex into a NFA
    return equivalent_nfa.execute(the_string)  # give a string as input to NFA

### Example usage of example1 function ###
### Once you read and understand what's going on, comment out this block of code before moving forward ###
matches_ex1 = "aaabcacaccaaacccbd"
doesnt_match_ex1 = "daacacc"
this_is_true = example1(matches_ex1)
this_is_false = example1(doesnt_match_ex1)
print(this_is_true)
print(this_is_false)



def zerostar_onestar_zerostar():
    """Prints the description of an NFA which computes the
    language 0*1*. To see the NFA, copy-paste the console
    output into this tool: https://dreampuf.github.io/GraphvizOnline/"""
    the_regex = "(a|b|c)*d"
    nfa = regex.regex_to_NFA(the_regex)
    nfa.toDot()


### Uncomment this to print the description of the zerostar_onestar_zerostar nfa ###
#zerostar_onestar_zerostar()

### Uncomment each to print the description of a few more NFAs. ###
### Verify that you follow how the construction is working ###
#regex.regex_to_NFA('a').toDot()
#regex.regex_to_NFA('ab').toDot()
#regex.regex_to_NFA('a|b|c').toDot()
#regex.regex_to_NFA('(a|b|c)*').toDot()
#regex.regex_to_NFA('(a|b|c)*d').toDot()

def huntingtons(dna_sequence):
    """TODO: see task description for details """
    normal = "normal"
    carrier = "carrier"
    at_risk = "at risk"
    affected = "affected"
    
    diagnosis = normal
    return diagnosis
    
    
    
###### TESTING BELOW: Uncomment last line to test your huntingtons implementation ######    
    
def test_huntingtons():
    normal_strings = []
    carrier_strings = []
    at_risk_strings = []
    affected_strings = []
    
    normal_strings.append("g")
    normal_strings.append("cag")
    normal_strings.append("acagt")
    normal_strings.append("acacacacacacacacacacacacacacacacacacacacacacacacagcagttg")
    normal_strings.append('cag'*25)
    
    carrier_strings.append("ca" + 'cag'*27 + "g")
    carrier_strings.append("ca" + 'cag'*34 + "g")
    
    at_risk_strings.append("ca" + 'cag'*37 + "g")
    at_risk_strings.append("ca" + 'cag'*38 + "g")
    
    affected_strings.append("ca" + 'cag'*41 + "g")
    affected_strings.append("ca" + 'cag'*50 + "g")

    try:
        passed = True
        for test in normal_strings:
            if huntingtons(test) != 'normal':
                passed = False
                print("huntingtons failed for normal string", test)
                return
        for test in carrier_strings:
            if huntingtons(test) != 'carrier':
                passed = False
                print(huntingtons(test), len(test))
                print("huntingtons failed for carrier string", test)
                return
        for test in at_risk_strings:
            if huntingtons(test) != 'at risk':
                passed = False
                print("huntingtons failed for at risk string", test)
                return
        for test in affected_strings:
            if huntingtons(test) != 'affected':
                passed = False
                print("huntingtons failed for affected string", test)
                return
        if passed:
            print("huntingtons works!")
    except:
        print("huntingtons", "failed due to an error");


#test_huntingtons()
