import streamlit as st

# Function to load the results (assuming the file is being updated regularly)
def load_results():
    try:
        with open("basketball_results.txt", "r", encoding="ISO-8859-1") as file:
            data = file.readlines()

        # Process the text file into a structured list of games
        games = []
        game = {}
        
        for line in data:
            line = line.strip()
            # Look for keywords to process each line
            if line.startswith("Game"):
                if game:  # Save previous game
                    games.append(game)
                    game = {}
                game["Game"] = line
            elif "Away Team" in line:
                game["Away Team"] = line.split(":")[1].strip() if ":" in line else "N/A"
            elif "Home Team" in line:
                game["Home Team"] = line.split(":")[1].strip() if ":" in line else "N/A"
            elif "Spread Away" in line:
                game["Spread Away"] = line.split(":")[1].strip() if ":" in line else "N/A"
            elif "Spread Home" in line:
                game["Spread Home"] = line.split(":")[1].strip() if ":" in line else "N/A"
            elif "Over/Under" in line:
                game["Over/Under"] = line.split(":")[1].strip() if ":" in line else "N/A"
            elif "Predicted Total" in line:
                game["Predicted Total"] = line.split(":")[1].strip() if ":" in line else "N/A"
            elif "Torvik Prediction" in line:
                game["Torvik Prediction"] = line.split(":")[1].strip() if ":" in line else "N/A"

        # Add the last game to the list (in case the last game doesn't end with a "Game X" line)
        if game:
            games.append(game)

        return games

    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

def show_dashboard():
    st.title("Basketball Betting Dashboard")

    # Load the latest results from the file
    games = load_results()

    if games is not None:
        st.subheader("Basketball Game Results")
     
