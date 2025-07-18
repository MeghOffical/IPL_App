from flask import Flask, render_template, request
import requests
import logging

app = Flask(__name__)

# messages for debugging in production
logging.basicConfig(level=logging.INFO)

# Base URL of your deployed IPL data API
API_BASE = 'https://ipl-flask-final-api.onrender.com/'

# error message
GENERAL_ERROR_MSG = "Something went wrong while fetching the data. Please try again later."


@app.route('/')
def index():
    # Show the home page
    return render_template('index.html')


@app.route('/api/teams', methods=['POST'])
def teams():
    # Fetch list of all IPL teams
    try:
        resp = requests.get(f'{API_BASE}/api/teams')
        resp.raise_for_status()
        teams_list = resp.json().get('teams', [])
        return render_template('teams.html', teams=teams_list)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching teams: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/teamVteam', methods=['POST'])
def teamVteam():
    # Fetch same team list for matchup selection
    try:
        resp = requests.get(f'{API_BASE}/api/teams')
        resp.raise_for_status()
        teams_list = resp.json().get('teams', [])
        return render_template('teamVteam.html', teams=teams_list)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching team list: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/teamVteam_response')
def teamVteam_response():
    # Show comparison of two selected teams
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    if not team1 or not team2:
        # Both must be provided
        return render_template('error.html', message=GENERAL_ERROR_MSG)

    try:
        resp = requests.get(f'{API_BASE}/api/teamVteam?team1={team1}&team2={team2}')
        resp.raise_for_status()
        data = resp.json()
        return render_template('teamVteam_response.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching comparison data: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/team_winning_record', methods=['POST'])
def team_winning():
    # Fetch each team's win/loss record
    try:
        resp = requests.get(f'{API_BASE}/api/team_winning_record')
        resp.raise_for_status()
        data = resp.json()
        return render_template('team_winning.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching win records: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/point_table', methods=['POST'])
def point_table():
    # Show form for selecting a season
    return render_template('point_table.html')


@app.route('/api/points_table_view', methods=['POST'])
def points_table_view():
    # Display sorted points table for selected season
    season = request.form.get('season_ka_data')
    if not season:
        return render_template('error.html', message=GENERAL_ERROR_MSG)

    try:
        resp = requests.get(f'{API_BASE}/api/point_table?season={season}')
        resp.raise_for_status()
        points_data = resp.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching points table: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)

    # Define how positions should sort (Winner, Runner Up, etc.)
    def season_sort_key(team):
        order = {"Winner":1, "Runner Up":2, "3rd Place":3, "4th Place":4}
        pos = team.get('SeasonPosition')
        if isinstance(pos, str) and pos.strip() in order:
            return order[pos.strip()]
        try:
            return int(pos)
        except Exception:
            return float('inf')

    has_pos = any(team.get('SeasonPosition') for team in points_data)
    try:
        sorted_points = sorted(points_data, key=season_sort_key) if has_pos else points_data
    except Exception as e:
        logging.error(f"Sorting error: {e}")
        sorted_points = points_data
        has_pos = False

    return render_template(
        'points_result_combined.html',
        season=season,
        points=sorted_points,
        has_position=has_pos
    )


@app.route('/api/purple_cap', methods=['POST'])
def purple_cap():
    # Fetch list of top wicket takers per season
    try:
        resp = requests.get(f'{API_BASE}/api/purple_cap')
        resp.raise_for_status()
        data = resp.json()
        return render_template('purple_cap.html', purple_data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching purple cap: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/orange_cap', methods=['POST'])
def orange_cap():
    # Fetch list of top run scorers per season
    try:
        resp = requests.get(f'{API_BASE}/api/orange_cap')
        resp.raise_for_status()
        data = resp.json()
        return render_template('orange_cap.html', orange_data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching orange cap: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/batting_pair', methods=['POST'])
def batting_pair():
    # Fetch best batting pairs
    try:
        resp = requests.get(f'{API_BASE}/api/batting_pair')
        resp.raise_for_status()
        data = resp.json()
        return render_template('batting_pair.html', pairs=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching batting pairs: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/Player_Of_Match', methods=['POST'])
def pom():
    # Fetch count of Player of the Match awards
    try:
        resp = requests.get(f'{API_BASE}/api/Player_Of_Match')
        resp.raise_for_status()
        data = resp.json()
        return render_template('pom.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Player of the Match: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/bowler_details', methods=['POST'])
def bowler():
    # Fetch list of all bowlers
    try:
        resp = requests.get(f'{API_BASE}/api/name_of_bowlers')
        resp.raise_for_status()
        data = resp.json()
        return render_template('bowler.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching bowlers: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/specific_bowler', methods=['POST'])
def specific_bowler():
    # Fetch stats for a selected bowler
    name = request.form.get('bowler_name')
    if not name:
        return render_template('error.html', message=GENERAL_ERROR_MSG)
    try:
        resp = requests.get(f'{API_BASE}/api/bowler_details?bowler={name}')
        resp.raise_for_status()
        data = resp.json()
        return render_template('bowler_detail.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching bowler '{name}': {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/batsman_details', methods=['POST'])
def batsman_details():
    # Fetch list of all batsmen
    try:
        resp = requests.get(f'{API_BASE}/api/name_of_batsmens')
        resp.raise_for_status()
        data = resp.json()
        return render_template('batsman.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching batsmen: {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)


@app.route('/api/specific_batsman', methods=['POST'])
def specific_batsman():
    # Fetch stats for a selected batsman
    name = request.form.get('batsman_name')
    if not name:
        return render_template('error.html', message=GENERAL_ERROR_MSG)
    try:
        resp = requests.get(f'{API_BASE}/api/batsman_details?batsman={name}')
        resp.raise_for_status()
        data = resp.json()
        return render_template('batsman_detail.html', data=data)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching batsman '{name}': {e}")
        return render_template('error.html', message=GENERAL_ERROR_MSG)




# if __name__ == '__main__':
#     # Local development server 
#     app.run(debug=True, port=8888)
