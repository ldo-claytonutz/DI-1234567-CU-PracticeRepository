# %%
import pandas as pd
from sqlalchemy import create_engine, text
import urllib
import json
import re
from typing import Union, Callable, List
import os

# %%
class SQLUtils:

    ## to upload txt, excel, csv files to a SQL table.

        