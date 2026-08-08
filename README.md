# 🔐 Image Steganography

A desktop-based **Image Steganography application** built with **Python, Tkinter, and Pillow (PIL)** that allows users to hide secret text messages inside images and later extract the hidden message.

The application provides a simple graphical interface with separate **Encode** and **Decode** workflows, making basic image-based data hiding easy to use.

---

## 📌 Project Overview

**Image Steganography** is the technique of hiding secret information inside another file, such as an image, without visibly changing the appearance of the original file.

This project implements **Least Significant Bit (LSB) steganography** to encode text into the pixel data of an image.

The application allows users to:

* 🖼️ Select an image
* 🔐 Hide a text message inside the image
* 💾 Save the resulting stego-image as a PNG file
* 🔎 Select an image containing hidden data
* 🔓 Extract and display the hidden message
* 🖥️ Perform all operations through a graphical user interface

---

## ✨ Features

### 🔐 Encode Message

* Select an image from your computer.
* Enter a secret text message.
* Encode the message into the image pixels.
* Save the resulting image as a new PNG file.

### 🔓 Decode Message

* Select an image containing hidden information.
* Extract the encoded message from its pixel data.
* Display the recovered message inside the application.

### 🖥️ Graphical User Interface

* Built using Python's **Tkinter** library.
* Full-screen application interface.
* Simple Encode/Decode workflow.
* File selection dialogs.
* Success and error notifications.

### 🛡️ LSB Steganography

The project uses the **Least Significant Bit (LSB)** technique to modify pixel values while keeping visual changes to the image extremely small.

---

## 🛠️ Technologies Used

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| 🐍 Python        | Core programming language       |
| 🖼️ Tkinter      | Graphical User Interface        |
| 🎨 Pillow (PIL)  | Image processing                |
| 📁 OS Module     | File and path handling          |
| 🔢 LSB Algorithm | Hiding text inside image pixels |

---

## 📂 Project Structure

```text
Image-Steganography/
│
├── steganography.py
├── README.md
├── requirements.txt
│
└── screenshots/
    ├── home.png
    ├── encode.png
    └── decode.png
```

> You can rename `steganography.py` to match the actual Python filename in your repository.

---

## ⚙️ How It Works

The project uses **Least Significant Bit (LSB) encoding**.

Each RGB image pixel contains three color channels:

```text
Red    → 8 bits
Green  → 8 bits
Blue   → 8 bits
```

For example:

```text
Original pixel:

R = 11001010
G = 10110101
B = 01101100
```

The application modifies the least significant bits of pixel values to represent the binary form of the secret message.

A character is converted into an 8-bit binary representation.

For example:

```text
A → 01000001
```

The application then uses pixel values to store these bits.

Because only the least significant bit is changed, the visual difference between the original and encoded image is generally very small.

---

## 🔄 Encoding Process

The encoding workflow is:

```text
Select Image
     ↓
Enter Secret Message
     ↓
Convert Message to Binary
     ↓
Read Image Pixel Data
     ↓
Modify Least Significant Bits
     ↓
Generate Stego Image
     ↓
Save as PNG
```

### Example

Suppose the message is:

```text
HELLO
```

The characters are converted into binary:

```text
H → 01001000
E → 01000101
L → 01001100
L → 01001100
O → 01001111
```

These binary values are embedded into the image's pixel data.

---

## 🔍 Decoding Process

The decoding workflow reverses the encoding process:

```text
Select Stego Image
       ↓
Read Pixel Data
       ↓
Extract Least Significant Bits
       ↓
Group Bits into 8-bit Characters
       ↓
Convert Binary to Text
       ↓
Display Hidden Message
```

The application detects the termination condition stored during encoding and reconstructs the original text message.

---

## 📋 Requirements

Make sure you have:

* Python **3.x**
* Tkinter
* Pillow

Tkinter is generally included with standard Python installations on Windows.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Image-Steganography.git
```

Navigate to the project directory:

```bash
cd Image-Steganography
```

---

### 2. Create a Virtual Environment

Recommended:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

Install Pillow:

```bash
pip install Pillow
```

Or install everything from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
Pillow
```

---

## ▶️ Running the Application

Run the Python file:

```bash
python steganography.py
```

The Image Steganography application will launch.

---

## 🖥️ How to Use

### Step 1 — Encode

Select:

```text
Encode
```

Then select the image in which you want to hide your message.

---

### Step 2 — Enter Message

Enter your secret message into the text area.

For example:

```text
This is my secret message.
```

Click:

```text
Encode
```

---

### Step 3 — Save Image

Choose a location and filename.

The application saves the encoded image as a:

```text
.PNG
```

file.

---

### Step 4 — Decode

Return to the main screen and select:

```text
Decode
```

Choose the previously generated stego-image.

---

### Step 5 — Read Hidden Message

The application extracts the hidden message and displays it in the text area.

---



## 🧠 Algorithm

The project consists of three main stages.

### 1. Convert Text to Binary

Each character is converted into an 8-bit binary value.

```python
format(ord(character), '08b')
```

For example:

```text
A
↓
ASCII value = 65
↓
Binary = 01000001
```

---

### 2. Modify Pixel Values

The RGB pixel values are examined and their least significant bits are adjusted according to the message bits.

Conceptually:

```text
Message bit = 0
→ Pixel value should be even

Message bit = 1
→ Pixel value should be odd
```

This allows binary information to be embedded into the image.

---

### 3. Extract Hidden Data

During decoding, the application checks whether each pixel value is even or odd.

```text
Even → 0
Odd  → 1
```

Eight extracted bits are combined to reconstruct one character.

The process continues until the encoded termination condition is reached.

---

## 📐 Capacity

The amount of data that can be hidden depends on the dimensions of the image.

Larger images generally provide greater capacity.

For example:

```text
Small Image
   ↓
Less storage capacity

Large Image
   ↓
More storage capacity
```

The application will show an error if the selected image is too small to hold the complete message.

---

## ⚠️ Limitations

This project is intended primarily as an educational implementation of image steganography.

Current limitations include:

* Text-only data hiding.
* No password authentication.
* No encryption before embedding.
* Message capacity depends on image size.
* The implementation is not designed to resist advanced steganalysis.
* JPEG compression can damage hidden information.
* PNG is recommended for preserving encoded pixel data.
* Very large messages may require a larger image.

---

## 🔒 Security Considerations

**Steganography is not the same as encryption.**

Steganography attempts to hide the existence of information, whereas encryption protects the information itself.

For stronger security, a production-grade version should use:

```text
Secret Message
      ↓
Encryption
      ↓
Encrypted Data
      ↓
Steganography
      ↓
Stego Image
```

This would provide two layers of protection:

1. **Encryption** — protects the content.
2. **Steganography** — hides the presence of the content.

---

## 🔮 Future Enhancements

Possible improvements include:

* 🔑 Password-protected encoding and decoding
* 🔐 AES encryption before embedding
* 📄 Support for text files
* 📁 Support for document/file hiding
* 🖼️ Improved image preview
* 📊 Message capacity indicator
* 📈 Image quality comparison
* 🎨 Modern GUI design
* 🧹 Improved error handling
* 📦 Standalone Windows `.exe` application
* 🧪 Automated unit testing
* 🛡️ Improved resistance against steganalysis
* 📱 Web-based version
* 🔐 SHA-256-based integrity verification

---

## 🎯 Learning Objectives

This project demonstrates practical understanding of:

* Python programming
* Object-oriented programming
* GUI development with Tkinter
* Image processing with Pillow
* Binary representation
* ASCII character encoding
* RGB pixel manipulation
* Least Significant Bit steganography
* File handling
* Exception handling
* Event-driven programming

---

## 🧪 Example

### Original Image

```text
Input Image
    +
Secret Message
```

### Encoding

```text
Input Image
     ↓
LSB Modification
     ↓
Stego Image
```

### Decoding

```text
Stego Image
     ↓
Extract LSBs
     ↓
Binary Data
     ↓
Characters
     ↓
Secret Message
```

---

## 📊 Project Information

| Category         | Details                              |
| ---------------- | ------------------------------------ |
| Project Type     | Desktop Application                  |
| Domain           | Cybersecurity / Information Security |
| Language         | Python                               |
| GUI              | Tkinter                              |
| Image Library    | Pillow                               |
| Technique        | LSB Steganography                    |
| Input            | PNG/JPEG/JPG                         |
| Output           | PNG                                  |
| Primary Function | Text hiding and extraction           |

---

## 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/improvement
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new steganography feature"
```

5. Push the branch.

```bash
git push origin feature/improvement
```

6. Open a Pull Request.

---

## 📜 License

This project is available for educational and personal use.



---

## 👨‍💻 Author

**Jayesh Margi**

📧 Email: **[jayeshmargi28@gmail.com](mailto:jayeshmargi28@gmail.com)**

---

## ⭐ Support

If you found this project useful or helpful for learning:

⭐ **Star this repository**

🍴 **Fork the repository**

🐛 **Report issues**

💡 **Suggest improvements**

---

### 🔐 Hide the message. Protect the information. Reveal it when needed.

> **Image Steganography — A simple implementation of hiding information inside digital images using LSB techniques.**
