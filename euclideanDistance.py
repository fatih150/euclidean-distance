def euclideanDistance(point1, point2):

  x1, y1 = point1
  x2, y2 = point2
  distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
  return distance

points = [(1, 1), (9, 16)]

distance = euclideanDistance(points[0], points[1])

print("İki nokta arasındaki mesafe:", distance)
