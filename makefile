config:
	pip3 install pyinstaller
build:
	pyinstaller --onefile Spike-Search.py
	mv dist/Spike-Search .
run:
	./Spike-Search
clean:
	rm -rf dist/
	rm -rf build/
	rm Spike-Search
	rm Spike-Search