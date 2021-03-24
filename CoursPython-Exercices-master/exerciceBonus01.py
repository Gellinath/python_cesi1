import random
def la_roulette(mise, numero):

       if mise<1 :
              return "Veuillez miser minimum 1 pour jouer"
       if numero<0 or numero>49 :
              return "Vous ne pouvez miser que sur des numéros compris entre 0 et 49"

       numeroStatut = ""
       if numero%2 == 0 :
              numeroStatut = "Pair"
       else :
              numeroStatut = "impair"
       
       a=random.randint(0,49)
       b = ""
       if a%2 == 0 :
              b = "Pair"
       else :
              b = "impair"

       gain = 0
       
       if numero == a :
              gain = mise*3
       elif b == numeroStatut :
              gain = mise//2
              
       return "le numéro est : ",a, ". Vos gains : ",gain
