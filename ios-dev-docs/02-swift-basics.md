# 02 - Swift Basics

## 📦 Variables & Constants

```swift
let appName: String = "MyApp"
var userScore: Int = 0
userScore += 10
let isLoggedIn = true
```

---

## 🔤 String Interpolation

```swift
let name = "Parris"
let greeting = "Hello, \(name)! Welcome to iOS development."
```

---

## 🔁 Control Flow

```swift
if userScore > 100 {
    print("High score!")
} else {
    print("Keep playing.")
}

for i in 1...5 {
    print("Step \(i)")
}
```

---

## 📦 Collections

```swift
var fruits: [String] = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")

var userInfo: [String: Any] = ["name": "Parris", "age": 28]
var uniqueIDs: Set<Int> = [1, 2, 3, 2, 1] // {1, 2, 3}
```

---

## 🔧 Functions

```swift
func greetUser(name: String) -> String {
    return "Hello, \(name)!"
}

func getScreenSize() -> (width: Int, height: Int) {
    return (390, 844)
}
```

---

## 🏛 Classes & Structs

```swift
// Struct (value type — preferred for SwiftUI models)
struct User {
    var name: String
    var age: Int
}

// Class (reference type — used for ViewControllers)
final class AuthManager {
    static let shared = AuthManager()
    private var token: String?

    func login(token: String) { self.token = token }
    func isAuthenticated() -> Bool { return token != nil }
}
```

---

## 🎯 Optionals

```swift
var email: String? = nil

guard let email = email else {
    print("No email provided")
    return
}

let displayEmail = email ?? "user@example.com"
```

---

## ⚡ Closures

```swift
let numbers = [5, 2, 8, 1, 9]
let sorted = numbers.sorted { $0 < $1 }
```

---

## 🔄 Async/Await

```swift
func fetchUserData(userID: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(userID)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

Task {
    do {
        let user = try await fetchUserData(userID: "123")
        print(user.name)
    } catch {
        print("Error: \(error)")
    }
}
```

---

## 📌 Protocols

```swift
protocol Describable {
    var description: String { get }
    func describe() -> String
}

struct Product: Describable {
    var name: String
    var price: Double
    var description: String { "\(name) - $\(price)" }
    func describe() -> String { "Product: \(description)" }
}
```
