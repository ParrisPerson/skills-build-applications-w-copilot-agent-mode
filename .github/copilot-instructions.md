# GitHub Copilot Instructions — iOS Development

## Project Context
This is an iOS application project built with **Swift**. The codebase targets **iOS 16+** and is developed using **Visual Studio Code** with the Swift extension and GitHub Copilot.

---

## Language & Platform
- **Language:** Swift 5.9+
- **Platform:** iOS 16.0+
- **Xcode:** 15+
- **Package Manager:** Swift Package Manager (SPM) — do NOT suggest CocoaPods or Carthage

---

## UI Framework Preference
- Prefer **SwiftUI** for all new views and screens
- Use **UIKit** only when SwiftUI does not support the required functionality (e.g., complex gesture recognizers, custom UICollectionViewLayout)
- When mixing UIKit and SwiftUI, use `UIHostingController` to wrap SwiftUI views inside UIKit
- Never use Storyboards or XIB files — all UI must be **programmatic**

---

## Architecture
- Use **MVVM (Model-View-ViewModel)** as the primary architecture pattern
- ViewModels must use `@ObservableObject` with `@Published` properties (SwiftUI) or delegate/closure-based bindings (UIKit)
- Keep Views free of business logic — all logic belongs in the ViewModel or Service layer
- Use dependency injection via initializers — avoid singletons unless for shared services (e.g., `NetworkManager.shared`)

---

## Swift Coding Standards

### Naming
- Use **camelCase** for variables, functions, and parameters
- Use **PascalCase** for types (classes, structs, enums, protocols)
- Protocol names should end in `-able`, `-ing`, or `-Delegate` where appropriate
- File names must match the primary type defined in them (e.g., `UserViewModel.swift`)

### Types
- Prefer **structs over classes** for models and data types
- Use **enums with associated values** for state representation (e.g., `LoadingState`)
- Use `final` on classes that are not meant to be subclassed

### Optionals
- Never force-unwrap (`!`) — always use `if let`, `guard let`, or nil coalescing (`??`)
- Prefer `guard let` over `if let` in functions to reduce nesting

### Async/Await
- Use **async/await** for all asynchronous code — avoid callbacks and Combine where async/await suffices
- Use `Task {}` to bridge async code into synchronous contexts
- Use `@MainActor` for ViewModel properties and functions that update the UI

---

## Project Structure
Follow this folder structure strictly:

```
MyApp/
├── App/                  # AppDelegate, SceneDelegate, or @main SwiftUI App
├── Features/             # One folder per feature (Auth, Home, Profile, etc.)
│   └── FeatureName/
│       ├── Models/
│       ├── ViewModels/
│       └── Views/
├── Core/
│   ├── Network/          # NetworkManager, APIEndpoints, APIError
│   ├── Storage/          # CoreData, UserDefaults, Keychain
│   └── Services/         # Business logic services
├── Shared/
│   ├── Components/       # Reusable SwiftUI views or UIKit components
│   ├── Extensions/       # Swift extensions (grouped by Type+Feature.swift)
│   └── Utilities/        # Constants, Logger, Helpers
└── Resources/            # Assets, Localizable.strings, Info.plist
```

---

## SwiftUI Guidelines
- Use `@State` for local view state
- Use `@StateObject` to own a ViewModel in a view
- Use `@ObservedObject` when a ViewModel is passed in from a parent
- Use `@EnvironmentObject` for app-wide shared state
- Use `NavigationStack` (not deprecated `NavigationView`)
- Always add `#Preview` macros for every SwiftUI view
- Use `.task {}` modifier for async data loading inside views

---

## UIKit Guidelines (when required)
- Build all UIKit UIs **programmatically** — no Storyboards
- Set `translatesAutoresizingMaskIntoConstraints = false` on every view
- Use `NSLayoutConstraint.activate([...])` for constraints
- Organize files using `// MARK: -` sections:
  - `// MARK: - Properties`
  - `// MARK: - UI Components`
  - `// MARK: - Lifecycle`
  - `// MARK: - Setup`
  - `// MARK: - Actions`
  - `// MARK: - Network`

---

## Networking
- Use `URLSession` with `async/await` — do NOT suggest third-party HTTP libraries unless asked
- All API responses must conform to `Codable`
- Define custom error types conforming to `Error` and `LocalizedError`
- Use a generic `NetworkManager` with a `request<T: Codable>(_ endpoint:) async throws -> T` pattern

---

## Testing
- Use **XCTest** for unit tests
- Use **XCUITest** for UI tests
- Test ViewModels independently from Views
- Mock network calls using protocol-based dependency injection
- Name test functions: `test_<methodName>_<condition>_<expectedResult>`

---

## Accessibility
- Always add `.accessibilityLabel()` and `.accessibilityHint()` to interactive SwiftUI elements
- Use semantic colors (`Color(.systemBackground)`, `.primary`, `.secondary`) — never hardcode hex colors
- Support **Dynamic Type** — use `.font(.body)` and relative font styles, not fixed sizes

---

## Localization
- All user-facing strings must use `NSLocalizedString` or `String(localized:)`
- Never hardcode display strings directly in views

---

## Documentation
- Add `///` doc comments to all public functions, classes, and structs
- Follow Apple's documentation style
- Example:
  ```swift
  /// Fetches the user profile from the remote API.
  /// - Parameter userID: The unique identifier of the user.
  /// - Returns: A `User` model decoded from the API response.
  /// - Throws: `APIError.notFound` if the user does not exist.
  func fetchUser(userID: String) async throws -> User
  ```

---

## What to Avoid
- ❌ No Storyboards or XIB files
- ❌ No force unwrapping (`!`)
- ❌ No CocoaPods — use SPM only
- ❌ No `DispatchQueue.main.async` when `@MainActor` or `.task` can be used
- ❌ No hardcoded colors, fonts, or strings
- ❌ No `NavigationView` — use `NavigationStack`
- ❌ No massive ViewControllers — split logic into ViewModels and Services
