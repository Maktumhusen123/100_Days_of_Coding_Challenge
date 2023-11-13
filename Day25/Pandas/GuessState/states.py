import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click(x, y):
#    print(x, y)

# turtle.onscreenclick(get_mouse_click)
guessed_states = []
to_learn = []
data = pandas.read_csv("states.csv")
# print(data["state"])
state_list = data["state"].to_list()
while len(guessed_states) < len(state_list):
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/{len(state_list)} States Correct", prompt="What's "
                                                                                                             "another "
                                                                                                             "city"
                                                                                                             " name?")).title()
    # print(answer_state)
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    if answer_state == "Exit":
        for state in state_list:
            if state not in guessed_states:
                to_learn.append(state)
        pandas.DataFrame(to_learn).to_csv("states_to_learn.csv")
        break

turtle.mainloop()
