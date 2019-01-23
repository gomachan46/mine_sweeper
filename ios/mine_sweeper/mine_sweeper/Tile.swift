import SpriteKit

class Tile : SKShapeNode {
    var rect : CGRect
    init(position: CGPoint, rectOf size: CGSize) {
        rect = CGRect(origin: CGPoint.zero, size: size)
        super.init()

        self.position = position
        self.path = CGPath(rect: rect, transform: nil)
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
