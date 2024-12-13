import menu
from menu import*
from tkinter import *

def set_status(text, color='black'):
    canvas.itemconfig(text_id, text=text, fill=color)

def key_handler(event):
    if event.keycode == KEY_UP or event.keycode == KEY_UP_2:
        menu.menu_up(canvas)
    if event.keycode == KEY_DOWN or event.keycode == KEY_DOWN_2:
        menu.menu_down(canvas)
    if event.keycode == KEY_ENTER:
        menu.menu_enter(canvas, player1, player2, text_id)

    if game_over:
        return

    if event.keycode == KEY_PAUSE or event.keycode == KEY_PAUSE_2:
        menu.pause_toggle()
        set_status('Пауза!')

    if menu.pause:
        return

    if event.keycode == KEY_ESC:
        menu.menu_toggle(canvas)

    if menu_mode:
        return

    set_status('Вперед!')

    if event.keycode == KEY_PLAYER1:
        canvas.move(player1, SPEED, 0)
    if event.keycode == KEY_PLAYER2:
        canvas.move(player2, SPEED, 0)

    check_finish()

def check_finish():
    global game_over
    coords_player1 = canvas.coords(player1)
    coords_player2 = canvas.coords(player2)
    coords_finish = canvas.coords(finish_id)

    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]

    if x1_right >= x_finish:
        set_status('Победа верхнего игрока', player1_color)
        game_over = True

    if x2_right >= x_finish:
        set_status('Победа нижнего игрока', player2_color)
        game_over = True

game_width = menu.game_width
game_height = menu.game_height
menu_mode = menu.menu_mode
menu_options = menu.menu_options
menu_current_index = menu.menu_current_index
menu_options_id = menu.menu_options_id

KEY_UP = menu.KEY_UP
KEY_UP_2 = menu.KEY_UP_2
KEY_DOWN = menu.KEY_DOWN
KEY_DOWN_2 = menu.KEY_DOWN_2
KEY_ESC = menu.KEY_ESC
KEY_ENTER = menu.KEY_ENTER

player_size = menu.player_size
x1, y1 = menu.x1, y1
x2, y2 = x1, y1 + player_size + 100
player1_color = menu.player1_color
player2_color = menu.player2_color

x_finish = game_width - 50

KEY_PLAYER1 = menu.KEY_PLAYER1
KEY_PLAYER2 = menu.KEY_PLAYER2
KEY_PAUSE = menu.KEY_PAUSE
KEY_PAUSE_2 = menu.KEY_PAUSE_2
SPEED = menu.SPEED

game_over = menu.game_over
pause = menu.pause
window = Tk()
window.title('DMEC')
canvas = Canvas(window, width=game_width, height=game_height, bg='white')
canvas.pack()

player1 = canvas.create_rectangle(x1,
                                  y1,
                                  x1 + player_size,
                                  y1 + player_size,
                                  fill=player1_color)
player2 = canvas.create_rectangle(x2,
                                  y2,
                                  x2 + player_size,
                                  y2 + player_size,
                                  fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')
text_id = canvas.create_text(x1,
                             game_height - 50,
                             anchor=SW,
                             font=('Arial', '25'),
                             text='Вперед!')

window.bind('<KeyRelease>', key_handler)

window.mainloop()