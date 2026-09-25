class Objects:
    """Registers objects by (id, class), counting how many and storing the distances."""

    # {"(id, class)": {"quantity": int, "distances": [float, ...]}}
    _registry = {}

    def __init__(self, id, obj_class, distance):
        self.id = id
        self.obj_class = obj_class
        self.distance = distance

        key = (id, obj_class)   # tuple = composite key

        if key in Objects._registry:
            # Same id AND same class → increment and append the distance
            Objects._registry[key]["quantity"] += 1
            Objects._registry[key]["distances"].append(distance)
        else:
            # New combination → create with 1 and the list with the first distance
            Objects._registry[key] = {
                "quantity": 1,
                "distances": [distance]
            }

    @classmethod
    def quantity(cls, id, obj_class):
        """Returns how many objects with this (id, class) exist."""
        return cls._registry.get((id, obj_class), {}).get("quantity", 0)

    @classmethod
    def distances(cls, id, obj_class):
        """Returns the list of distances for this (id, class)."""
        return cls._registry.get((id, obj_class), {}).get("distances", [])

    def __repr__(self):
        return f"Objects(id={self.id}, class={self.obj_class}, distance={self.distance})"


# ---- Testing ----
Objects(1, "A", 10.5)
Objects(1, "A", 15.3)   # same id AND class → increments
Objects(1, "B", 20.0)   # same id, different class → new entry
Objects(2, "A", 8.7)    # different id, same class → new entry
Objects(1, "A", 5.0)    # same id AND class → increments
Objects(1, "B", 33.2)   # same id AND class → increments
Objects(2, "A", 9.7) 


print(Objects.quantity(1, "A"))   # 3
print(Objects.distances(1, "A"))  # [10.5, 15.3, 5.0]
print(Objects.quantity(1, "B"))   # 2
print(Objects.distances(1, "B"))  # [20.0, 33.2]
print(Objects.quantity(2, "A"))  # 1
print(Objects.distances(2, "A"))  