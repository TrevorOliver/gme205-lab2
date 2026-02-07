















# import csv
# import pandas as pd


# DATA_PATH = "data/points.csv"

# class Point:
#     def __init__ (self, id, lon, lat):
#         self.id = id
#         self.lon = lon
#         self.lat = lat

# class PointSet:
#     def __init__(self, points):
#         self.points = points

#     @classmethod
#     def from_csv(cls, path):
#         try: 
#             df = pd.read_csv(DATA_PATH)
#         except FileNotFoundError: 
#             print(f"Error: Cannot find file at '{DATA_PATH}'.") 
#             print("Make sure you have: data/points.csv") 
#             raise

#         points = []
        
#         print(df.head())

#         # points = []
#         # with open(path, newline="", encoding="utf-8") as f:
#         #     reader = csv.DictReader(f)
#         #     for row in reader:
#         #         pid = str(row["id"])
#         #         lon = float(row["lon"])
#         #         lat = float(row["lat"])
#         #         points.append(Point(pid, lon, lat))
#         # return cls(points)