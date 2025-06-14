
# ☁️ Automated Cloud Backup System

A lightweight, real-time file backup application that automatically uploads new or modified files from a selected folder to **Cloudinary**. This tool is designed for users who want a simple GUI-based solution to keep important files safe and accessible in the cloud — without manual effort.

---

## ✨ Features

* ✅ **Real-time file monitoring** using `watchdog`
* ✅ **Instant cloud uploads** to Cloudinary (on file create/modify)
* ✅ **Blink-free GUI** using multithreading for smooth interaction
* ✅ **Upload log display** and **Cloudinary URLs** of uploaded files
* ✅ **Skips duplicate uploads** (5-second cooldown for same file)
* ✅ Built with **Python** and **Tkinter** — no complex setup required

---

## 🖼️ GUI Preview

* 📁 Select a folder to watch
* ▶ Start or ■ Stop monitoring anytime
* 📋 View upload logs in real-time
* 🔗 Copy URLs of uploaded files easily

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install cloudinary watchdog
```

---

## 🚀 Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/vivekbargude/automated-backup-system.git
   cd cloud-backup-system
   ```

2. Run the application:

   ```bash
   python main.py
   ```

3. Select a folder and click **Start Backup**.

> All created or modified files in that folder will be uploaded to your Cloudinary account automatically.

---

## 🔧 Cloudinary Configuration

Edit the `cloudinary.config()` section in the script to use your own Cloudinary credentials:

```python
cloudinary.config(
    cloud_name='your-cloud-name',
    api_key='your-api-key',
    api_secret='your-api-secret'
)
```

> **Important:** Never expose these credentials in public repositories. Use environment variables or `.env` files in production.

---

## 💡 Use Cases

* Automated backup of scanned documents
* Archiving project or research folders
* Seamless cloud-sync for personal or shared files
* Uploading logs or reports to remote storage

---

## 🧠 Tech Stack

* `Python 3`
* `Tkinter` – GUI
* `watchdog` – File change detection
* `Cloudinary` – Cloud storage (raw file uploads)




