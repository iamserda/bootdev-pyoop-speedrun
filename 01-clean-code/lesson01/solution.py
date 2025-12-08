
# def destroy_walls(wall_health):
#     h = []
#     for w in wall_health:
#         if w > 0:
#             h.append(w)
#     return h
#
# Rewrite the function above to look more clean
# As of now, given a list of walls, it should return a list of healthy walls left. 
# The others are "destroyed"

def destroy_walls(wall_healths: list)->list:
    healthy_walls = []
    if wall_healths:
        for wall_health in wall_healths:
            if wall_health > 0:
                healthy_walls.append(wall_health)
    return healthy_walls

if __name__ == "__main__":
    assert destroy_walls([]) == []
