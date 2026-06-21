# 🔐 Password Strength Checker

A sleek, dark-themed desktop application built with Python and Tkinter that evaluates the strength of your passwords in real time — with detailed feedback and a common password database check.

![Password Strength Checker Screenshot](screenshot.png)

---

## ✨ Features

- **Real-time strength analysis** — scores your password on a scale of 0 to 7
- **Visual strength bar** — color-coded indicator (Weak 🔴 / Moderate 🟡 / Strong 🟢 / Very Strong 💪)
- **Detailed feedback** — tells you exactly what's missing or what to improve
- **Common password detection** — checks against known leaked password lists
- **Show/Hide password toggle** — eye icon for visibility control
- **Dark UI** — modern, minimalist interface with a deep purple accent theme
- **CLI mode** — can also be run directly in the terminal without the GUI

---

## 🖥️ Screenshots

> The app running with a sample password showing a **Very Strong** result (7/7 score):

![App Preview](screenshot.png)

---

## 📁 Project Structure

```
password-strength-checker/
│
├── app.py                      # GUI application (Tkinter)
├── password_strength_checker.py # Core logic + CLI runner
├── password_list/               # Folder containing common password .txt files
│   └── *.txt                   # One or more text files with common passwords
└── README.md
```

---

## ⚙️ How It Works

The checker evaluates passwords against **7 criteria**, each worth 1 point:

| # | Rule | Points |
|---|------|--------|
| 1 | At least 8 characters | +1 |
| 2 | At least 12 characters | +1 (bonus) |
| 3 | At least 16 characters | +1 (bonus) |
| 4 | Contains uppercase letters (A–Z) | +1 |
| 5 | Contains lowercase letters (a–z) | +1 |
| 6 | Contains digits (0–9) | +1 |
| 7 | Contains special characters (!@#$...) | +1 |
| ⚠ | 3+ repeated characters in a row | −1 penalty |
| ⚠ | Found in common password list | −1 penalty |

### Strength Labels

| Score | Label |
|-------|-------|
| 0 – 2 | Weak 🔴 |
| 3 – 4 | Moderate 🟡 |
| 5 – 6 | Strong 🟢 |
| 7 | Very Strong 💪 |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Tkinter (included with standard Python installations)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mdrakibulislam10009/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Add a password list** *(optional but recommended)*:

   Place one or more `.txt` files inside a folder named `password_list/`. Each line should contain one common password. You can download public wordlists like [SecLists](https://github.com/danielmiessler/SecLists) or [rockyou.txt](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz).

   ```
   password_list/
   └── common_passwords.txt
   ```

3. **Run the GUI app:**

   ```bash
   python app.py
   ```

4. **Or run in CLI mode:**

   ```bash
   python password_strength_checker.py
   ```

---

## 🧪 CLI Usage Example

```
Enter Your Password: MyP@ssw0rd!

==================================================
  Password : ***********
  Length   : 11 characters
  Score    : [█████░░] 5/7
  Strength : Strong 🟢
--------------------------------------------------
  Feedback:
    ✅  Length is good (11 characters)
    ✅  Contains uppercase letters
    ✅  Contains lowercase letters
    ✅  Contains numbers
    ✅  Contains special characters
==================================================
```

---

## 🎨 UI Color Theme

| Element | Color |
|---------|-------|
| Background | `#0f0f1a` |
| Card | `#1a1a2e` |
| Accent | `#7c6af7` (Purple) |
| Strong | `#4ade80` (Green) |
| Moderate | `#fbbf24` (Yellow) |
| Weak | `#f87171` (Red) |
| Very Strong | `#a78bfa` (Light Purple) |

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `tkinter` | GUI framework (built-in with Python) |
| `re` | Regex-based password rule checking (built-in) |
| `os` | File and directory handling (built-in) |

No external packages required — this project runs entirely on the Python standard library.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Md Rakibul Islam**
- GitHub: [@mdrakibulislam10009](https://github.com/mdrakibulislam10009)

---

> ⭐ If you found this project helpful, consider giving it a star on GitHub!
