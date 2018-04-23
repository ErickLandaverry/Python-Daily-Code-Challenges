# Write a method that translates a text to Pig Latin and back. 

#   For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added, as in the following examples:. "The quick brown fox" becomes "Ethay uickqay rownbay oxfay".

#       BONUS:

#       Allow for when a vowel is the first letter (like is, or, of) then the letters are kept the same, and "ay" is added to the end of said letters.


def text ():
  print('Hello! Go ahead and type a text and watch it be magically translated to Pig Latin:')
  translate=str(input('')).split()
  for word in translate:
    print(word[1:] + word [0] + "ay", end='') 
   

text()