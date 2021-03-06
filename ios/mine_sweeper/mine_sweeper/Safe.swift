import SpriteKit

class Safe : Tile {
   var count = 0

   override init(position: CGPoint, rectOf size: CGSize) {
       super.init(position: position, rectOf: size)
       self.fillColor = .white

       let label = SKLabelNode(text: String(self.count)).apply { l in
           l.fontName = "Menlo"
           l.fontSize = CGFloat(self.rect.width)
           l.fontColor = .black
           l.verticalAlignmentMode = .center
           l.horizontalAlignmentMode = .center
           l.position = CGPoint(x: self.rect.width / 2, y: self.rect.height / 2)
       }
       self.addChild(label)
   }

   required init?(coder aDecoder: NSCoder) {
       fatalError("init(coder:) has not been implemented")
   }
}
