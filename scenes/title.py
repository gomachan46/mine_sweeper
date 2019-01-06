from canvas import Canvas
from scenes.player_creation import PlayerCreation
from scenes.player_viewer import PlayerViewer
from scenes.scene import Scene


class Title(Scene):
    def draw(self):
        Canvas.store_main([
            'ドキドキ地雷パニック',
            '1キー: ゲームスタート',
            '2キー: 選手名鑑',
            'Note: `exit`と入力することでいつでも終了できます',
            'Note: ベータ版につき正常に動作しない場合は.mine_sweeper/mine_sweeper.dbを削除してください'
        ])

    def next(self, key):
        if key == '1':
            return PlayerCreation()
        elif key == '2':
            return PlayerViewer()
        else:
            Canvas.store_side(['正しく入力してください'])

        return self
