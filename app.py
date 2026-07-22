import os
import sqlite3
import hashlib
import pickle
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ==========================================
# 1. HARDCODED SECRETS (Secret Scanning Test)
# ==========================================
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_PERSONAL_ACCESS_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz1234"
JWT_SECRET_KEY = "super_secret_master_key_12345"

app.config['SECRET_KEY'] = JWT_SECRET_KEY

# ==========================================
# 2. SAST VULNERABILITIES (Static Analysis Test)
# ==========================================

# A. SQL Injection Vulnerability (CWE-89)
@app.route('/user')
def get_user():
    username = request.args.get('username', '')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Flaw: String formatting directly in SQL query allows SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return str(user)

# B. Command Injection Vulnerability (CWE-78)
@app.route('/ping')
def ping_host():
    ip = request.args.get('ip', '127.0.0.1')
    # Flaw: Unsanitized user input passed directly to OS shell command execution
    cmd = f"ping -c 1 {ip}"
    os.system(cmd)
    return f"Pinged {ip}"

# C. Weak Cryptographic Hash Function (CWE-328)
def hash_password(password):
    # Flaw: MD5 is cryptographically broken and vulnerable to collision attacks
    return hashlib.md5(password.encode()).hexdigest()

# D. Insecure Deserialization Vulnerability (CWE-502)
@app.route('/load_data', methods=['POST'])
def load_data():
    raw_data = request.data
    # Flaw: pickle.loads executes arbitrary Python code during deserialization
    untrusted_object = pickle.loads(raw_data)
    return f"Loaded: {untrusted_object}"

# E. Reflected Cross-Site Scripting (XSS) (CWE-79)
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    # Flaw: Rendering user input directly without HTML escaping
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
