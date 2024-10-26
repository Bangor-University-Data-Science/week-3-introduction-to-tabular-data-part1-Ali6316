def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary = pd.DataFrame({
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Number of Unique Values': [df[feature].nunique() for feature in df.columns],
        'Has Missing Values': [df[feature].isnull().any() for feature in df.columns]
    })
    
    return summary
