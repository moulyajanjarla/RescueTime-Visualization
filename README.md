📂 Project Structure

ActivityWatch-Visualization/
│-- fetch_activitywatch_data.py  # Fetch data from ActivityWatch API
│-- visualize_activitywatch.py   # Generate graphs and insights
│-- predict_usage.py             # Train LSTM model for predictions
│-- update_github.py             # Automate GitHub updates
│-- app.py                       # Streamlit dashboard
│-- activitywatch_data.csv       # Extracted activity data (ignored in Git)
│-- activitywatch_model.pth      # Trained model file (ignored in Git)
│-- README.md                    # Project documentation
│-- .gitignore                    # Ignore unnecessary files

🔹 Step 1: Install Dependencies

Ensure Python 3.8+ is installed, then install the required packages:

pip install requests pandas matplotlib seaborn plotly torch torchvision scikit-learn streamlit

🔹 Step 2: Fetch ActivityWatch Data

Run the following script to extract application usage data:

python fetch_activitywatch_data.py

This script:

Connects to ActivityWatch API (http://localhost:5600/api/0/buckets)

Extracts active window usage

Saves the data to activitywatch_data.csv

🔹 Step 3: Visualize Data

To generate graphs showing application usage trends, run:

python visualize_activitywatch.py

This script:

Reads activitywatch_data.csv

Displays the Top 10 Most Used Applications

🔹 Step 4: Predict Future Usage (Deep Learning)

Train an LSTM model to forecast future activity usage:

python predict_usage.py

This script:

Prepares training data from activitywatch_data.csv

Trains an LSTM model using PyTorch

Saves the trained model as activitywatch_model.pth

🔹 Step 5: Automate Updates to GitHub

Ensure your repository is linked:

git remote add origin https://github.com/your-username/ActivityWatch-Visualization.git

Run the script manually:

python update_github.py

To schedule automatic updates:

Linux/Mac: Add a Cron Job (crontab -e):

0 9 * * * python3 /path/to/update_github.py

Windows: Use Task Scheduler to run update_github.py daily.

🔹 Step 6: Run Interactive Dashboard

Launch the Streamlit dashboard:

streamlit run app.py

This will open a web-based dashboard displaying activity insights.

🔹 Step 7: Push the Code to GitHub

After making changes, update GitHub:

git add .
git commit -m "Updated ActivityWatch data and visualizations"
git push origin main

🎯 Future Improvements

Improve LSTM model accuracy

Add more visualization charts

Deploy Streamlit app online (e.g., Streamlit Cloud, Heroku)

💡 Credits

Developed by Sai Venkata Moulya Janjarla. Built using Python, ActivityWatch API, Pandas, PyTorch, and Streamlit.

📌 GitHub Repo: https://github.com/your-username/ActivityWatch-Visualization

