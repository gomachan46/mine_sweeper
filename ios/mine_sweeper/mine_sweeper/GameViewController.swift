import UIKit
import SpriteKit
import GameplayKit

class GameViewController: UIViewController {
    var skView: SKView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        skView = SKView(frame: self.view.frame)
        skView.ignoresSiblingOrder = true
        skView.showsFPS = true
        skView.showsNodeCount = true
        
        let scene = GameScene(size: skView.frame.size)
        scene.scaleMode = .aspectFill
        skView.presentScene(scene)
        self.view.addSubview(skView)
    }

    override var shouldAutorotate: Bool {
        return true
    }

    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        if UIDevice.current.userInterfaceIdiom == .phone {
            return .allButUpsideDown
        } else {
            return .all
        }
    }

    override var prefersStatusBarHidden: Bool {
        return true
    }
}
