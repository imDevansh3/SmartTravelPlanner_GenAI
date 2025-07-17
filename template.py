import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Project file structure for the Smart Travel Planner Bot
list_of_files = [
    ".env",
    "requirements.txt",
    "app.py",
    "setup.py",
    "README.md",
    "research/trials.ipynb",
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "src/itinerary_chain.py",
    "src/packing_chain.py",
    "src/food_chain.py",
    "src/mock_flight_api.py",
    "assets/flight_mock_data.json",
    "config/config.yaml",
    "logs/__init__.py",
    "logs/logging_config.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")