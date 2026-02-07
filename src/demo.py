from spatial import Point, PointSet


p = Point("123", -122.4194, 37.7749)
print(p.id, p.lon, p.lat)

ps = PointSet.from_csv("data/points.csv")