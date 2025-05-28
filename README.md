# Slack Domain Info App

This app provides a Slack slash command `/domainInfo <domain_name>` that returns all CNAME records for the given domain. It is built with Flask, deployable on Heroku, and uses dnspython for DNS lookups.

## Features
- Slack slash command integration
- Returns CNAME records for any domain
- Deployable on Heroku

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file (optional):**
   - You can add environment variables here if needed.

4. **Run locally:**
   ```bash
   python app.py
   ```
   The app will run on `http://localhost:5000/` by default.

## Deploy to Heroku

1. **Login to Heroku and create an app:**
   ```bash
   heroku login
   heroku create <your-app-name>
   ```

2. **Push code to Heroku:**
   ```bash
   git push heroku main
   # or
   git push heroku master
   ```

3. **Set environment variables on Heroku (if needed):**
   ```bash
   heroku config:set VAR_NAME=value
   ```

4. **Open your app:**
   ```bash
   heroku open
   ```

## Slack Integration

1. **Create a Slack App:**
   - Go to [Slack API: Your Apps](https://api.slack.com/apps) and create a new app.
   - Add a Slash Command:
     - Command: `/domainInfo`
     - Request URL: `https://<your-heroku-app>.herokuapp.com/domainInfo`
     - Short description: "Get CNAME records for a domain"
     - Usage hint: `<domain_name>`

2. **Install the app to your workspace.**

3. **Use the command in any channel:**
   ```
   /domainInfo example.com
   ```

## License
MIT
