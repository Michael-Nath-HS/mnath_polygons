from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 114, 48 ]
edges = []
polygons = []
transform = new_matrix()
draw_polygons(polygons, screen, color)
display(screen)
parse_file( 'script', edges, polygons, transform, screen, color )
