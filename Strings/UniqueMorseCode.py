class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            morse_word=""
            for letter in word:
                morse_word += morse[ord(letter) - 97]
            words[words.index(word)] = morse_word
        return len(set(words))