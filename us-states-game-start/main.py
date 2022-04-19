import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start\states_image.gif"
screen.addshape(image)
turtle.shape(image)
guessed = 0

data = pandas.read_csv("us-states-game-start\q_states.csv")
data_list = data
def get_mouse_click(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click)

states = data.state.to_list()
x_coor = data.x.to_list()
y_coor = data.y.to_list()
guessed_states = []

while guessed_states != 50:
    user_answer = screen.textinput(title=f"States guessed {guessed}/{len(states)}", prompt="What is another state?").title()

    if user_answer == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    
    if user_answer in states:
        guessed_states.append(user_answer)
        x = x_coor[states.index(user_answer)]
        y = y_coor[states.index(user_answer)]
        if guessed_states.count(user_answer) == 1: 
            guessed += 1
        name = turtle.Turtle()
        name.speed("fastest")
        name.hideturtle()
        name.pu()
        name.goto(x, y)
        name.write(user_answer, align="center", font=("Arial",8, "normal"))

    if guessed == 50:
        game_on = False
        print("You have successfully guessed all the states!")


turtle.mainloop()