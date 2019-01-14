import UIKit
import SpriteKit
import GameplayKit

class GameViewController: UIViewController {
    var skView = SKView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.skView.frame = self.view.frame
        self.skView.ignoresSiblingOrder = true
        self.skView.showsFPS = true
        self.skView.showsNodeCount = true
        
        let scene = GameScene(size: skView.frame.size)
        scene.scaleMode = .aspectFill

        self.skView.presentScene(scene)
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
