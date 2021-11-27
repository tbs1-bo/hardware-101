venv: requirements.txt
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

.venv: pyproject.toml
	poetry install

HOST=huckleberrypi.local
DIR=/home/pi/proj

deploy_rgbled: rgb_led/*
	scp -r rgb_led $(HOST):$(DIR)
	ssh $(HOST) python3 $(DIR)/rgb_led/rgb_led.py

publish: pyproject.toml
	poetry publish --build
	