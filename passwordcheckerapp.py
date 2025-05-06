import hashlib
import requests
import tkinter as tk
from tkinter import messagebox

class PasswordCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Checker")
        master.geometry("400x200")

        self.label = tk.Label(master, text="Enter a password to check:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(master, show="*", width=30)
        self.password_entry.pack(pady=10)

        self.check_button = tk.Button(master, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=10)

    def request_api_data(self, query):
        url = 'https://api.pwnedpasswords.com/range/' + query
        res = requests.get(url)
        if res.status_code != 200:
            messagebox.showerror("Error", f"API request was not successful. Error code {res.status_code}")
            return None
        return res

    def get_passwords_leak_count(self, hashes, hash_to_check):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for h, count in hashes:
            if h == hash_to_check:
                return count
        return 0

    def pwned_api_check(self, password):
        hashed_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first_five, tail = hashed_sha1[:5], hashed_sha1[5:]
        response = self.request_api_data(first_five)
        if response is None:
            return None
        return self.get_passwords_leak_count(response, tail)

    def check_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password.")
            return

        count = self.pwned_api_check(password)
        if count is None:
            return  # Error occurred, already handled in request_api_data

        if count:
            messagebox.showwarning("Warning", f"Your password was found {count} times. You should change your password!")
        else:
            messagebox.showinfo("Success", "Your password was not found. Carry on!")

        self.password_entry.delete(0, tk.END)  # Clear the password entry

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()