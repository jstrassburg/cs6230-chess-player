if (Test-Path .\results.csv) {
    Remove-Item .\results.csv
}
python .\play_chess.py --search-depth 1 --max-children 1 --max-turns 999
python .\play_chess.py --search-depth 1 --max-children 5 --max-turns 999
python .\play_chess.py --search-depth 1 --max-children 10 --max-turns 999
python .\play_chess.py --search-depth 1 --max-children 15 --max-turns 999
python .\play_chess.py --search-depth 1 --max-children 20 --max-turns 999
python .\play_chess.py --search-depth 2 --max-children 1 --max-turns 999
python .\play_chess.py --search-depth 2 --max-children 5 --max-turns 999
python .\play_chess.py --search-depth 2 --max-children 10 --max-turns 999
python .\play_chess.py --search-depth 2 --max-children 15 --max-turns 999
python .\play_chess.py --search-depth 2 --max-children 20 --max-turns 999
python .\play_chess.py --search-depth 3 --max-children 1 --max-turns 999
python .\play_chess.py --search-depth 3 --max-children 5 --max-turns 999
python .\play_chess.py --search-depth 3 --max-children 10 --max-turns 999
python .\play_chess.py --search-depth 3 --max-children 15 --max-turns 999
python .\play_chess.py --search-depth 3 --max-children 20 --max-turns 999
python .\play_chess.py --search-depth 4 --max-children 1 --max-turns 999
python .\play_chess.py --search-depth 4 --max-children 5 --max-turns 999
python .\play_chess.py --search-depth 4 --max-children 10 --max-turns 999
python .\play_chess.py --search-depth 4 --max-children 15 --max-turns 999
python .\play_chess.py --search-depth 4 --max-children 20 --max-turns 999
python .\play_chess.py --search-depth 5 --max-children 1 --max-turns 999
python .\play_chess.py --search-depth 5 --max-children 5 --max-turns 999
python .\play_chess.py --search-depth 5 --max-children 10 --max-turns 999
python .\play_chess.py --search-depth 5 --max-children 15 --max-turns 999
python .\play_chess.py --search-depth 5 --max-children 20 --max-turns 999