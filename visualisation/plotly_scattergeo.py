import os
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


from pandas_tools import PandasTools
from colour_creator import *


def create_scattergeo_list(
        grouped_df: pd.DataFrame.groupby, colour_val_column: str, text_label_col: str,
        long_col: str = "Long", lat_col: str = "Lat") -> list[go.Scattergeo]:
    """
    This function creates an individual scattergeo plot for each group in a grouped dataframe and appends them to a
    list. This can be used to add individual traces to one figure.
    :param grouped_df: Dataframe that is already grouped
    :param colour_val_column: column that stores the colour value for the individual point
    :param text_label_col: the column that stores the text label for the individual point
    :param long_col: column with longitude value
    :param lat_col: column with latitude value
    :return: a list with scattergeo figures
    """
    # intiate a list
    trace_list = []
    # iterate over the grouped df
    for group_name, group in grouped_df:
        # append the trace
        trace_list.append(
            go.Scattergeo(
                lon=group[long_col],
                lat=group[lat_col],
                # set the text for the hover label
                text=group[text_label_col],
                # show each value as a point
                mode="markers",
                # assign a colour for the marker
                marker_color=group[colour_val_column],
                # add the name for the marker, this is displayed in the legend
                name=group_name
            ))
    # return the trace
    return trace_list


def create_one_dropdown_button(button_name: str, idx_button: int, len_buttonlist: int, visible_value: bool = False) \
        -> dict:
    """
    This function creates a button for a dropdown menu. The 'visible_value' decides if all the values which specifies
    visibility of the data is true or false, default is false. the value is to be set to true if all data should be
    selected. In that case setting the value with the index value to true too, has no effect, but it is faster
    than checking with a bool if this operation should be done, as this button only exists once, while the buttons that
    need this operation may be numerous.
    :param button_name: Display name for the button
    :param idx_button: the index number for the data that should be visible
    :param len_buttonlist: the length of the list that contains the data
    :param visible_value: if all the values in the list should be true or false, default false in order to create a
    filter for the data
    :return: dictionary with button specifications
    """
    # normally we only want the data returned that corresponds to the name of the button, but, in order to create one
    # button that selects all the data, we need all the visible values as True.
    visible = [visible_value] * len_buttonlist
    # change the button we are currently creating to true, so that it shows that selection
    visible[idx_button] = True
    return dict(
        # set to modify the data
        method='restyle',
        # specify the visibility of the button
        args=[{'visible': visible}],
        # set the name for the button
        label=button_name
    )


def create_all_dropdown_buttons(input_df: pd.DataFrame, button_name_col: str, all_selection_button_name) -> list[dict]:
    """
    This function creates a dropdown menu for a graph. Each group of the values in the column 'button_name_col'
    should have an individual trace to enable the filtering through a dropdown. Firts it creates a button to select
    all data and then one button per group. It returns a list with dictionaries, with the display specifications.
    :param all_selection_button_name: The name of the button that selects all the data
    :param input_df: dataframe
    :param button_name_col: name of the column that contains the name for the button
    :return: a list with dictionaries that contain the styling information for each button.
    """
    # get a unique list of the names for the individual buttons
    button_names = input_df[button_name_col].drop_duplicates().tolist()
    # sort the list alphabetically
    button_names.sort()
    len_list = len(button_names)
    # initiate a list to store each button
    button_list = [
        # create the button that selects all, the index for the button has no effect in this case as all values are
        # already true because 'visible_value' is set to true
        create_one_dropdown_button(
            button_name=all_selection_button_name,
            idx_button=0,
            len_buttonlist=len_list,
            visible_value=True
        )
    ]
    # iterate over the list as the first button is the whole selection,
    for i, name in enumerate(button_names):
        button_list.append(
            create_one_dropdown_button(
                button_name=name.capitalize(),
                idx_button=i,
                len_buttonlist=len_list
            )
        )
    return button_list


def create_scattergeo(
        in_csv: str, inpath: os.path, label_col_list: list[str], filter_value_column: str, dropdown_label: str,
        figure_title: str, long_col: str = "Long", lat_col: str = "Lat", geoscope="europe") -> None:
    """
    This function takes a csv document and creates an interactive web based visualisation. It overlays individual
    data as dots over a geographical map. Each datapoint is labeled based on the values of one or more columns.
    The displayed datapoints can be filtered according to a specified criteria.
    :param in_csv: name of the csv, containing the data
    :param inpath: path to the csv document
    :param label_col_list: a list with column names, which are used to create the labels for each individual dot
    :param filter_value_column: the column, which contains the values according to which the dots are grouped
    :param dropdown_label: the title for the dropdown menu
    :param figure_title: The title of the whole figure
    :param long_col: name of the column that stores the longitude values
    :param lat_col: name of the column that stores the latitude values
    :param geoscope: The display of the map can be limited to a content, default is europe
    :return: None, a browser window pops up displaying the figure
    """
    df = PandasTools.in_csv_to_df(
        in_csv_name=in_csv,
        inpath_name=inpath
    )
    # create the hover label, based on a list of columns, if the value is not empty, then it adds that to the label
    df["label_text"] = np.nan
    for i, row in df.iterrows():
        text_string_list = []
        # check if the specific column is empty, if not append the value
        for col in label_col_list:
            if PandasTools.check_is_not_empty(pd_row=row, column=col):
                text_string_list.append(str(row[col]))
        # join the values and assign not the df column
        df.loc[i, "label_text"] = ", ".join(text_string_list)
    # get the colour
    df = create_distinct_rgb_colours(
        in_df=df,
        colour_column=filter_value_column,
        col_for_rbg_val="colour_values"
    )
    # group the df according to the colour column
    grouped = df.groupby(by=filter_value_column)
    # create the figure
    fig = go.Figure()
    # create for each column which is grouped together based on value its own trace by grouping the df according
    # to the desired column, this is so that they can be filtered according to this value
    list_trace = create_scattergeo_list(
        grouped_df=grouped,
        colour_val_column="colour_values",
        text_label_col="label_text",
        long_col=long_col,
        lat_col=lat_col
    )
    # add the individual traces to the figure
    for individual_trace in list_trace:
        fig.add_trace(
            individual_trace
        )
    # limit the region showed in the graph and add the title
    fig.update_layout(
        geo_scope=geoscope,
        title=f"<b>{figure_title}</b>"
    )
    dropdown_title = f'<b>All {dropdown_label.title()}</b>'
    # create the buttons for the dropdown menu
    list_buttons = create_all_dropdown_buttons(
        input_df=df,
        button_name_col=filter_value_column,
        all_selection_button_name=dropdown_title
    )
    # update the layout with the buttons for the dropdown
    fig.update_layout(
        # create the dropdown
        updatemenus=[
            dict(
                # the list of the buttons
                buttons=list_buttons,
                # direction in which the list should extend
                direction="up",
                # the padding around the buttons and dropdown
                pad={"r": 10, "t": 10},
                # highlighting the active button
                showactive=True,
                # placement on the axis
                xanchor="left",
                y=0.1,
                x=-0.05,
                yanchor="bottom"
            )
        ],
        # add a title for the dropdown menu
        annotations=[
            dict(
                # label name
                text=dropdown_title,
                # placement
                x=-0.05,
                y=0.15,
                align="left",
                # do not show an arrow pointing to the dropdown box
                showarrow=False
            )
        ]
    )
    # show the figure
    fig.show()


def create_scattergeo_freuqency(
        in_csv: str, inpath: os.path, group_col: str, location_name_col: str, text_col: str, figure_title: str,
        long_col: str = "Long", lat_col: str = "Lat", geoscope="europe") -> None:
    """
    This function creates a geo scatterplot based on a csv. The markers display the frequency of an occurrence in one
    geographical location based on a specified column. Each marker is labeled with the name of the location and all the
    entries in another specified column once.
    :param in_csv: name of the csv with the data
    :param inpath: path to the document
    :param group_col: column name on which the dataframe should be grouped
    :param location_name_col: name of the column, which provides the name for the geographical location
    :param text_col: name of the column, which contains additional text we want to include in our label
    :param figure_title: title of the figure
    :param long_col: name of the longitude column
    :param lat_col: name of the latitude column
    :param geoscope: region in the world the graph should display
    :return: None, a browser window pops up displaying the figure
    """
    df = PandasTools.in_csv_to_df(
        in_csv_name=in_csv,
        inpath_name=inpath
    )
    # we create a new dataframe for the visualisation, which we will create from a list of dictionaries
    visualisation_dict_list = []
    # group the dataframe according to the column on which the frequency is based
    grouped = df.groupby(by=group_col)
    # iterate over the grouped dataframes
    for name, group in grouped:
        # reset the index, so that we can access the values through the index number
        group.reset_index(inplace=True)
        # text for the hover labels, this includes the location and all the currency names mentioned in that place once
        text = group.at[0, location_name_col] + ": " + ", ".join(group[text_col].drop_duplicates(keep="first").tolist())
        # create the dictionary with the information needed for the visualisation
        visualisation_dict_list.append(
            {
                "Name": group.at[0, location_name_col],
                "Number": len(group),
                "Lat": group.at[0, lat_col],
                "Long": group.at[0, long_col],
                "Text": text
            }
        )
    # create a df from the list of dictionaries
    visualisation_df = pd.DataFrame.from_records(data=visualisation_dict_list)
    # create a scatter geo figure
    fig = px.scatter_geo(
        # specify the dataframe
        data_frame=visualisation_df,
        # name of the column for long and lat
        lon="Long",
        lat="Lat",
        # name of the column which contains the text for the hover label
        hover_name="Text",
        # column on which the size of the markers are based on
        size="Number",
        # the markers should be coloured according to their size
        color="Number"
    )
    # restrict the geoscope and add the title
    fig.update_layout(
        geo_scope=geoscope,
        title=f"<b>{figure_title}</b>"
    )
    # the image automatically zooms in on the data points
    fig.update_geos(
        fitbounds="locations"
    )
    fig.show()


if __name__ == '__main__':
    pass

