# DAA_exp2
# 🔍 String Matching Algorithm Visualizer

An interactive web application that demonstrates and compares three popular string matching algorithms:

- Naive String Matching
- Knuth-Morris-Pratt (KMP)
- Rabin-Karp Algorithm

The application provides a **step-by-step visualization**, allowing users to understand how each algorithm searches for a pattern within a text while comparing their execution process and performance.

---

## 📖 Project Overview

String matching is one of the fundamental problems in computer science and is widely used in search engines, text editors, plagiarism detection, bioinformatics, and data processing.

This project was developed to help students and beginners visualize how different string matching algorithms work internally through interactive animations and detailed explanations.

---

## ✨ Features

### 🔹 Interactive Visualization
- Step-by-step execution of each algorithm
- Side-by-side comparison
- Highlight current character comparisons
- Display current indices
- Real-time algorithm explanation

### 🔹 Supported Algorithms

#### 1. Naive String Matching
- Character-by-character comparison
- Simple implementation
- Easy to understand

#### 2. Knuth-Morris-Pratt (KMP)
- LPS (Longest Prefix Suffix) table visualization
- Efficient pattern matching
- Avoids unnecessary comparisons

#### 3. Rabin-Karp
- Rolling Hash calculation
- Hash comparison visualization
- Collision handling

---

## 🎯 Learning Objectives

This project helps users understand:

- How string matching algorithms work
- Difference between brute-force and optimized searching
- Pattern preprocessing
- Rolling hash technique
- LPS array construction
- Time complexity analysis
- Performance comparison

---

## 🛠 Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- Chart.js (Performance Graph)
- Responsive Web Design

---

## 🚀 How to Run

### Option 1

Download the project and open

```
index.html
```

using any web browser.

### Option 2

Clone the repository

```bash
git clone https://github.com/yourusername/string-matching-visualizer.git
```

Open the folder

```
index.html
```

using VS Code Live Server.

---

## 📂 Project Structure

```
String-Matching-Visualizer/
│
├── index.html
├── README.md
├── assets/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── icons/
├── screenshots/
└── LICENSE
```

---

## 📸 Screenshots

### Home Page

(Add Screenshot)

---

### Naive Algorithm Visualization

(Add Screenshot)

---

### KMP Visualization

(Add Screenshot)

---

### Rabin-Karp Visualization

(Add Screenshot)

---

### Performance Comparison

(Add Screenshot)

---

## ⚙️ Algorithms Implemented

### Naive String Matching

The Naive algorithm compares the pattern with every possible position in the text until a match is found.

**Time Complexity**

- Best Case: O(n)
- Average Case: O(nm)
- Worst Case: O(nm)

---

### Knuth-Morris-Pratt (KMP)

The KMP algorithm preprocesses the pattern using the Longest Prefix Suffix (LPS) array to skip unnecessary comparisons.

**Time Complexity**

- Best Case: O(n)
- Average Case: O(n + m)
- Worst Case: O(n + m)

---

### Rabin-Karp

Rabin-Karp uses rolling hash values to compare the pattern and text efficiently.

**Time Complexity**

- Best Case: O(n + m)
- Average Case: O(n + m)
- Worst Case: O(nm)

---

## 📊 Performance Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space |
|------------|-----------|--------------|-------------|-------|
| Naive | O(n) | O(nm) | O(nm) | O(1) |
| KMP | O(n) | O(n+m) | O(n+m) | O(m) |
| Rabin-Karp | O(n+m) | O(n+m) | O(nm) | O(1) |

---

## 🎮 Website Features

- Interactive UI
- Animated visualization
- Character highlighting
- Live comparison
- Performance analysis
- Step explanation panel
- Execution statistics
- Responsive design
- Dark mode support
- Modern dashboard layout

---

## 📚 Applications

- Text Editors
- Search Engines
- Spell Checking
- DNA Sequence Matching
- Plagiarism Detection
- Bioinformatics
- Malware Detection
- Data Mining

---

## 🔮 Future Enhancements

- Boyer-Moore Algorithm
- Aho-Corasick Algorithm
- Visualization speed control
- Random text generator
- Pattern generator
- Download execution report
- Code highlighting
- Mobile optimization

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Moulidharan B M**

Department of Computer Science and Engineering

Chennai Institute of Technology

---

## ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork the project

📢 Share it with others

---

## 📧 Contact

For any suggestions or improvements, feel free to create an issue or submit a pull request.

Happy Coding! 🚀
