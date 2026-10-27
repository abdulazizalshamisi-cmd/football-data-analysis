# FIFA Players Data Analysis

Exploratory analysis of about 19,667 FIFA players using Python, pandas and matplotlib.

## Dataset

- Source: Kaggle (Fifa.csv)
- 19,667 players
- Columns: Name, Country, Position, Age, Overall_Rating, Future Potential, Team, Value Per M$, Total_Stats Score

## Key Findings

- Most players are young: the median age is 22, and the largest age group (about 6,000 players) is around 18 to 21.
- Ratings rise from the late teens through the 20s and start to decline after about age 30.
- Younger players have a higher Future Potential than older players, because a young player still has room to grow while an older player is usually near his peak.

## How to Run

    python -m venv .venv
    .venv\Scripts\python.exe -m pip install -r requirements.txt
    .venv\Scripts\python.exe analysis.py

## Notes

- pandas is pinned below version 3 because Windows Smart App Control blocked the newer version on my laptop.
- The Team column mixes clubs and national teams (for example, Netherlands has only 1 player), so a club ranking is not reliable yet. Planned for v1.1.