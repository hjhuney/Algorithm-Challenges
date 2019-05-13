import sys

n = 20
test1 = 'miss miss hit miss hit miss hit miss miss hit miss miss miss miss hit hit hit miss hit miss'
# print(len(test1))

# num = int(input())
# test = input()

shots = test1.split()
# print(shots)

horse = "HORSE"
counter = 0
p1_misses = 0
p2_misses = 0

# print(len(shots))

while counter < len(shots):
    if shots[counter] == "hit":
        if shots[counter+1] == "miss":
            if (counter+1)% 2 == 0:
                p1_misses += 1
            else: 
                p2_misses += 1
                
        counter += 2
#         print(counter, "hit")
        
    elif shots[counter] == "miss":
        counter += 1
#         print(counter, "miss")

        
# print(p1_misses)
# print(p2_misses)

print("Player 1: " + horse[:p1_misses] )
print("Player 2: " + horse[:p2_misses] )