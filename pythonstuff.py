import math 
import numpy as np

test_score = [88, 92, 79, 93, 85]
print(np.mean(test_score))

curved_test_score = [math.sqrt(score) * 10 for score in test_score]
print(np.mean(curved_test_score))






