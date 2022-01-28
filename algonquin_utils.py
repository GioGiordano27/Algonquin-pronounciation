#Giordano Di Marzio

CONSONANTS = "bcdghkmnpstwyzj"
VOWELS = "aeio"
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

def is_valid_consonant(x):
    
    """
    str -> Boolean
    
    >>> is_valid_consonant("c")
    True
    
    >>>  is_valid_consonant("poo") # Does not return any value, bc the input wasn't a character
    False
    
    >>>   is_valid_consonant("x")
    False
    
    """
    
    
    if (len(x)!=1) and (x.lower()!="dj"): # dj is the only consonant not of length 1
        return False 
    return (x.lower() in CONSONANTS or x.lower()=="dj") # we make sure not to forget the fact that we could be dealing with uppercases letters
        
def is_valid_vowel(x):
    
    """
    str -> Boolean
    
    >>> is_valid_vowel("10")
    False
    
    >>> is_valid_vowel("àèì")
    False
    
    >>> is_valid_vowel("à")
    True
    
    """
    
    if len(x)!=1: # All vowels only have one letter
        return False  
    return ( (x.lower() in VOWELS) or (x.lower() in VOWELS_WITH_ACCENT) ) # we verify to see if the letter is either in vowels or vowels with accents
        
def is_valid_single_word(x):
    
    """
    str -> Boolean
    
    >>> is_valid_single_word("asdbasdasodahnsdjkasdnajskjnd")
    False
    
    >>> is_valid_single_word("qwe15")
    False
    
    >>> is_valid_single_word("].;asdmasmnda")
    False
    
    """
    
    for i in range(len(x)):
        if not ((is_valid_consonant(x[i])) or (is_valid_vowel(x[i])) or x==DIPHTHONGS[i]): # if each element of the word is either a Consonant/vowel/diphthon, we know it is a valid word
            return False
    return True

def is_valid_phrase(x):
    """
    str -> Boolean
    
    >>>is_valid_phrase("jai ei")
    True
    
    >>>is_valid_phrase("Hi, I hope whoever is reading this is having a great day:)")
    False
    
    >>>is_valid_phrase(":3")
    False

    """
    for i in range(len(x)):
        if not((is_valid_consonant(x[i]) or (is_valid_vowel(x[i])) or (x[i]==" ") or x[i] in PUNCTUATION)): # if the elements of the sentence are in punctuation,are a space, or are either a conson./vowel, we know it is a valid phrase                                                                                               #
            return False
    return True



