def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': ['Fare','Age'],  # Fill with continuous numerical features
            'discrete': ['SibSp','Parch']  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': ['Sex','Embarked'],  # Fill with nominal categorical features
            'ordinal': ['Pclass']  # Fill with ordinal categorical features
        }
    }
    return feature_types
