from flask import Flask, request, jsonify
from models.meal import Meal

app = Flask(__name__)

meals = []
meal_id_control = 1

@app.route('/meals', methods=['POST'])
def create_meal():
    global meal_id_control
    data = request.get_json()
    new_meal = Meal(id=meal_id_control, name=data['name'], description=data['description'], meal_time=data['meal_time'], situation=data['situation'])
    meal_id_control += 1
    meals.append(new_meal)
    print(meals)
    return jsonify({"message": "Nova refeição adicionada com sucesso.", "id":new_meal.id})


if __name__ == "__main__":
    app.run(debug=True)


