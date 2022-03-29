import sqare_paint
import random
UP,RIGHT,DOWN,LEFT,STAY =0,1,2,3,4

def user_code(field,my_pos,others_pos):
    return random.randrange(0,4)


exec("""def error_code(a,b,c):
    list = [1,2,3,4]
    return list[9]
""")
code = [user_code,user_code,user_code,error_code]
op = sqare_paint.Option(
    num_players=4 ,
    user_code=code,
    json_path="input.json"
    )

dict_json = sqare_paint.start(op)
