from pico2d import clear_canvas, get_events, load_image, update_canvas
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_ESCAPE, SDL_KEYDOWN, SDL_QUIT

import game_framework
import game_world
import play_mode


image = None
ITEM_SELECT_IMAGE = 'item_select.png'
CANVAS_CENTER = (400, 300)
NO_BALL = 0
SMALL_BALL = 21
LARGE_BALL = 41
ITEM_SIZES = {
    SDLK_0: NO_BALL,
    SDLK_1: SMALL_BALL,
    SDLK_2: LARGE_BALL,
}


def init():
    global image
    image = load_image(ITEM_SELECT_IMAGE)


def finish():
    global image
    image = None


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(*CANVAS_CENTER)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type != SDL_KEYDOWN:
            continue
        if event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            return
        if event.key in ITEM_SIZES:
            play_mode.boy.set_ball_size(ITEM_SIZES[event.key])
            game_framework.pop_mode()
            return
