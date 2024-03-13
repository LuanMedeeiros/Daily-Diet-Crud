class Meal:
    def __init__(self, id, description, meal_time, situation) -> None:
        self.id = id
        self.description = description
        self.meal_time = meal_time
        self.situation = situation

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "meal_time": self.meal_time,
            "situation": self.situation
        }