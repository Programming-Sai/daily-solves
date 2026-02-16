def uniqueMorseRepresentations(words):
    morse_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    res_set = set()
    for word in words:
        morse_word=""
        for char in word:
            morse_word += morse_table[ord(char) - ord("a")]
        res_set.add(morse_word)
    return len(res_set)