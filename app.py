from flask import Flask, request, jsonify
from models.meal import Meal

app = Flask(__name__)

meals = []
meal_id_control = 1

@app.route('/meals', methods=['POST'])
def create_meal():
    global meal_id_control
    data = request.get_json()
    new_meal = Meal(id=meal_id_control, description=data['description'], meal_time=data['meal_time'], situation=data['situation'])
    meal_id_control += 1
    meals.append(new_meal)
    print(meals)
    return jsonify({"message": "Nova refeição adicionada com sucesso.", "id":new_meal.id})

@app.route('/meals', methods=['GET'])
def get_meals():
    meals_list = [meal.to_dict() for meal in meals]

    output = {
        "meals": meals_list,
        "total_meals": len(meals_list)
    }
    return jsonify(output)

@app.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    for m in meals:
        if m.id == id:
            return jsonify(m.to_dict())
    return jsonify({"message": "Não foi possivel encontrar a refeição"}), 404

@app.route('/meals/<int:id>', methods=['PUT'])
def update_meal(id):
    meal = next((m for m in meals if m.id == id), None)
    if meal is None:
        return jsonify({"message": "Não foi possível encontrar a refeição"}), 404

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    meal_time = data.get('meal_time')

    if title is not None:
        meal.title = title
    if description is not None:
        meal.description = description
    if meal_time is not None:
        meal.meal_time = meal_time

    return jsonify({"message": "Refeição atualizada com sucesso"})

@app.route('/meals/<int:id>', methods=['DELETE'])
def delete_meal(id):
   meal = None
   for m in meals:
      if m.id == id:
          meal = m
          break

   if not meal:
      return jsonify({"message": "Não foi possivel encontrar a refeição"}), 404
   
   meals.remove(meal)
   return jsonify({"message": "Refeição deletade com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)


