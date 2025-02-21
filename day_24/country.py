import turtle
import pandas
score_count = 0
guessed_states = []

screen = turtle.Screen()
turty = turtle.Turtle()
image = r"C:\Users\Bertha\Documents\UDEMY\day_24\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
country_data = pandas.read_csv(r'C:\Users\Bertha\Documents\UDEMY\day_24\50_states.csv')
remaining_states = country_data.state.to_list()

def game():
    global score_count    
    screen.title(f"{score_count}/50 U.S states game")
    get_user_guess()

def get_user_guess():
    global score_count
    while score_count!=50:
        answer_state = screen.textinput(title="guess a state", prompt="enter a states name").title().strip()
        if not answer_state:
            game()
        if answer_state == "Exit":
            remaining_states_df = pandas.DataFrame(remaining_states)
            remaining_states_df.to_csv("remaining_states.csv", mode="w")
            turtle.bye()
            break
        else: 
            check_guess(answer_state=answer_state)
    else:
        turty.penup()
        turty.goto(0,0)
        turty.pendown()
        turty.write("you win!",font=('arial',12,"bold"),align="center")



def check_guess(answer_state):
    for state in guessed_states:
        if answer_state == state:
            return game()
    check_valid_state(answer_state=answer_state)

def check_valid_state(answer_state):
    for state in country_data.state:
        if state == answer_state:
            chosen_country_data = (country_data[country_data.state == answer_state])
            x = chosen_country_data.iloc[0].x
            y = chosen_country_data.iloc[0].y
            display_state(x,y,answer_state=answer_state)
    game()  

def display_state(x,y,answer_state):
    global score_count
    turty.penup()
    turty.goto(x=x,y=y)
    turty.pendown()
    turty.write(answer_state,align='center',font=('arial',12,"normal"))
    index = remaining_states.index(answer_state)
    remaining_states.pop(index)
    score_count+=1
    
    

game()
turtle.mainloop()
