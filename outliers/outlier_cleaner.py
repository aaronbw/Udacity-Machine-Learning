def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
 
    # Find residual error
    error = predictions - net_worths
    
    
    # Create a list of tuples and remove 10% of the points
    # that have the largest residual errors
    data = zip(ages, net_worths, error)
    
    cleaned_data = sorted(data, key=lambda x: x[2])
    cleaned_data = cleaned_data[:81]

    return cleaned_data