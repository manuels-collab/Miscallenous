import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

tim = turtle.Turtle()
tim.hideturtle()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = (screen.textinput(title=f"Guess the state: {len(guessed_state)}/50", prompt="What's another state's name")).title()
    csv_file = pandas.read_csv("50_states.csv")
    file = (csv_file[csv_file.state == answer_state])
    try:
        if answer_state == 'Exit':
            unguessed_state = [state for state in csv_file.state  if state not in  guessed_state]
            new_data = pandas.DataFrame(unguessed_state)
            new_data.to_csv(f"{len(unguessed_state)}States_to_learn.csv")

        if [csv_file.state == answer_state]:
            guessed_state.append(answer_state)
            tim.penup()
            tim.goto(file.x.item(), file.y.item())
            tim.pendown()
            tim.write(answer_state)
            if guessed_state == 50:
                print("You won")
    except ValueError:
        print("No more")
screen.exitonclick()


