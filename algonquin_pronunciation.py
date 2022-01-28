#Giordano Di Marzio

import algonquin_utils

def get_consonant_pronunciation(x):
    
    """
    >>>get_consonant_pronunciation("b")
    'b'
    
    >>>get_consonant_pronunciation("j")
    'Ge'
    
    >>>get_consonant_pronunciation("x")
    ''
    
    """
    if algonquin_utils.is_valid_consonant(x):
        
        list1=["j","dj"] # Here we associate elements of the vocubalary directly to their pronunciation
        
        list2=["Ge","j"]
        
        for i in range (len(list1)): # we match the specific consonants to their pronunciation
            if list1[i]==x:
                return list2[i].upper()
        else:
            return x.upper() # It is only in the case where the consonant is j or dj that the pronunciation differs from the vocabulary
    else:
        return""
def get_vowel_pronunciation(x):
    
    """
    str->str
    
    >>>get_vowel_pronunciation("aj")
    ''
    >>>get_vowel_pronunciation("i")
    "i"
    
    >>>get_vowel_pronunciation("o")
    "u"
    
    """
    
    if algonquin_utils.is_valid_vowel(x):
        
        list1=["a","à","e","è","i","ì","o","ò"] # Same principle as last function
        
        list2=["a","a","e","e","i","ee","u","o"]
        
        for i in range (len(list1)): # in this case though, we need to map each element directly to its proper index in the second list
            if list1[i]==x:
                return list2[i].upper()
    else:
        return ""

        
def get_diphthong_pronunciation(x):
    
    """
    str->str
    
    >>>get_diphthong_pronunciation("iw")
    'ew'
    
    >>>get_diphthong_pronunciation("ow")
    'ow'
    
    >>>get_diphthong_pronunciation("ay")
    'ay'
        
    """
    
    if len(x)==2: # all of the diphthongs have 2 characters
        for i in range (len(algonquin_utils.DIPHTHONGS)): # we match the diphthong to its proper pronunciation
            if algonquin_utils.DIPHTHONGS[i]==x:
                list2=["ow","eye","ao","ay","ew","ow"]
                return list2[i].upper()
    return ""


def get_word_pronunciation(x):
    
    """
    str->str
    
    >>>get_word_pronunciation("kwewiay")
    kwaoieye
    
    >>>get_word_pronunciation("asdsad")
    asdsad
    
    >>>get_word_pronunciation("madjashin")
    majashin
    
    """
    if algonquin_utils.is_valid_single_word(x): # we verify if the word is valid before 
        
        trans="" # we create a string that will contain the final pronunciation ( chose trans like in the word translation ) 
        
        i=0
        while i<=(len(x)-1):
            if (i+1)<=(len(x)-1) and ((x[i]+x[i+1]) in algonquin_utils.DIPHTHONGS): # we see for every set of two letters before the last if any of them are diphthongs
                trans+=get_diphthong_pronunciation(x[i]+x[i+1]) 
                i+=1
            
            elif get_vowel_pronunciation(x[i])!="": # we then proceed to verify if the letter is instead a vowel
                trans+=get_vowel_pronunciation(x[i])
                
            elif get_consonant_pronunciation(x[i])!="": # we now proceed to verify if the letter is a consonant
                if (i+1)<=(len(x)-1) and (x[i]+x[i+1])=="dj": # because dj is the only two charactered consonant, we need to verify if there exists the pair of sequent letter dj in the word x 
                    trans+=get_consonant_pronunciation("dj") 
                    i+=1
                else:
                    trans+=get_consonant_pronunciation(x[i]) # if it isnt dj, it must be a sinle character consonant
            i+=1
        return trans.upper() # returning the string containing the final pronunciation translation
        
    else:
        return ""
   
def tokenize_sentence(x):
    
    """
    
    str->list
    
    >>>tokenize_sentence("asdasd  !")
    ['asdasd', ' ', ' ', '!']
    
    >>>tokenize_sentence(" 12,asdasd")
    ''
    
    >>>tokenize_sentence("kwey, anin eji-pimadizin?")
    ['kwey', ',', ' ', 'anin', ' ', 'eji', '-', 'pimadizin', '?']
    
    """
    
    if algonquin_utils.is_valid_phrase(x): # we check to see if there are any unwanted characters in the string
        
        sentence1=[] # we create two lists, one to store all of the letters and symbols individually , and another to gather the letters forming a word under a same index
        sentence2=[]
        
        for i in range (len(x)): 
            
            if x[i] in algonquin_utils.PUNCTUATION: # Here we put punctuation symbols, spaces and everything elsde ( being necessarily letters ) in the first list
                sentence1.append(x[i])
                
            elif x[i]==" ":
                sentence1.append(x[i]) 
                
            else:
                sentence1.append(x[i])
        k=0       
        while k<=(len(sentence1)-1): 
            
            if x[k] in algonquin_utils.PUNCTUATION or x[k]==" ": # if there is a space or a punctuation marik, it is put directly into the 2nd list
                sentence2.append(x[k])
                k+=1
            else:
                word="" # This is where we begin the formation of words from the letters put into individual indexes of the first list by creating an empty string word
                j=k # we set the 2nd index counter to the first that way the for loop can gather letters from an index after the space/punctuation
                while j<=(len(sentence1)-1):
                    
                    if x[j] not in algonquin_utils.PUNCTUATION and x[j]!=" ": # we add the letters together until we reach a space/punctuation
                        word+=x[j]   
                        j+=1
                    else:
                         break # exit the nested loop if it is the case
                sentence2.append(word)
                k=j # it is important to make sure we do not keep counting from the indexes of the letters we just assembled together, thats why we set k=j 
        return sentence2
    else:
            return []
                      
def get_sentence_pronunciation(x):
    
    """
    >>>get_sentence_pronunciation("Mino ishkwa nawakwe")
    Minu  ishkwa  nowakwe
    
    >>>get_sentence_pronunciation("asdasd 123")
    ''
    
    >>>get_sentence_pronunciation("aswaka-dji !")
    aswaka-ji!
    
    """
    if algonquin_utils.is_valid_phrase(x):
        
        list1=tokenize_sentence(x) # this will facilitate the creation of the final sentence
        word=""
        for i in range(len(list1)):
            if list1[i] in algonquin_utils.PUNCTUATION: # we verify if there is punctuation and add it directly to the desired final word
                word+=list1[i]
            else:
                word+=get_word_pronunciation(list1[i]) 
                if i+1<len(list1) and list1[i+1]!=" " and (list1[i+1] not in algonquin_utils.PUNCTUATION): # we dont want to add a space if there is a form of punctuation of if the element of x is already a space
                   word+=" "
        return word.upper()
    else:
        return ""
