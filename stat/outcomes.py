#Task
# 1 Outcomes, Events, Sample Space, Complements
# 1.1. What is the sample space of the following experiments? What is the size of the sample space? (We
# sometimes call the number of possible outcomes the cardinality).

# a) The outcomes of a six-sided die roll.

# Approach to solve the task:
# 1. we have one six-sided die 
# 2. so we knew that each side has one number
# 3. they are independent
# 4. so Sample Space will be {1,2,3,4,5,6} and outcome will be 6
# 5. so count the propability of appearing 4 will be equal 1/6
# 6. solve it with python 

outcomes = []
for die in range(1, 7):
    outcomes.append(die)
    
print(f"Outcome for rolling one die: {len(outcomes)}")  

import random

rolls = 100
count_6 = 0

for die in range(rolls):
    if random.randint(1, 6) == 6:
        count_6 += 1

simulated_prob = count_6 / rolls
print(f"Simulated probability: {simulated_prob:.4f}")

# b) The outcomes of two rolls of a six-sided die.
# Approach to solve the task:
# 1. we have two six-sided die 
# 4. there are 6 possible outcomes for the first roll, and 6 possible outcomes for the
# second roll, so there are 36 possible outcomes
# 5. so count the propability of appearing 4 will be equal 1/36
# 6. solve it with python 

outcomes = []
total_outcomes = 0
count_only_six = 0

for die1 in range(1, 7):
    for die2 in range(1, 7):
        outcomes.append((die1, die2))
        
print(outcomes)
print(f"Outcome for rolling both dies: {len(outcomes)}")        


for die1 in range(1, 7):
    for die2 in range(1, 7):
        total_outcomes += 1
        if die1 == 4 and die2 == 4:
            count_only_six += 1

probability = count_only_six / total_outcomes
print(f"Probability of rolling only 4: {probability:.4f}")

# c) The number of goals scored in a hockey game.
# Solution: The sample space is the set of all non-negative integers. That is, the number of
# goals scored in a game can be 0, 1, 2, 3, 4, or (theoretically) any other positive integer. Thus,
# the size of the sample space is infinite because there is technically no limit on how many goals
# can be score in a game.

# d) The distance traveled to work, in miles.
# Solution: The sample space is the set of all non-negative real numbers. That is, the distance
# traveled to work can be 0, for someone who works at home, and it can be any positive number
# - 0.4 miles, 20 miles, or 100.373 miles. Thus, the size of the sample space is infinite, because
# there are infinitely many possible distances.
