from plotly_scattergeo import *


if __name__ == '__main__':

    pass

    """
    In his notebook, Bernoulli noted some of the expenses of his travels including the name of the currency.
    This dataset contains one row for each currency mentioned and the type of expense. In case of transportation cost, 
    the location of the destination was taken. Some rows had to be deleted as they did not contain the mandatory 
    information of identifiable currency or a location that had a wikidata page, based on which the coordinate 
    information was queried. Some locations could not be identified at all. 
    """

    # # This function call visualises the dataset described above, based on the name of the currency
    # create_scattergeo(
    #     in_csv="CurrencyVisualisationCoordinates",
    #     filter_value_column="CurrencyName",
    #     dropdown_label="Currency",
    #     inpath="visualisation_data",
    #     figure_title="Currency Mentioned in the Reisbüchlein",
    #     label_col_list=["locationName", "hasDate"]
    # )

    # # This function displays the frequency of cost noted in one geographical location
    # create_scattergeo_freuqency(
    #     in_csv="CurrencyVisualisationCoordinates",
    #     inpath="visualisation_data",
    #     text_col="CurrencyName",
    #     group_col="geonameID",
    #     location_name_col="locationName",
    #     figure_title="Number of Cost Noted per Location in the Reisbüchlein"
    # )

    # # This function call visualised the dataset described above, based on the type of expense
    # create_scattergeo(
    #     in_csv="CurrencyVisualisationCoordinates",
    #     filter_value_column="type",
    #     dropdown_label="Expense Type",
    #     inpath="visualisation_data",
    #     figure_title="Type of Expenses Noted in the Reisbüchlein",
    #     label_col_list=["type", "locationName", "hasDate"]
    # )

    """
    This data set was created through a SPARQL query. The coordinates were mapped with the 'Locations_Coordinates'
    document. The query specified the area of interest to the journey from Basel to Geneva, it request all the cost
    spent during that journey and the type of the expense.
    """

    # # This function call visualised the activities and cost enroute to Geneva
    # create_scattergeo(
    #     in_csv="ActivitiesCost_GenevaJourney",
    #     filter_value_column="type",
    #     dropdown_label="Expense Type",
    #     inpath="visualisation_data",
    #     figure_title="Expenses Enroute to Geneva",
    #     label_col_list=["cost", "nameCurrency", "nameLocation", "date"]
    # )
