def get_word_count(sentence):
       a=0
       b = False
       for char in sentence :
              if char.isalpha() :
                     b = True
              elif char == " " and b == True :
                     a+=1
                     b = False
       if b == True :
              a+=1
              
       return a

def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0
