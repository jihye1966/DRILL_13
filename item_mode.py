from pico2d import *
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_ESCAPE, SDL_KEYDOWN, SDL_QUIT

import game_framework
import game_world
import play_mode


image = None
ITEM_SIZES = {
    SDLK_0: 0,
    SDLK_1: 21,
    SDLK_2: 41,
}


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
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
            play_mode.boy.ball_size = ITEM_SIZES[event.key]
            game_framework.pop_mode()
            return
