from enum import Enum


class Colours(Enum):
    WHITE = "white"
    BLACK = "black"

class Directions(Enum):
    RIGHT = "Right"
    LEFT = "Left"
    UP = "Up"
    DOWN = "Down"

class Tags(Enum):
    FOOD = "food"
    SNAKE = "snake"
    SCORE = "score"
