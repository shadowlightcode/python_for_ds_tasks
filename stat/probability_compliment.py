#Task Probability of complements problems
# a) P(A) = 0.7. What is P(A`)?

#use python
def complement(probability):
    if 0 <= probability <= 1:
        return 1 - probability
    else: 
        raise ValueError("Propability must be between 0 and 1.")
    
probability_event = 0.7 # chance of something happening
probability_not_event = complement(probability_event)
print(f'Complement (not happening): {probability_not_event:.2f}')
   
#use numpy 
import numpy as np

p = np.array([0.2, 0.5, 0.9])
p_complement = 1 - p

print('P(event):', p)
print('P(not event):', p_complement)