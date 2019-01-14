import UIKit
import SpriteKit
import GameplayKit

class GameViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func viewWillLayoutSubviews() {
        super.viewWillLayoutSubviews()

        if #available(iOS 11.0, *) {
            self.view.frame = self.view.safeAreaLayoutGuide.layoutFrame
        }

        SKView().apply { this in
            this.frame = self.view.frame
            this.ignoresSiblingOrder = true
            this.showsFPS = true
            this.showsNodeCount = true

            let scene = GameScene(size: self.view.bounds.size)
            scene.scaleMode = .aspectFill
            this.presentScene(scene)
            self.view.addSubview(this)
        }
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
