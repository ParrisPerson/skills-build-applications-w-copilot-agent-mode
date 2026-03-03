# 06 - Recommended iOS Project Structure

## 🗂 Universal Project Structure

```
MyApp/
├── MyApp.xcodeproj
├── MyApp/
│   ├── App/
│   │   ├── AppDelegate.swift
│   │   ├── SceneDelegate.swift
│   │   └── MyAppApp.swift
│   ├── Features/
│   │   ├── Auth/
│   │   │   ├── Models/
│   │   │   ├── ViewModels/
│   │   │   └── Views/
│   │   ├── Home/
│   │   │   ├── Models/
│   │   │   ├── ViewModels/
│   │   │   └── Views/
│   │   └── Profile/
│   │       ├── Models/
│   │       ├── ViewModels/
│   │       └── Views/
│   ├── Core/
│   │   ├── Network/
│   │   │   ├── NetworkManager.swift
│   │   │   ├── APIEndpoints.swift
│   │   │   └── APIError.swift
│   │   ├── Storage/
│   │   │   ├── CoreDataManager.swift
│   │   │   └── UserDefaultsManager.swift
│   │   └── Services/
│   │       ├── AuthService.swift
│   │       └── NotificationService.swift
│   ├── Shared/
│   │   ├── Components/
│   │   ├── Extensions/
│   │   └── Utilities/
│   └── Resources/
│       ├── Assets.xcassets
│       ├── Localizable.strings
│       └── Info.plist
└── Tests/
    ├── UnitTests/
    └── UITests/
```

---

## 🏛 MVVM Pattern

```
Feature/
├── Model/        → User.swift (Codable struct)
├── ViewModel/    → UserViewModel.swift (@ObservableObject)
└── View/         → UserView.swift (SwiftUI View / UIViewController)
```

---

## 📦 Swift Package Manager

Prefer SPM over CocoaPods. Add packages via Xcode → File → Add Package Dependencies.

Popular packages:
- **SDWebImage** — Image loading
- **KeychainAccess** — Secure storage
- **Lottie** — Animations

---

## 🔖 Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Files | PascalCase | `UserProfileView.swift` |
| Classes / Structs | PascalCase | `class NetworkManager` |
| Variables / Functions | camelCase | `func fetchUser()` |
| Extensions | TypeName+Feature | `String+Validation.swift` |
| Protocols | PascalCase + `-able` | `Loadable`, `UserDelegate` |

---

## 🧹 MARK Organization

```swift
class ProductViewController: UIViewController {
    // MARK: - Properties
    // MARK: - UI Components
    // MARK: - Lifecycle
    // MARK: - Setup
    // MARK: - Actions
    // MARK: - Network
}
```

---

## 🚀 Build & Test from Terminal

```bash
# Build for simulator
xcodebuild -project MyApp.xcodeproj -scheme MyApp -sdk iphonesimulator -configuration Debug build

# Run tests
xcodebuild test -project MyApp.xcodeproj -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 15'

# Clean
xcodebuild clean -project MyApp.xcodeproj -scheme MyApp
```
