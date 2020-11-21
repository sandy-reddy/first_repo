points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]


points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key = lambda x: x[1])

# the lambda above is the same thing as the function below
# def sort_by_y(x):
#     return x[1]

print(points2D_sorted)

points2D_sorted = sorted(points2D, key = lambda x: x[0] + x[1])
print(points2D_sorted)


