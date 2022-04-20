import square_paint
import random

UP, RIGHT, DOWN, LEFT, STAY = 0, 1, 2, 3, 4


def user_code(field, my_pos, others_pos):
    return random.randrange(0, 4)

json = {

    
}
print(square_paint.start(square_paint.Option.fromJSONDict(json,[user_code]*4,[{"name":"name","icon":""}]*4)))

