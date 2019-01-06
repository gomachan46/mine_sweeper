from canvas import Canvas
from scenes.scene import Scene


class PlayerViewer(Scene):
    def draw(self):
        Canvas.store_main([
            '選手名鑑',
            '======',
        ])
        from game import Game
        if len(Game.data['cleared_players']) == 0:
            Canvas.store_main(['まだ登録されていません'])
            return

        for cleared_player in Game.data['cleared_players']:
            Canvas.store_main([
                f'名前: {cleared_player.name}',
                f'攻撃力: {cleared_player.attack}',
                f'防御力: {cleared_player.defence}',
                '======'
            ])
        Canvas.store_main(['キー入力でタイトルへ戻ります'])

    def next(self, _):
        from scenes.title import Title
        return Title()
