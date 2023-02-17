from distinctipy import distinctipy
import pandas as pd


def create_distinct_rgb_colours(in_df: pd.DataFrame, colour_column: str, col_for_rbg_val: str) -> pd.DataFrame:
    """
    This function takes a dataframe and a column name. It creates a list of colours, that are as distinct from each
    other as possible and assigns them to each row, based on the values in the colour_column. Each identical value in
    that column gets the same colour value
    :param in_df: dataframe
    :param colour_column: column, on which the colours should be assigned to
    :param col_for_rbg_val: column where the created rgb values will be stored.
    :return: dataframe with the updated or newly added column with the colour values
    """
    # create a set from the df column, on which the colours will be showed by
    colour_vals = set(in_df[colour_column].tolist())
    # get the number of distinct colours
    colours = distinctipy.get_colors(len(colour_vals))
    # in order to use the result, plotly needs the text rgb
    colours = [f'rgb{x}' for x in colours]
    # create a dictionary to map the colour values based on the values in the column,
    # on which the colour is based on
    colour_dict = {
        key: colour for key, colour in zip(colour_vals, colours)
    }
    # map the dict to the column in the df
    in_df[col_for_rbg_val] = in_df[colour_column].map(colour_dict)
    return in_df


if __name__ == '__main__':
    pass
