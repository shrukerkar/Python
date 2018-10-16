import random


# function random_kid works on bayesTheorem
def random_kid():
    return random.choice(["boy","girl"])
both_girls=0
older_girls=0
either_girls=0

random.seed(0)
for _ in range(10000):
   younger=random_kid()
   older=random_kid()
   if older=="girl":
    older_girls+=1
    if older=="girl" and younger=="girl":
        both_girls+=1
    if older == "girl" and younger == "girl":
        either_girls+=1

print("P(both|older)",both_girls/older_girls)
print("P(both|either)",both_girls/either_girls)

