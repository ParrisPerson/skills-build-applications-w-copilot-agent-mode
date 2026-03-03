# 03 - UIKit Guide

## 🏗 UIViewController Lifecycle

```swift
import UIKit

class HomeViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
    }

    private func setupUI() {
        view.backgroundColor = .systemBackground
        title = "Home"
    }
}
```

---

## 🖼 Programmatic UI (No Storyboard)

```swift
class ProfileViewController: UIViewController {

    // MARK: - UI Components
    private let nameLabel: UILabel = {
        let label = UILabel()
        label.font = .systemFont(ofSize: 24, weight: .bold)
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

    private let actionButton: UIButton = {
        let button = UIButton(type: .system)
        button.setTitle("Edit Profile", for: .normal)
        button.backgroundColor = .systemBlue
        button.setTitleColor(.white, for: .normal)
        button.layer.cornerRadius = 10
        button.translatesAutoresizingMaskIntoConstraints = false
        return button
    }()

    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        view.addSubview(nameLabel)
        view.addSubview(actionButton)
        setupConstraints()
        actionButton.addTarget(self, action: #selector(editProfileTapped), for: .touchUpInside)
    }

    // MARK: - Setup
    private func setupConstraints() {
        NSLayoutConstraint.activate([
            nameLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            nameLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 24),
            nameLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -24),

            actionButton.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 24),
            actionButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            actionButton.widthAnchor.constraint(equalToConstant: 200),
            actionButton.heightAnchor.constraint(equalToConstant: 50)
        ])
    }

    // MARK: - Actions
    @objc private func editProfileTapped() {
        print("Edit Profile tapped")
    }
}
```

---

## 📋 UITableView

```swift
class TaskListViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {

    private let tableView = UITableView()
    private var tasks: [String] = ["Buy groceries", "Write code", "Go for a run"]

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.frame = view.bounds
        tableView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "TaskCell")
        view.addSubview(tableView)
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        tasks.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "TaskCell", for: indexPath)
        cell.textLabel?.text = tasks[indexPath.row]
        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        print("Selected: \(tasks[indexPath.row])")
    }
}
```

---

## 🧭 Navigation

```swift
// Push
let detailVC = DetailViewController()
navigationController?.pushViewController(detailVC, animated: true)

// Present modally
let navController = UINavigationController(rootViewController: SettingsViewController())
present(navController, animated: true)

// Dismiss / Pop
dismiss(animated: true)
navigationController?.popViewController(animated: true)
```

---

## 🏁 SceneDelegate Entry Point (No Storyboard)

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options: UIScene.ConnectionOptions) {
        guard let windowScene = (scene as? UIWindowScene) else { return }
        let rootVC = HomeViewController()
        let navController = UINavigationController(rootViewController: rootVC)
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = navController
        window?.makeKeyAndVisible()
    }
}
```
