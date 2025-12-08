# def fight_soldiers(soldier_one, soldier_two):
#     soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
#     soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
#     if soldier_one_dps > soldier_two_dps:
#         return "soldier 1 wins"
#     if soldier_two_dps > soldier_one_dps:
#         return "soldier 2 wins"
#     return "both soldiers die"
#
# Rewrite the function above, make it DRY
#

def fight_soldiers(soldier_one, soldier_two):
    pass

#=================================================== #
# ================= TEST ARENAS ==================== #
#=================================================== #
if __name__ == "__main__":
    s1 = {"damage": 10, "attacks_per_second": 1}
    s2 = {"damage": 6, "attacks_per_second": 2}
    assert fight_soldiers(soldier_one=s1, soldier_two=s2) == "soldier 2 wins"

    s1 = {"damage": 6, "attacks_per_second": 3}
    s2 = {"damage": 15, "attacks_per_second": 1}
    assert fight_soldiers(soldier_one=s1, soldier_two=s2) == "soldier 1 wins"

    s1 = {"damage": 10, "attacks_per_second": 1}
    s2 = {"damage": 5, "attacks_per_second": 2}
    assert fight_soldiers(soldier_one=s1, soldier_two=s2) == "both soldiers die"

    try:
        s1 = None
        s2 = None
        isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2), int)
    except TypeError as err:
        print(err)
        pass

    try:
        s1 = {}
        s2 = {}
        assert isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2), ValueError)
    except ValueError as err:
        print(err)
        pass

    try:
        s1 = {"damage": None, "attacks_per_second": None}
        s2 = {"damage": None, "attacks_per_second": None}
        assert isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2), ValueError)
    except TypeError as err:
        print(err)
        pass
    try:
        s1 = {"damage": -6, "attacks_per_second": 2}
        s2 = {"damage": -15, "attacks_per_second": 2}
        assert isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2))
    except ValueError as err:
        print(err)
        pass
