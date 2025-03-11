# Valley Mutant Twilio Game - Easy Setup Guide

### Step 1: Install Dependencies
Run the following command in the project folder:
```
pip install -r requirements.txt
```

### Step 2: Run the Game Locally (Test)
Start the Flask server with:
```
python app.py
```
Visit `http://127.0.0.1:5000/` to see if it runs.

### Step 3: Deploy to Render
1. Go to https://dashboard.render.com/
2. Click **"New Web Service"**
3. Connect your **GitHub repository** (if not set up, see below).
4. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variables**:
     - `TWILIO_ACCOUNT_SID` (Your Twilio SID)
     - `TWILIO_AUTH_TOKEN` (Your Twilio Token)
     - `TWILIO_PHONE_NUMBER` (Your Twilio Number)
5. Click **Deploy**.
6. Copy the **Render URL** and set it in **Twilio Console > Phone Numbers > "A Call Comes In"**.

### Step 4: Push to GitHub (If Not Done)
If your project is not yet on GitHub:
```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/valley-mutant-game.git
git push -u origin main
```

### Step 5: Call Your Twilio Number & Play!
Enjoy the **Twilio-based Valley Mutant game!**
