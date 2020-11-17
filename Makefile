
all: test_game.py
	rm -f data_base.sqlite
	pytest --disable-warnings

print: test_game.py
	rm -f data_base.sqlite
	pytest --disable-warnings --capture=no