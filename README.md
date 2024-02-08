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

## Deployment

Please refer to the steps below to deploy your discord bot (<a href="https://dev.to/rishabk7/host-your-discord-bot-on-ec2-instance-aws-5c07" rel="noreferrer ">Source</a>):

### AWS EC2 Instance Setup

1. Go to AWS and sign up for an account. Once logged in, please hover the Apps Logo labeled Services on the top left. Navigate to All Services and find EC2.
2. Select `Launch Instance`
3. Below is an example of what sections to change. If not stated - please leave as default

```bash
   Name: something-one-word
   Application and OS Images: Ubuntu (any free tier eligible)
   Key pair (login):
      Create new key pair ->
        Key pair name: [name]-key
        Type: RSA
        Format: .pem
   Download the key pair .pem file and save this file in the same directory as your application
   Networking settings: Default is okay
```

4. Select `Connect to instance` and click the `SSH client` subtab

### Connect to your EC2 instance

1. Make sure your .pem file is saved within the same directory as your application
   Project/

- orchid-bot
  - main.py
  - ...
- orchid-key.pem

2. Navigate to the directory where your .pem file is, ensure your key is not publicly viewable

   ```
   chmod 400 "your-key.pem"
   ```

3. Connect to your instance using its Public DNS:
   ```
   ssh -i "your-key.pem" ubuntu@ec2-3-91-230-159.compute-1.amazonaws.com
   ```

### Install node and Python

1. Please run the following commands to install Node and npm on your EC2 instance:
   ```
   sudo apt-get update
   sudo apt-get install nodejs
   sudo apt-get install npm
   ```
2. Install Python and pip on your EC2 instance:

   ```
   sudo apt install python3
   python3 --version
   sudo apt install python3-pip
   pip3 --version
   pip install -r requirements.txt
   ```

3. Set your env variables

   ```
   export MY_VARIABLE=VALUE
   ```

4. Check if you've set your env variables correctly

   ```
   env
   ```

5. Clone your repo onto your EC2 instance and change directories into repo
   ```
   git clone https://github.com/quyencodes/orchid-bot.git
   ```
6. Run your bot (make sure to cd into the project on your EC2 instance)

   ```
   python3 main.py
   ```

7. The bot will ONLY run while you have your terminal open. In order for it to be run after you've logged out of your EC2 instance, please

### Install PM2 and run PM2

1. Please run the following commands:

   ```
   sudo npm install -g pm2
   ```

2. Set your env variables and run the following command, please replace values accordingly

   ```
   pm2 start your_app.py --name "your_app_name" --env '{"DISCORD_TOKEN": ASDFGHJKL123456789}
   ```

3. Run the following commands to check on your instance and read pm2 terminal
   ```
   pm2 list
   pm2 logs
   ```
