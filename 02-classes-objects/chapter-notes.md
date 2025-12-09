# Chapter 2: Classes and Objects

## Overview
Classes define reusable templates for creating objects that group data (attributes) with behavior (methods). Objects are concrete instances of those templates.

## Defining a Class
```python
class Wizard:
    def __init__(self, name, mana):
        self.name = name          # attribute
        self.mana = mana          # attribute

    def cast_spell(self, cost):
        if cost <= self.mana:
            self.mana -= cost
            return f"{self.name} casts a spell!"
        return f"{self.name} is out of mana."
```
- `__init__` initializes each new object.
- `self` gives methods access to the current instance.

## Creating Objects
```python
merlin = Wizard("Merlin", 100)
morgana = Wizard("Morgana", 80)

print(merlin.cast_spell(30))   # Merlin casts a spell!
print(merlin.mana)             # 70
```
Each object keeps its own state while sharing the same behavior defined on the class.

## Expanding Behavior
```python
class Spellbook:
    def __init__(self):
        self.spells = []

    def add_spell(self, spell_name):
        self.spells.append(spell_name)

    def list_spells(self):
        return ", ".join(self.spells) or "No spells yet."
```
Objects can collaborate: a `Wizard` could hold a `Spellbook` to compose functionality.

## Key Takeaways
- Use classes to encapsulate related data and behavior.
- Objects are instantiated classes with their own state.
- Methods operate on object state through `self`.
- Composition lets classes work together to model richer domains.
