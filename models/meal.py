class Meal:
    def __init__(self, id, name, description, meal_time, situation=True) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.meal_time = meal_time
        self.situation = situation

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "meal_time": self.meal_time,
            "situation": self.situation
        }