"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
"-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example,
"cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such
a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""


def uniqueMorseRepresentations(words: list[str]) -> int:
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...",
                  "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    tmp_str = ""
    my_Dict= dict()
    for i in words:
        for j in range(len(i)):
            tmp_str += morse_code[ord(i[j]) - 97]
        if tmp_str not in my_Dict:
            my_Dict[tmp_str] = 1
        tmp_str = ""
    return len(my_Dict.values())

