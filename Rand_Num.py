#Program generates a random number between 1 and 99

#imports libraries
import random
import time

print("""
$$$$$$$\                            $$\       $$\   $$\                         
$$  __$$\                           $$ |      $$$\  $$ |                        
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$$ |      $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  
$$$$$$$  | \____$$\ $$  __$$\ $$  __$$ |      $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ 
$$  __$$<  $$$$$$$ |$$ |  $$ |$$ /  $$ |      $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |      $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |      $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |
\__|  \__| \_______|\__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|
""")
# define constant r1 - r10
r1 = random.randint(1,99)
r2 = random.randint(1,99)
r3 = random.randint(1,99)
r4 = random.randint(1,99)
r5 = random.randint(1,99)
r6 = random.randint(1,99)
r7 = random.randint(1,99)
r8 = random.randint(1,99)
r9 = random.randint(1,99)
r10 = random.randint(1,99)

# prints numbers with 3 second interval inbetween
print(r1)
time.sleep(3)
print(r2)
time.sleep(3)
print(r3)
time.sleep(3)
print(r4)
time.sleep(3)
print(r5)
time.sleep(3)
print(r6)
time.sleep(3)
print(r7)
time.sleep(3)
print(r8)
time.sleep(3)
print(r9)
time.sleep(3)
print(r10)
