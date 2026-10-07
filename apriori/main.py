# %%
import pandas as pd
import numpy as np
# data preprocessing

dataset = pd.read_csv('C:/Interview Process/python_ML/apriori/Market_Basket_Optimisation.csv', header=None)

# Keep only actual items; dropping empty/NaN values avoids creating useless "nan" items
# and makes the rule-generation step much faster.
transactions = [
    [str(item) for item in row if str(item) not in {'nan', 'None', ''}]
    for row in dataset.fillna('').values
]

# %%
# training apriory algo
from apyori import apriori

rules = apriori(
    transactions=transactions,
    min_support=0.003,
    min_confidence=0.2,
    min_lift=3,
    min_length=2,
    max_length=2
)
# %%
result = list(rules)
result
# %%
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))

resultsinDataFrame = pd.DataFrame(inspect(result), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
# %%
resultsinDataFrame
# %%
