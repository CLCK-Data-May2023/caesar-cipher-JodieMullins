# Dictionary established to use for translate method, which is available to 
# string types; also established to clearly define required alphabet replacement
# shift of 5 letters; also because writing something with lists and strings was taking forever

# Will not overwrite special characters or numeric values, as requested


encoded = {
    'a': 'f',
    'b': 'g',
    'c': 'h',
    'd': 'i',
    'e': 'j',
    'f': 'k',
    'g': 'l',
    'h': 'm',
    'i': 'n',
    'j': 'o',
    'k': 'p',
    'l': 'q',
    'm': 'r',
    'n': 's',
    'o': 't',
    'p': 'u',
    'q': 'v',
    'r': 'w',
    's': 'x',
    't': 'y',
    'u': 'z',
    'v': 'a',
    'w': 'b',
    'x': 'c',
    'y': 'd',
    'z': 'e',
}

# To later use the translate method on my string, I have to first use the maketrans method

# Within the maketrans() string method I pass my dictionary deemed 'encoded' to 
# pair the Python-established ASCII table keys with my new alphabet-shifted values
cipher = str.maketrans(encoded) # This new unicoded dictionary is held by the variable cipher


# Next, I want to establish the exact string to work with; in this case, the string I want to 
# work with will be input by the user, held by the variable 'user_sentence'
user_sentence = str(input('Input message: ')).lower()
# - lower method allows for control over user input to ensure stable output regardless of capitalization


# Now I want to update the value of the 'user_sentence' so that 
# whatever statement the user input is ciphered beyond quickly recognizable language

# The translate method will take in (the re-assigned ASCII table values from my) variable cipher
# and 'translate' the characters identified in the 'encoded' dictionary from the user's 
# sentence (entered based on Python-established ASCII)  
user_sentence = user_sentence.translate(cipher)

print('The encrypted sentence is:', user_sentence)