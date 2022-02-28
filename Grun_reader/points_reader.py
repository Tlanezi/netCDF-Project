# PointSet Class
# Mohammad Areeb Anwer

import os
import pandas as pd


class PointsSet:
    def __init__(self, file_name="points.xlsx"):
        self.file_name = file_name
        self.points_data = pd.read_excel(self.file_name)
        self.lat_search = float
        self.lon_search = float

    def get_lat_search(self, index=int):
        self.lat_search = self.points_data['Latitude'][index]
        return self.lat_search

    def get_lon_search(self, index=int):
        self.lon_search = self.points_data['Longitude'][index]
        return self.lon_search

    def __call__(self, *args, **kwargs):
        # prints class structure information to console
        print("Class Info: <type> = PointsSet (%s)" % os.path.dirname(__file__))
        print(dir(self))
