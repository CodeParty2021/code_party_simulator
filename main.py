import sqare_paint

UP,RIGHT,DOWN,LEFT,STAY =0,1,2,3,4

def user_code(field,my_pos,others_pos):
    return RIGHT

op = sqare_paint.Option(
    num_players=1 ,
    user_code=[user_code],
    initial_pos=[(0,0)]
    )

dict_json = sqare_paint.start(op)
