import square_paint
import random

UP, RIGHT, DOWN, LEFT, STAY = 0, 1, 2, 3, 4


def user_code(field, my_pos, others_pos):
    return random.randrange(0, 4)


json = {"num_players":1,"initial_pos":[(0,0)],"clear_rule": {"type": "fill", "payload": {"N": 1}},}
option= square_paint.Option.fromJSONDict(
            json, [user_code] * 1, [{"name": "ぼっち太郎", "icon": ""}] * 1
        )
option.json_path = "./input.json"
print(
    square_paint.start(
        option
    )
)
