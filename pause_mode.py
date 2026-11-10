from pico2d import *
import game_framework
import game_world


message_font = load_font('C:\\Windows\\Fonts\\malgun.ttf', 40)


def init():
    pass


def finish():
    pass


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    message_font.draw(400, 280, '일시정지 중', (255, 255, 255))
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type != SDL_KEYDOWN:
            continue
        if event.key == SDLK_p:
            game_framework.pop_mode()
            return
        if event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return
