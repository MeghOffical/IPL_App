# 🏏 IPL Web App – IPL Stats Explorer (2008–2022)

A beautifully designed **web interface** built on top of the [IPL Flask API](https://github.com/MeghOffical/ipl_flask_api). This app allows users to interactively explore IPL data including teams, matches, players, caps, and points tables — all in one place.

🔗 **Live Web App**: [https://ipl-app-va1w.onrender.com/](https://ipl-app-va1w.onrender.com/)

---

## 💡 What It Does

- Uses API routes from [IPL Flask API](https://github.com/MeghOffical/ipl_flask_api)
- Lets users explore:
  - All IPL teams
  - Compare any 2 teams head-to-head
  - View Orange & Purple Cap holders
  - Player-wise stats
  - Points Table by season
  - Final appearances by captains
  - Top batting partnerships

---

## 📁 Project Structure

```

IPL\_App/
├── static/                   # Static CSS files
│   └── style.css             # Custom styles
├── templates/                # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── teamvteam.html
│   ├── batsman.html
│   ├── bowler.html
│   ├── points.html
│   ├── caps.html
│   ├── finals.html
│   └── partnership.html
├── app.py                    # Main Flask app with routes
├── requirements.txt          # Python dependencies
├── Procfile                  # For Render deployment
└── README.md                 # This file

```

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/MeghOffical/IPL_App.git
   cd IPL_App```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally**

   ```bash
   python app.py
   ```

5. **Open in browser:**
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Hosted Version

The app is deployed for free using Render:

🔗 **Live Site**: [https://ipl-app-va1w.onrender.com/](https://ipl-app-va1w.onrender.com/)

---

## 🚀 Pages and Functionalities

| Page                   | URL Path        | Description                                   |
| ---------------------- | --------------- | --------------------------------------------- |
| Home                   | `/`             | Welcome page                                  |
| All Teams              | `/teams`        | Lists all IPL teams                           |
| Team vs Team           | `/teamvteam`    | Compare any 2 teams head-to-head              |
| Orange & Purple Caps   | `/caps`         | Season-wise top run scorers and wicket takers |
| Player Stats – Batsman | `/batsman`      | Get batsman stats by name                     |
| Player Stats – Bowler  | `/bowler`       | Get bowler stats by name                      |
| Points Table           | `/points`       | Points table for a specific season            |
| Most Final Played      | `/finals`       | Captains with most finals played              |
| Partnerships           | `/partnerships` | Top all-time batting pairs                    |

---

## 🔗 Connected API

This web app fetches data using your custom backend from the IPL Flask API:
📦 [GitHub Repo: ipl\_flask\_api](https://github.com/MeghOffical/ipl_flask_api)
📡 [API URL (Render)](https://ipl-api-render-url.com) *(replace with actual deployed API if public)*

---

## ✅ Technologies Used

* Python
* Flask
* HTML + CSS 
* Jinja2 Templates
* IPL API (custom backend)

---

## 💡 Future Ideas

* Add graphs using Seaborn or Plotly
* Add player vs player comparisons
* Improve mobile responsiveness
* Add team filters and search bars
* Use caching for faster performance


---

## 📝 License

This project is open source feel free to contribute it.

---

## 🙋 About the Creator

👤 **Megh Bavarva**  

I'm deeply passionate about **data science** and **data-driven storytelling**.  
This project was built as a way to apply **real-world data analysis** using IPL cricket data, and to showcase how raw CSVs can be transformed into actionable insights through APIs and dashboards.  

My primary interests are:
- **Data wrangling and feature engineering**
- **Building analytics pipelines**
- **Working with Pandas, NumPy, and ML tools**
- **Solving real-world problems using data**

Feel free to fork, star, or collaborate on data-focused projects!

🔗 GitHub: [@MeghOffical](https://github.com/MeghOffical)
