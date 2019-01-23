import SpriteKit
import GameplayKit

class GameScene: SKScene {
    private var label : SKLabelNode?

    override func didMove(to view: SKView) {
        let tileLength = self.frame.width / 11

        var tiles = [Tile]()
        for y in 0...10 {
            for x in 0...10 {
                let position = CGPoint(x: tileLength * CGFloat(x), y: tileLength * CGFloat(y) + self.frame.height / 4)
                let size = CGSize(width: tileLength, height: tileLength)
                let tile : Tile
                if y == 0 && x == 5  {
                    tile = Start(position: position, rectOf: size)
                } else if y == 10 && x == 5 {
                    tile = Goal(position: position, rectOf: size)
                } else if y == 0 || y == 10 || x == 0 || x == 10 {
                    tile = Wall(position: position, rectOf: size)
                } else {
                    tile = Safe(position: position, rectOf: size)
                }
                tiles.append(tile)
            }
        }
        tiles.forEach { self.addChild($0) }
    }

    func touchDown(atPoint pos : CGPoint) {
    }
    
    func touchMoved(toPoint pos : CGPoint) {
    }
    
    func touchUp(atPoint pos : CGPoint) {
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        for t in touches { self.touchDown(atPoint: t.location(in: self)) }
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        for t in touches { self.touchMoved(toPoint: t.location(in: self)) }
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        for t in touches { self.touchUp(atPoint: t.location(in: self)) }
    }
    
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        for t in touches { self.touchUp(atPoint: t.location(in: self)) }
    }
    
    override func update(_ currentTime: TimeInterval) {
        // Called before each frame is rendered
    }
}
