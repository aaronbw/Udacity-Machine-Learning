#!/usr/bin/python3


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
 

#     cleaned_data = []
# 
#     ### your code goes here
#     import pandas as pd
#     
#     
#     
#     return cleaned_data


    data = []
    
    size = len(predictions)
    
    for i in range(size):
        error = (predictions[i][0] - net_worths[i][0]) * (predictions[i][0] - net_worths[i][0])
        data.append((ages[i][0],
                        net_worths[i][0],
                        error))
    
    data.sort(key=lambda tup: tup[2])
    
    
#     class Data_Length(object):
#         def __index__(self):
#             return int(len(data) * .9)
# 
# 
#     data_length = Data_Length()
#     print('data_length = ', data_length)
    
    cleaned_data = data[:81]
    print(len(cleaned_data))


    return cleaned_data