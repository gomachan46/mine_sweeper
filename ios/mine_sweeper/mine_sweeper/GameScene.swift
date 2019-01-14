import SpriteKit
import GameplayKit

class GameScene: SKScene {
    private var label : SKLabelNode?

    override func didMove(to view: SKView) {
        let cellSize = UIScreen.main.bounds.size.width / 10

        var cells = [SKShapeNode]()
        for y in 0...9 {
            for x in 0...9 {
                let cell = SKShapeNode(rectOf: CGSize(width: cellSize, height: cellSize)).apply { c in
                    c.position = CGPoint(x: cellSize * CGFloat(x) + cellSize / 2, y: cellSize * CGFloat(y) + cellSize / 2 + self.frame.height / 4)
                    c.fillColor = .white

                    let label = SKLabelNode(text: String(1)).apply { l in
                        l.fontName = "Menlo"
                        l.fontSize = CGFloat(cellSize)
                        l.fontColor = .black
                        l.verticalAlignmentMode = .center
                        l.horizontalAlignmentMode = .center
                    }
                    c.addChild(label)
                }
                cells.append(cell)
            }
        }
        cells.forEach { self.addChild($0) }
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
