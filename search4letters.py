def search4letters(phrase, letters = 'aeiou') -> set:
    return set(phrase).intersection(set(letters))
    
