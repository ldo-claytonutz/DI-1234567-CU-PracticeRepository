import pandas as pd
from sqlalchemy import create_engine, text
from typing import Union, Callable, List
import os
from os import PathLike
from openpyxl import load_workbook


class ExportUtils:

    # to export a SQL table to an Excel file.