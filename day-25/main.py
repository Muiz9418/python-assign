"""
Day 25 - US States Game
Shows a blank map, the player types a state name, and if correct
its name is stamped on the map at the right coordinates. Progress
is saved to a CSV of missed states at the end.
"""
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # background map image, not included here
screen.addshape(image)
turtle.Turtle().shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                     prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)

screen.exitonclick()
