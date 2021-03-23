from flask import jsonify
from .models import *
from . import create_app
import logging
from sqlalchemy import and_

logging.basicConfig(level=logging.DEBUG)
app = create_app()

@app.route('/')
@app.route('/menu/<string:date>/<string:meal_type>', methods=['GET'])
def get_food(date, meal_type):
  """get all meals of a certain type available on a specific date"""

  requested_date = datetime.datetime.strptime(date, "%Y-%m-%d")

  # Find the week id for the given date.
  week = Week.query.filter(Week.end_date >= requested_date, Week.start_date <= requested_date).first()

  if (week is None):
    return jsonify({"error": "Cannot access resource. Week ID does not exist."}), 404

  # Query available meals for the given week.
  available_meals = MealWeek.query.filter_by(week_id=week.id).all()

  if (available_meals is None):
    return jsonify({"error": "Cannot access resource. There are no available meals for this week."}), 404

  # Filter available meals by meal_type requested.
  available_meal_ids_list = [m.meal.name for m in available_meals if m.meal.type == meal_type]
  
  if (len(available_meal_ids_list) == 0):
    return jsonify({"error": "Cannot access resource. No available meals for this week fit the meal type."}), 404

  return jsonify(available_meal_ids_list)
