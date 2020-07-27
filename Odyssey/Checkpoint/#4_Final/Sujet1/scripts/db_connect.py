# Get dataset from github.com
link = 'https://github.com/murpi/wilddata/raw/master/quests/chinook.db'
r = requests.get(link)
open('chinook.db', 'wb').write(r.content)

# Create connector
conn = sqlite3.connect('Odyssey/Checkpoint/#4_Final/Sujet1/datasets/chinook.db')
cursor = conn.cursor()