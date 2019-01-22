import SpriteKit
import GameplayKit

class GameScene: SKScene {
    private var label : SKLabelNode?

    override func didMove(to view: SKView) {
        let cellSize = self.frame.width / 11

        var cells = [SKShapeNode]()
        for y in 0...10 {
            for x in 0...10 {
                let cell = SKShapeNode(rectOf: CGSize(width: cellSize, height: cellSize))
                if (y == 0 && x == 5) || (y == 10 && x == 5) {
                    cell.position = CGPoint(x: cellSize * CGFloat(x) + cellSize / 2, y: cellSize * CGFloat(y) + cellSize / 2 + self.frame.height / 4)
                    cell.fillColor = .brown
                } else if y == 0 || y == 10 || x == 0 || x == 10 {
                    cell.position = CGPoint(x: cellSize * CGFloat(x) + cellSize / 2, y: cellSize * CGFloat(y) + cellSize / 2 + self.frame.height / 4)
                    cell.fillColor = .darkGray
                } else {
                    cell.position = CGPoint(x: cellSize * CGFloat(x) + cellSize / 2, y: cellSize * CGFloat(y) + cellSize / 2 + self.frame.height / 4)
                    cell.fillColor = .white

                    let label = SKLabelNode(text: String(1)).apply { l in
                        l.fontName = "Menlo"
                        l.fontSize = CGFloat(cellSize)
                        l.fontColor = .black
                        l.verticalAlignmentMode = .center
                        l.horizontalAlignmentMode = .center
                    }
                    cell.addChild(label)
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
