from implementation import *
start, goal = (0, 10), (8, 3)
came_from, cost_so_far = a_star_search(diagram_test, start, goal)
draw_grid(diagram_test, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram_test, path=reconstruct_path(came_from, start=start, goal=goal))

print(diagram_test.weights)