def get_letter_count(word):
       a=0
       for char in word :
              if char.isalpha() :
                     a+=1
                     
       return a

def run():
   assert get_letter_count("Oui") == 3
   assert get_letter_count("Bonjour") == 7
   assert get_letter_count("") == 0
   assert get_letter_count(".........hein???") == 4
   assert get_letter_count("Attention y'a quatre mots !") == 21
