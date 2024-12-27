import random
import tkinter as tk

from os import path

from enumerators import Colours, Directions, Tags

WINDOW_POSITION = "+500+100"
SNAKE_IMG_PATH = path.join(path.abspath(path.dirname(__file__)), 'assets', 'snake.png')
FOOD_IMG_PATH = path.join(path.abspath(path.dirname(__file__)), 'assets', 'food.png')
MOVE_INCREMENT = 20
moves_per_second = 15
GAME_SPEED = 1000 // moves_per_second


class Snake(tk.Canvas):
    
    def __init__(self):
        super().__init__(width=600, height=620, background=Colours.BLACK.value, highlightthickness=0)

        self.snake_coordinates = [(100, 100), (80, 100), (60, 100)]
        self.food_coordinates = self._generate_food()
        self.score = 0
        self.direction= Directions.RIGHT.value

        self._load_assets()
        self._create_objects()
        
        self.bind_all('<Key>', self._determine_direction)
        self.after(GAME_SPEED, self._perform_actions)

    def _load_assets(self):
        try:
            self.snake_image = tk.PhotoImage(file=SNAKE_IMG_PATH)
            self.food_image = tk.PhotoImage(file=FOOD_IMG_PATH)
        except IOError as e:
            print(e)
            return
        
    def _create_objects(self):
        for x_position, y_position in self.snake_coordinates:
            self.create_image(x_position, y_position, image=self.snake_image, tag=Tags.SNAKE.value)

        self.create_image(*self.food_coordinates, image=self.food_image, tag=Tags.FOOD.value)

        self.create_text(50, 15, text=f'Score: {self.score}', fill=Colours.WHITE.value, font=('TkDefaultFont', 16), tag=Tags.SCORE.value)

        self.create_text(300, 15, text='Snake Game', fill=Colours.WHITE.value, font=('TkDefaultFont', 16))

        self.create_rectangle(10, 30, 590, 610, outline=Colours.WHITE.value)

    def _perform_actions(self):
        if self._detect_collision():
            self._end_caption()
            return
        
        self._detect_food()
        self._move_snake()
        self.after(GAME_SPEED, self._perform_actions)

    def _move_snake(self):
        x_position, y_position = self.snake_coordinates[0]

        match self.direction:
            case Directions.RIGHT.value:
                x_position += MOVE_INCREMENT
            case Directions.LEFT.value:
                x_position -= MOVE_INCREMENT
            case Directions.UP.value:
                y_position -= MOVE_INCREMENT
            case Directions.DOWN.value:
                y_position += MOVE_INCREMENT

        new_head = (x_position, y_position)

        self.snake_coordinates.insert(0, new_head)
        self.snake_coordinates.pop()

        for snake_coords, new_coords in zip(self.find_withtag(Tags.SNAKE.value), self.snake_coordinates):
            self.coords(snake_coords, new_coords)

    def _determine_direction(self, e):
        new_direction = e.keysym

        opposites = ({Directions.RIGHT.value, Directions.LEFT.value}, {Directions.UP.value, Directions.DOWN.value})
        if {new_direction, self.direction} not in opposites:
            self.direction = new_direction

    def _detect_collision(self):
        x_position, y_position = self.snake_coordinates[0]

        if (not 0 < x_position < 600 or not 20 < y_position < 620) or \
           ((x_position, y_position) in self.snake_coordinates[1:]):
            return True
        
        return False
    
    def _end_caption(self):
        self.delete(tk.ALL)

        self.create_text(300, 300, text=f'Your score is: {self.score}', fill=Colours.WHITE.value, font=("TkDefaultFont", 24))

    def _detect_food(self):
        snake_head = self.snake_coordinates[0]

        if snake_head == self.food_coordinates:

            new_segment = self.snake_coordinates[-1]
            self.snake_coordinates.append(new_segment)
            self.create_image(*new_segment, image=self.snake_image, tag=Tags.SNAKE.value)

            self.score += 1
            score_object = self.find_withtag(Tags.SCORE.value)
            self.itemconfig(score_object, text=f'Score: {self.score}')

            self.food_coordinates = self._generate_food()
            food_object = self.find_withtag(Tags.FOOD.value)
            self.coords(food_object, self.food_coordinates)

    def _generate_food(self):
        while True:
            x_position = random.randint(1, 29) * MOVE_INCREMENT
            y_position = random.randint(2, 30) * MOVE_INCREMENT
            food_position = (x_position, y_position)

            if food_position not in (self.snake_coordinates):
                return food_position



if __name__ == "__main__":
    root = tk.Tk()
    root.title('Snake')
    root.geometry(WINDOW_POSITION)
    root.resizable(False, False)

    border = Snake()
    border.pack()

    root.mainloop()