# orchid-bot

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/quyencodes/orchid-bot.git
   ```

2. Ensure that you have Python (at least 3.11) installed on your computer. Please downgrade if needed or build the virtual enviornment in Python 3.11 to protect against compatability issues:

   ```
   python --version
   ```

3. Pip should be automatically installed when you install Python, but ensure pip is installed by:

   ```
   pip --version
   ```

4. Install relevant packages:

   ```
   pip install -r requirements.txt
   ```

5. Copy example.env and rename to .env:

   ```
   DISCORD_TOKEN = 'YOUR DISCORD TOKEN HERE'
   ```

6. Run main.py:

   ```
   python3 main.py
   ```

## Hot Reload

In order to run our application with hot reload, please ensure node and npm are installed on your machine. We strongly recommend installing npm as your Node.js manager.

1. Install npm:

   ```
   npm install -g npm
   ```

2. Install node:

   ```
   npm install node
   ```

3. Install necessary packages:

   ```
   npm install
   ```

4. Run application using hot reload:

   ```
   npm run start
   ```
