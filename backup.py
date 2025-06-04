import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import cloudinary
import cloudinary.uploader

# ---------------------- Cloudinary Configuration ----------------------
cloudinary.config(
    cloud_name='drfabpozh',
    api_key='159681838633182',
    api_secret='ny8O_FAjXnS8cuUKUJIl_H7DEgs'
)

# ---------------------- Backup Handler ----------------------
class BackupHandler(FileSystemEventHandler):
    def __init__(self, log_area, url_area):
        self.log_area = log_area
        self.url_area = url_area
        self.uploaded_files = {}  # Dictionary to track recent uploads

    def upload_file(self, path):
        current_time = time.time()
        last_uploaded = self.uploaded_files.get(path, 0)
        # Skip upload if same file was uploaded in the last 5 seconds
        if current_time - last_uploaded < 5:
            return

        try:
            self.log_area.insert(tk.END, f"Uploading: {path}\n")
            self.log_area.see(tk.END)
            response = cloudinary.uploader.upload(path, resource_type='raw')
            url = response['secure_url']
            self.url_area.insert(tk.END, f"{url}\n")
            self.url_area.see(tk.END)
            self.log_area.insert(tk.END, "Uploaded successfully.\n\n")
            self.log_area.see(tk.END)
            self.uploaded_files[path] = current_time
        except Exception as e:
            self.log_area.insert(tk.END, f"Failed to upload: {e}\n")
            self.log_area.see(tk.END)

    def on_created(self, event):
        if not event.is_directory:
            self.upload_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.upload_file(event.src_path)

# ---------------------- GUI Application ----------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("☁️ Automated Cloud Backup System")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.folder = ""
        self.observer = None

        self.setup_ui()

    def setup_ui(self):
        font_label = ("Segoe UI", 11, "bold")
        font_button = ("Segoe UI", 10)

        # Folder Selection
        self.label = tk.Label(self.root, text="📁 Folder to Watch:", font=font_label)
        self.label.pack(pady=(15, 0))

        path_frame = tk.Frame(self.root)
        path_frame.pack(pady=5)
        self.path_display = tk.Entry(path_frame, width=45, font=("Segoe UI", 10))
        self.path_display.pack(side=tk.LEFT, padx=5)
        self.browse_btn = tk.Button(path_frame, text="Browse", command=self.browse_folder, font=font_button)
        self.browse_btn.pack(side=tk.LEFT)

        # Start and Stop Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        self.start_btn = tk.Button(btn_frame, text="▶ Start Backup", command=self.start_backup,
                                   bg="#4CAF50", fg="white", font=font_button, width=15)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="■ Stop Backup", command=self.stop_backup,
                                  bg="#F44336", fg="white", font=font_button, width=15)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # Upload Logs
        self.log_label = tk.Label(self.root, text="📋 Upload Logs:", font=font_label)
        self.log_label.pack(pady=(20, 5))

        self.log_area = scrolledtext.ScrolledText(self.root, height=10, width=70, font=("Consolas", 9))
        self.log_area.pack()

        # Uploaded URLs
        self.url_label = tk.Label(self.root, text="🔗 Uploaded URLs:", font=font_label)
        self.url_label.pack(pady=(15, 5))

        self.url_area = scrolledtext.ScrolledText(self.root, height=10, width=70, font=("Consolas", 9))
        self.url_area.pack()

        # Footer
        tk.Label(self.root, text="Made with ❤️ using Python + Cloudinary", font=("Segoe UI", 9, "italic"), fg="gray").pack(pady=10)

    def browse_folder(self):
        self.folder = filedialog.askdirectory()
        self.path_display.delete(0, tk.END)
        self.path_display.insert(0, self.folder)

    def start_backup(self):
        if self.folder:
            handler = BackupHandler(self.log_area, self.url_area)
            self.observer = Observer()
            self.observer.schedule(handler, self.folder, recursive=True)
            self.observer.start()
            self.log_area.insert(tk.END, f"✅ Started watching: {self.folder}\n")
            self.log_area.see(tk.END)
        else:
            self.log_area.insert(tk.END, "⚠️ Please select a folder first.\n")
            self.log_area.see(tk.END)

    def stop_backup(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.log_area.insert(tk.END, "🛑 Stopped watching.\n")
            self.log_area.see(tk.END)

# ---------------------- Main Program ----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
