import pandas as pd
from sqlalchemy import create_engine, text
from typing import Union, Callable, List
import os
from os import PathLike
from openpyxl import load_workbook


class ExportUtils:

    # to export a SQL table to an Excel file.
    @staticmethod
    def save_df_to_excel(df: pd.DataFrame, file_name: PathLike, index=False, **pdkwargs) -> None:
        """
        df: Pandas dataframe to save
        file_name: destination path to save
        index: whether to include the pandas dataframe index in output (default is False)
        pdkwargs: other kwargs to pass into the .to_excel() method
        """
        df.to_excel(file_name, index=index, **pdkwargs)
