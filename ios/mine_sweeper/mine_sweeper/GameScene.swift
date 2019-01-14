import SpriteKit
import GameplayKit

class GameScene: SKScene {
    private var label : SKLabelNode?

    override func didMove(to view: SKView) {
        if let label = self.label {
            self.addChild(label)
        }

        let cellSize = CGSize(width: 40, height: 40)
        let cell = SKShapeNode(rectOf: cellSize).apply { c in
            c.position = CGPoint(x: self.size.width / 2, y: self.size.height / 2)
            c.fillColor = .white

            let label = SKLabelNode(text: "1").apply { l in
                l.fontName = "Menlo"
                l.fontSize = 40
                l.fontColor = .black
                l.verticalAlignmentMode = .center
                l.horizontalAlignmentMode = .center
            }
            c.addChild(label)
        }
        self.addChild(cell)
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
