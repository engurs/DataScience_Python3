import pandas as pd

tweets_df = pd.read_csv('tweets.csv')


def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    cols_count = {}

    # Extract column from DataFrame
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    return cols_count


result = count_entries(tweets_df)
print(result)
