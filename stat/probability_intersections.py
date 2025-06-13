# Probability of A and B (Intersection)
# When we say "A and B," we mean the probability that both events happen at the same time. 
# This is called the intersection of A and B and is written as:

# P(A and B) or P(A ∩ B)

# If A and B are independent (they don't affect each other), 
# the probability of both happening is:
# P(A and B) = P(A) × P(B)

# For example, if you flip a coin (with a 1/2 chance of heads) and roll a die (with a 1/6 chance of getting a 3), 
# the chance of getting heads and 3 is: 1/2 × 1/6 = 1/12

#task Pr(A) = 0.5,Pr(B) = 0.6,Pr(A ∩ B) = 0.4 Are these events independent?

p_A = 0.5
p_B = 0.6
p_A_and_p_B = 0.4
intersection = 0.5 * 0.6 = 0.3
if p_A_and_p_B == intersection: 
    print(f'Events are independent, because {p_A_and_p_B} equal {intersection}')
else: 
    print(f'Events are not independent, because {p_A_and_p_B} not equal {intersection}')

# Pr(A ∩ B) = 0.4 means events happens 
# Conclusion intersection not equal 0.4, so events are not independent 

