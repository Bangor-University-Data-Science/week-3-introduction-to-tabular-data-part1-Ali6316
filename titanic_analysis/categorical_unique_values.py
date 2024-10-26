def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values_dict = {}  

    for feature in categorical_features:
        unique_v = df[feature].unique()  
        unique_values_dict[feature] = unique_v 
        print(f"Unique values for {feature}: {unique_v}")  
        
    return unique_values_dict
