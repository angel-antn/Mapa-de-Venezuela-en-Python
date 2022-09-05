from turtle import Turtle, Screen
import pandas

IMAGE_PATH = 'Venezuela.gif'
FONT = ("Helvetica", 12, "normal")

screen = Screen()
screen.title('Venezuela states')
screen.addshape(IMAGE_PATH)
screen.setup(width=758, height=600)
screen.tracer(0)

venezuelan_map = Turtle(shape=IMAGE_PATH)
turtle = Turtle()
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv('venezuela_states.csv')
states = data['States'].tolist()
guesses = []

while len(guesses) < 24:
    screen.update()
    try:
        answer_state = screen.textinput(title=f'Estados: {len(guesses)}/24',
                                        prompt="Ingrese el nombre de un estado:").capitalize()
    except AttributeError:
        break

    if answer_state == 'Distrito capital':
        answer_state = 'Dc'

    if answer_state not in guesses and answer_state in states:
        x = int(data[data.States == answer_state]['X'])
        y = int(data[data.States == answer_state]['Y'])
        turtle.goto(x, y)
        turtle.write(arg=answer_state, align='center', font=FONT)
        guesses.append(answer_state)

turtle.goto(x=0, y=270)
if len(guesses) == 24:
    turtle.write(arg='Has acertado los 24 estados de Venezuela!', align='center', font=FONT)
else:

    for i in states:
        if i in guesses:
            states.pop(states.index(i))

    states_left = {'Estados a repasar': states}
    data_left = pandas.DataFrame(states_left)
    data_left.to_csv('Check_the_missing_states.csv')

    turtle.write(arg='Archivo generado con los estados faltantes', align='center', font=FONT)
    turtle.goto(x=0, y=250)
    turtle.write(arg='Revisalos y vuelve a intentarlo cuando estes preparado', align='center', font=FONT)

screen.exitonclick()
