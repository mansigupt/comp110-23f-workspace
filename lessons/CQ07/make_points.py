"""Method calling for points."""

from lessons.CQ07.point import Point

my_point: Point = Point(10.0, 20.0)
my_new_point: Point = my_point.scale(4)
print(my_new_point.x, my_new_point.y)