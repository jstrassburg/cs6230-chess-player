# cs6230-chess-player
A simple AI player implementaion for the game of chess. Developed for a project for MSOE course CS6230 - AI Tools.

# Running the program

```
virtualenv .env
.env\Scripts\activate
pip install -r requirements.txt
python play_chess.py  --help
usage: play_chess.py [-h] [--search-depth SEARCH_DEPTH] [--max-children MAX_CHILDREN] [--max-turns MAX_TURNS]

Play some chess

options:
  -h, --help            show this help message and exit
  --search-depth SEARCH_DEPTH
                        How many levels deep to search for a good move. Default: 3
  --max-children MAX_CHILDREN
                        How many random legal moves will be evaluated. Default: 5
  --max-turns MAX_TURNS
                        Play until this many turns have been played. Default: 20
```

