import SpriteKit

class Start : Tile {
   var count = 0

   override init(position: CGPoint, rectOf size: CGSize) {
       super.init(position: position, rectOf: size)
       self.fillColor = .brown
   }

   required init?(coder aDecoder: NSCoder) {
       fatalError("init(coder:) has not been implemented")
   }
}
