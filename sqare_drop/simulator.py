from player import Player
from field import Field


class Option:
    def __init__(self, width: int = 5, height: int = 5, num_players: int = 4, initial_pos=[(1, 1), (1, 5), (5, 5), (5, 1)], max_turn=30):
        self.width = width
        self.height = height
        self.num_players = num_players
        self.initial_pos = initial_pos
        if(len(initial_pos) != num_players):
            raise Exception("initial_posとnum_playersの数が合ってません")


def start(option=Option()):
    # json用の辞書を生成
    json = {}
    # フィールド生成
    field = Field(option)
    # プレイヤー生成
    players = [Player(i, option) for i in range(option.num_players)]
    # シミュレーション実行
    json = run(option.max_turn, field, players, json)
    # JSON出力
    save_json(option, json)


def get_next_actions(players, field):
    # playersのaction()を実行
    pass


def step(next_actions):
    # next_actionを実行しfieldとplayerのフィールドを更新
    # 終了条件を満たしたかを返す
    pass


def check_finish():
    # 終了条件を満たしたかを返す
    pass


def run(max_turn: int, field: Field, players: list, json: dict):
    for i in range(max_turn):

        # 4人分の状態を生成

        # 4人分の行動を収集
        next_actions = get_next_actions()

        # 行動を反映
        step(next_actions)

        # 終了時の処理
        if check_finish():
            break

        # JSONへ保存


def save_json(option, json):
    pass
