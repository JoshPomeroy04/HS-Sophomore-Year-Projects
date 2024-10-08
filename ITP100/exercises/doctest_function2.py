def only_vowels(s):
    """
    Return a string containing only the vowels in the orginial text in the
    same order in which they originally appeared.

      >>> only_vowels("What about that?")
      'aaoua'
      >>> only_vowels("Mississippi")
      'iiii'
      >>> only_vowels("This is a sentence. This also is a sentence.")
      'iiaeeeiaoiaeee'
      >>> only_vowels("A real winner named Abbot!")
      'AeaieaeAo'
    """
    vowels = "aAeEiIoOuU"
    only_vowels = ""
    for i in s:
        if i in vowels:
            only_vowels = only_vowels + i
    
    return only_vowels
            
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()
