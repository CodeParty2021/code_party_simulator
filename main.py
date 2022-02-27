import sqare_paint
import random
UP,RIGHT,DOWN,LEFT,STAY =0,1,2,3,4

def user_code(field,my_pos,others_pos):
    return random.randrange(0,4)

op = sqare_paint.Option(
    num_players=4 ,
    user_code=[user_code for i in range(4)],
    json_path="input.json"
    )

dict_json = sqare_paint.start(op)
