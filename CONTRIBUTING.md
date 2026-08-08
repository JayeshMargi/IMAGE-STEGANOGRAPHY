# Contributing to Image Steganography

Thank you for your interest in contributing to **Image Steganography**! 🎉

Contributions, suggestions, bug reports, and improvements are welcome. This guide explains how you can contribute to the project.

---

## 📌 How to Contribute

There are several ways you can contribute:

* 🐛 Report bugs
* 💡 Suggest new features
* 🔧 Improve existing functionality
* 🎨 Improve the graphical user interface
* 📚 Improve documentation
* 🧪 Add tests
* 🔐 Improve security and data protection
* ⚡ Improve application performance
* 🧹 Improve code quality

---

## 🚀 Getting Started

### 1. Fork the Repository

Fork the repository to your own GitHub account.

### 2. Clone Your Fork

Clone the repository to your local computer:

```bash
git clone https://github.com/YOUR-USERNAME/Image-Steganography.git
```

Navigate to the project directory:

```bash
cd Image-Steganography
```

### 3. Create a Virtual Environment

It is recommended to use a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Pillow manually:

```bash
pip install Pillow
```

---

## 🌿 Create a Branch

Create a separate branch for your contribution instead of working directly on `main`.

```bash
git checkout -b feature/your-feature-name
```

Examples:

```bash
git checkout -b feature/password-protection
```

```bash
git checkout -b fix/image-validation
```

```bash
git checkout -b docs/improve-readme
```

### Recommended Branch Naming

| Prefix      | Purpose                   |
| ----------- | ------------------------- |
| `feature/`  | New functionality         |
| `fix/`      | Bug fixes                 |
| `docs/`     | Documentation             |
| `refactor/` | Code improvements         |
| `test/`     | Adding or improving tests |
| `ui/`       | GUI improvements          |

---

## 💻 Make Your Changes

Make your changes while keeping the existing functionality intact.

Before submitting your contribution, make sure:

* The application starts successfully.
* Encoding works correctly.
* Decoding works correctly.
* Existing functionality is not unnecessarily broken.
* Error handling is appropriate.
* The code is readable and understandable.
* Unnecessary files are not added to the repository.

---

## 🧪 Test Your Changes

Run the application:

```bash
python steganography.py
```

Test both major workflows:

### Encoding

1. Select an image.
2. Enter a message.
3. Encode the message.
4. Save the resulting PNG image.

### Decoding

1. Select the encoded PNG image.
2. Decode the image.
3. Verify that the original message is recovered correctly.

Also test edge cases such as:

* Empty messages
* Very large messages
* Images that are too small
* Invalid image files
* Canceling file-selection dialogs

---

## 📝 Commit Guidelines

Write clear and meaningful commit messages.

### Good Examples

```bash
git commit -m "Add password protection"
```

```bash
git commit -m "Fix image capacity validation"
```

```bash
git commit -m "Improve encode screen UI"
```

```bash
git commit -m "Update installation instructions"
```

### Avoid

```bash
git commit -m "changes"
```

```bash
git commit -m "update"
```

```bash
git commit -m "final"
```

---

## 📤 Push Your Changes

Push your branch to your GitHub repository:

```bash
git push origin feature/your-feature-name
```

---

## 🔀 Create a Pull Request

After pushing your branch:

1. Open your GitHub repository.
2. Select **Compare & pull request**.
3. Provide a clear title.
4. Explain what you changed.
5. Explain why the change was needed.
6. Mention any relevant issues.
7. Submit the Pull Request.

### Pull Request Example

**Title:**

```text
Add password protection for encoded messages
```

**Description:**

```text
## Changes
- Added password-based protection
- Added validation for incorrect passwords
- Updated the encode/decode workflow

## Testing
- Tested encoding with valid messages
- Tested decoding with correct passwords
- Tested incorrect password handling
```

---

## 🐛 Reporting Bugs

If you discover a bug, please create a GitHub Issue.

Include:

* A clear description of the problem
* Steps to reproduce it
* Expected behavior
* Actual behavior
* Python version
* Operating system
* Relevant error messages
* Screenshots, if applicable

### Example

```text
### Bug
The application crashes when a very small image is selected.

### Steps to Reproduce
1. Open the application.
2. Select Encode.
3. Select a small image.
4. Enter a message.
5. Click Encode.

### Expected Behavior
The application should display a clear error message.

### Actual Behavior
The application terminates unexpectedly.
```

---

## 💡 Suggesting Features

Feature suggestions are welcome.

When proposing a feature, explain:

1. What the feature does.
2. Why it would be useful.
3. How it could improve the application.

Examples of potential improvements:

* Password-protected messages
* AES encryption
* Message capacity indicator
* Better image preview
* Drag-and-drop image selection
* File hiding support
* Modern GUI
* Automated testing
* Image integrity verification

---

## 🔐 Security Contributions

Security-related improvements are especially welcome.

Possible areas include:

* Encryption before embedding
* Password protection
* Data integrity verification
* Improved input validation
* Safer file handling
* Protection against malformed image input

Please do not submit sensitive information, private keys, passwords, or personal data in Issues or Pull Requests.

---

## 🎨 Code Style

Please try to maintain the existing coding style.

### General Guidelines

* Use meaningful variable and function names.
* Keep functions focused on a specific task.
* Avoid unnecessary duplicate code.
* Add comments when the logic is difficult to understand.
* Keep the GUI and steganography logic reasonably organized.
* Avoid committing unused code or debugging statements.

Example:

```python
def encode_message(image, message):
    # Encode the message into image pixels
    ...
```

is preferable to:

```python
def x(a, b):
    ...
```

---

## 📁 Files You Should Not Commit

Do not commit unnecessary generated or environment-specific files such as:

```text
__pycache__/
*.pyc
venv/
.env
.idea/
.vscode/
```

A `.gitignore` file should be used to prevent these files from being committed.

---

## 📋 Pull Request Checklist

Before submitting a Pull Request, make sure:

* [ ] My changes are related to the purpose of the Pull Request.
* [ ] I tested the application locally.
* [ ] Encoding still works.
* [ ] Decoding still works.
* [ ] I tested relevant edge cases.
* [ ] I did not commit unnecessary files.
* [ ] My code is readable.
* [ ] I updated the documentation if necessary.
* [ ] My commit messages are meaningful.
* [ ] I explained my changes in the Pull Request.

---

## 🤝 Code of Conduct

Please be respectful and constructive when interacting with other contributors.

We expect contributors to:

* Be respectful.
* Welcome constructive feedback.
* Avoid personal attacks.
* Respect different opinions.
* Focus discussions on improving the project.
* Keep Issues and Pull Requests professional.

---

## 📜 License

By contributing to this project, you agree that your contributions may be distributed under the project's license.

Please refer to the repository's `LICENSE` file for the applicable licensing terms.

---

## ⭐ Thank You!

Thank you for taking the time to contribute to **Image Steganography**.

Every contribution—whether it's a bug report, documentation improvement, UI enhancement, or new feature—helps make the project better.

**Happy coding! 🚀**
