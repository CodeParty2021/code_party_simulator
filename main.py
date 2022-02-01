import sqare_paint

UP,RIGHT,DOWN,LEFT,STAY =0,1,2,3,4

#TODO: user_codeの引数を分解する
def user_code(state):
    return RIGHT

op = sqare_paint.Option(
    num_players=1 ,
    user_code=[user_code],
    initial_pos=[(0,0)]
    )

sqare_paint.start(op)
