from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Week(db.Model):
  __tablename__ = "week"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  start_date = db.Column(db.DateTime, nullable=False)
  end_date = db.Column(db.DateTime, nullable=False)

  week = db.relationship("MealWeek", back_populates="week")

class Meal(db.Model):
  __tablename__ = "meal"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(500), unique=False, nullable=False)
  type = db.Column(db.String(500), unique=False, nullable=False)

  meal = db.relationship("MealWeek", back_populates="meal")

  def __repr__(self):
    return self.name

class MealWeek(db.Model):
  __tablename__ = "meal_week"

  week_id = db.Column(db.Integer, db.ForeignKey('week.id'), primary_key=True)
  meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), primary_key=True)

  week = db.relationship("Week", back_populates="week")
  meal = db.relationship("Meal", back_populates="meal")
