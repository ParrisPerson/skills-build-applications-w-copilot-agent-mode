# 04 - SwiftUI Guide

## 🌟 Your First SwiftUI View

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "swift")
                .font(.system(size: 60))
                .foregroundColor(.orange)
            Text("Hello, iOS Developer!")
                .font(.largeTitle)
                .fontWeight(.bold)
        }
        .padding()
    }
}

#Preview { ContentView() }
```

---

## 🔁 State & Binding

```swift
struct CounterView: View {
    @State private var count: Int = 0

    var body: some View {
        VStack(spacing: 20) {
            Text("Count: \(count)").font(.largeTitle)
            HStack(spacing: 20) {
                Button { count -= 1 } label: {
                    Image(systemName: "minus.circle.fill").font(.system(size: 40)).foregroundColor(.red)
                }
                Button { count += 1 } label: {
                    Image(systemName: "plus.circle.fill").font(.system(size: 40)).foregroundColor(.green)
                }
            }
        }
    }
}
```

---

## 📋 List View

```swift
struct Task: Identifiable {
    let id = UUID()
    var title: String
    var isCompleted: Bool
}

struct TaskListView: View {
    @State private var tasks: [Task] = [
        Task(title: "Buy groceries", isCompleted: false),
        Task(title: "Write code", isCompleted: true)
    ]

    var body: some View {
        NavigationStack {
            List($tasks) { $task in
                HStack {
                    Image(systemName: task.isCompleted ? "checkmark.circle.fill" : "circle")
                        .foregroundColor(task.isCompleted ? .green : .gray)
                        .onTapGesture { task.isCompleted.toggle() }
                    Text(task.title)
                        .strikethrough(task.isCompleted, color: .gray)
                }
            }
            .navigationTitle("My Tasks")
        }
    }
}
```

---

## 🧩 ObservableObject (MVVM)

```swift
class UserViewModel: ObservableObject {
    @Published var username: String = ""
    @Published var isLoading: Bool = false

    @MainActor
    func fetchUser(id: String) async {
        isLoading = true
        try? await Task.sleep(nanoseconds: 1_000_000_000)
        username = "Parris"
        isLoading = false
    }
}

struct UserProfileView: View {
    @StateObject private var viewModel = UserViewModel()

    var body: some View {
        VStack(spacing: 20) {
            if viewModel.isLoading {
                ProgressView("Loading...")
            } else {
                Text(viewModel.username.isEmpty ? "No user loaded" : "Hello, \(viewModel.username)!")
                    .font(.title)
            }
            Button("Load User") {
                Task { await viewModel.fetchUser(id: "123") }
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}
```

---

## 🧭 NavigationStack

```swift
struct AppRootView: View {
    var body: some View {
        NavigationStack {
            List(["Settings", "Profile", "Dashboard"], id: \.self) { item in
                NavigationLink(item, destination: DetailView(title: item))
            }
            .navigationTitle("Home")
        }
    }
}

struct DetailView: View {
    let title: String
    var body: some View {
        Text("Welcome to \(title)").font(.largeTitle).navigationTitle(title)
    }
}
```

---

## 🔄 Async Data Loading with `.task`

```swift
struct PostsView: View {
    @State private var posts: [String] = []
    @State private var isLoading = true

    var body: some View {
        Group {
            if isLoading { ProgressView("Loading...") }
            else { List(posts, id: \.self) { Text($0) }.navigationTitle("Posts") }
        }
        .task { await loadPosts() }
    }

    private func loadPosts() async {
        try? await Task.sleep(nanoseconds: 1_000_000_000)
        posts = ["Post 1", "Post 2", "Post 3"]
        isLoading = false
    }
}
```
