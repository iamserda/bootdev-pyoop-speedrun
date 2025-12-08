
# def destroy_walls(wall_health):
#     h = []
#     for w in wall_health:
#         if w > 0:
#             h.append(w)
#     return h

def destroy_walls(wall_healths: list)->list:
    healthy_walls = []
    if wall_healths:
        for wall_health in wall_healths:
            if wall_health > 0:
                healthy_walls.append(wall_health)
    return healthy_walls

if __name__ == "__main__":
    assert destroy_walls([]) == []
