.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available tasks:"
	@echo "    watch  Upload changed library files to board automagically"
	@echo "    sync   Upload library files to board"
	@echo "    reset  Soft reboot the board"
	@echo "    repl   Start a repl session"
	@echo "    deps   Install dependencies with upip"
	@echo ""

watch:
	find . -name "*.py" | entr -c sh -c 'make sync && make reset'

sync:
	ampy --port /dev/cu.usbserial-C54ABFCA45 put mpu6886.py

repl:
	screen /dev/cu.usbserial-C54ABFCA45 115200

reset:
	ampy --port /dev/cu.usbserial-C54ABFCA45 reset

dist:
	python3 setup.py sdist
	# twine upload dist/filename.tar.gz

.PHONY: help watch shell repl reset sync dist
