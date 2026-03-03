# 01 - Getting Started

## 🧰 Prerequisites

- **macOS 13 (Ventura)** or later
- **Xcode 15+** — [Download from the App Store](https://apps.apple.com/us/app/xcode/id497799835)
- **Visual Studio Code** — [Download here](https://code.visualstudio.com/)
- **GitHub Copilot** — Active subscription at [github.com/copilot](https://github.com/copilot)

---

## 🔧 VS Code Extensions for iOS Development

```bash
code --install-extension sswg.swift-lang
code --install-extension github.copilot
code --install-extension github.copilot-chat
code --install-extension christian-kohler.path-intellisense
```

| Extension | Purpose |
|-----------|---------|
| `Swift` (SSWG) | Swift language support, syntax highlighting, IntelliSense |
| `GitHub Copilot` | AI-powered code completions |
| `GitHub Copilot Chat` | Chat-based agent assistance |
| `Path IntelliSense` | Autocomplete for file paths |

---

## 🗂 Opening an Xcode Project in VS Code

```bash
cd ~/Projects/MyiOSApp
code .
```

> ⚠️ **Important:** VS Code is used for **code editing and Copilot interactions**. To **build and run** the app, you still need **Xcode**.

---

## 🏗 Creating a New Xcode Project

1. Open **Xcode** → **File > New > Project**
2. Select **iOS > App**
3. Set **Interface** to SwiftUI or Storyboard, **Language** to Swift
4. Save to `~/Projects` folder
5. Open in VS Code: `code ~/Projects/MyApp`

---

## 🤖 Enabling GitHub Copilot Chat

1. Press `Cmd + Shift + P` → "GitHub Copilot: Sign In"
2. Open Copilot Chat with `Cmd + Shift + I`
3. Try:
   - `@workspace What is the structure of this iOS project?`
   - `Generate a UIViewController with a UITableView`
   - `Create a SwiftUI view with a list and navigation`

---

## ✅ Verify Your Setup

```bash
swift --version
xcodebuild -version
```
