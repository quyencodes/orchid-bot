# orchid-bot

## Getting Started

1. Clone the repository

   ```
   $ git clone https://github.com/quyencodes/orchid-bot.git
   ```

2. Ensure that you have Python (at least 3.11) installed on your computer. Please downgrade if needed or build the virtual enviornment in Python 3.11 to protect against compatability issues.

   ```
   python --version
   ```

3. Pip should be automatically installed when you install Python, but ensure pip is installed by:

   ```
   pip --version
   ```

4. Install relevant packages:

   ```
   pip install requirements.txt
   ```

5. Create your secret.py (use secret.example.py as an example):

   ```
   API_TOKEN = "YOUR TOKEN HERE"
   ```

6. Run main.py:

   ```
   python3 main.py
   ```

7. Run main.py with nodemon:

   ```
   nodemon --exec python3 main.py
   ```
