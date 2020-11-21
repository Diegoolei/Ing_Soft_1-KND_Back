
all:
	rm -f test_data_base.sqlite
	pytest --disable-warnings

print:
	rm -f test_data_base.sqlite
	pytest --disable-warnings --capture=no