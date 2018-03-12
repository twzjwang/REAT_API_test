test:
	@./test.sh > log
	@python cal.py
	@rm log
