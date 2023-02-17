import os
import warnings
import pandas as pd


class PandasTools:

    @staticmethod
    def in_csv_to_df(in_csv_name: str, inpath_name: os.path) -> pd.DataFrame:
        return pd.read_csv(filepath_or_buffer=os.path.join(inpath_name, f'{in_csv_name}.csv'))

    @staticmethod
    def save_df_csv(file_path, name_df: pd.DataFrame, name_csv: str) -> None:
        name_df.to_csv(path_or_buf=os.path.join(file_path, f"{name_csv}.csv"), index=False)

    @staticmethod
    def check_is_not_empty(pd_row, column):
        # Check if a cell is empty
        if not pd.isna(pd_row[column]):
            return True
        else:
            return False

    @staticmethod
    def map_col_based_on_other_df(
            keydf, targetdf, source_col_key, source_col_info, target_key_col, target_info_col):
        # drop all the rows in which the column, that is used as a dictionary key are empty
        # if this contains information that should be
        map_df = keydf.dropna(subset=[source_col_key])
        # create a dictionary to map
        map_dict = dict(zip(map_df[source_col_key], map_df[source_col_info]))
        # map the values
        targetdf[target_info_col] = targetdf[target_key_col].map(map_dict)
        return targetdf

    @staticmethod
    def map_coordinates(
            incsv_data, incsv_coordinates, data_folder, data_id_column, coordinate_id_column, out_csv,
            long_col="Long", lat_col="Lat"):
        data_df = PandasTools.in_csv_to_df(in_csv_name=incsv_data, inpath_name=data_folder)
        coordinate_df = PandasTools.in_csv_to_df(in_csv_name=incsv_coordinates, inpath_name=data_folder)
        data_df = PandasTools.map_col_based_on_other_df(
            keydf=coordinate_df,
            targetdf=data_df,
            source_col_key=coordinate_id_column,
            source_col_info="Long",
            target_key_col=data_id_column,
            target_info_col=long_col
        )
        data_df = PandasTools.map_col_based_on_other_df(
            keydf=coordinate_df,
            targetdf=data_df,
            source_col_key=coordinate_id_column,
            source_col_info="Lat",
            target_key_col=data_id_column,
            target_info_col=lat_col
        )
        if data_df["Long"].isna().any():
            warnings.warn("There are rows, for which no coordinates could be transferred.")
        PandasTools.save_df_csv(
            file_path=data_folder,
            name_df=data_df,
            name_csv=out_csv
        )


if __name__ == '__main__':
    pass

    # PandasTools.map_coordinates(
    #     incsv_data="Transportation",
    #     incsv_coordinates="Locations_Coordinates",
    #     data_folder="visualisation_data",
    #     data_id_column="geonameIDend",
    #     coordinate_id_column="geonameID/mapID",
    #     out_csv="Transportation"
    # )
    #





