import exercice01
import exercice02
import exercice03
import exercice04
import exercice05
import exercice06
import exercice07
import exercice08

all_exercises = [
    exercice01.run, 
    exercice02.run, 
    exercice03.run,
    exercice04.run,
    exercice05.run,
    exercice06.run,
    exercice07.run,
    exercice08.run,
]

i = 1
for exercise in all_exercises:
    try:
        exercise()
        print(f"✅ Exercice {i} : passé")
    except AssertionError:
        print(f"❌ Exercice {i} : raté")
    finally:
        i += 1
