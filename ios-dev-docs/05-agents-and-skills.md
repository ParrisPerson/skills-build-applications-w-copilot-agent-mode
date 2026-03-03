# 05 - GitHub Copilot Agents & Skills for iOS Development

## 🤖 Available Agents

| Agent | Syntax | Best For |
|-------|--------|----------|
| Workspace | `@workspace` | Ask questions about your full Xcode project |
| Terminal | `@terminal` | Get shell commands (build, test, clean) |
| VS Code | `@vscode` | Configure the editor for Swift development |

---

## 🗣 `@workspace` Example Prompts

```
@workspace What view controllers exist in this project?
@workspace Explain the architecture of this iOS app
@workspace Where is the networking layer implemented?
@workspace What third-party dependencies are used in Package.swift?
```

---

## ⚡ Slash Commands

| Command | Description |
|---------|-------------|
| `/explain` | Explain selected Swift code |
| `/fix` | Fix bugs or errors in selected code |
| `/tests` | Generate XCTest unit tests |
| `/doc` | Add Swift documentation comments |
| `/new` | Scaffold a new Swift file or component |

---

## 🏗 Scaffolding Prompts

### UIKit ViewController
```
Create a UIViewController subclass called ProductDetailViewController
that displays a product image, name, price, and an "Add to Cart" button.
Use programmatic UI with Auto Layout, no storyboard.
```

### SwiftUI View + ViewModel
```
Create a SwiftUI view called WeatherView with an ObservableObject ViewModel
that has published properties for temperature, city name, and weather condition.
Include loading state and error handling.
```

### Networking Layer
```
Create a Swift NetworkManager using async/await and URLSession
with a generic request function that decodes Codable models.
Include custom error types.
```

---

## 🔧 Quick Prompts Reference

| Goal | Prompt |
|------|--------|
| New MVVM module | `Create a Swift MVVM module for [Feature] with Model, ViewModel, and SwiftUI View` |
| Fix a crash | `/fix This code crashes when the array is empty` |
| Refactor to SwiftUI | `Convert this UIViewController to a SwiftUI View keeping the same logic` |
| Add accessibility | `Add accessibility labels and hints to this SwiftUI view for VoiceOver` |
| Localization | `Extract all hardcoded strings into Localizable.strings` |
| Dark mode | `Update this UIKit code to support light and dark mode using semantic colors` |
| Memory check | `/explain Identify any retain cycles or memory issues in this Swift code` |
