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
def compute_soldier_dps(soldier: dict)->int:
    damage = soldier["damage"]
    attacks_per_second = soldier["attacks_per_second"]

    if isinstance(damage, bool) or not isinstance(damage, int):
        raise TypeError("damage must be an integer.")
    
    if isinstance(damage, bool) or not isinstance(attacks_per_second, int):
        raise TypeError("attacks_per_second must be an integer.")
    
    if damage < 0:
        raise ValueError("damage must be 0 or more")
    
    if attacks_per_second < 0:
        raise ValueError("attacks_per_second must be 0 or more.")
    
    return damage * attacks_per_second


def fight_soldiers(soldier_one:dict, soldier_two:dict)->str:
    if not isinstance(soldier_two, dict) or not isinstance(soldier_one, dict):
        raise TypeError("solder_one and soldier_two args must be 'dict' objects.")

    if not soldier_one:
        raise ValueError("soldier_one 'dict' is empty!")
    
    if not soldier_two:
        raise ValueError("soldier_two 'dict' is empty!")

    soldier_one_dps = compute_soldier_dps(soldier_one)
    soldier_two_dps = compute_soldier_dps(soldier_two)

    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"

    if soldier_one_dps < soldier_two_dps:
        return "soldier 2 wins"

    return "both soldiers die"


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
        isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2), TypeError)
    except TypeError as err:
        print(f"TypeError: {err}.")
        pass

    try:
        s1 = {}
        s2 = {}
        assert isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2), ValueError)
    except ValueError as err:
        print(f"ValueError: {err}")
        pass

    try:
        s1 = {"damage": None, "attacks_per_second": None}
        s2 = {"damage": None, "attacks_per_second": None}
        assert isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2), TypeError)
    except TypeError as err:
        print(f"TypeError: {err}.")
        pass
    try:
        s1 = {"damage": -6, "attacks_per_second": 2}
        s2 = {"damage": -15, "attacks_per_second": 2}
        assert isinstance(fight_soldiers(soldier_one=s1, soldier_two=s2))
    except ValueError as err:
        print(f"ValueError: {err}.")
        pass