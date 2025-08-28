import json
from pathlib import Path

"""
Centralized configuration module for the application.

This module is responsible for:
1. Defining static, project-wide path constants in an OS-agnostic way.
2. Loading dynamic settings from the settings.json file.
3. Providing a single, clean interface for accessing all configuration parameters.
"""

# --- Path Configuration ---
PROJECT_ROOT = Path(__file__).parent.parent
APP_DIR = PROJECT_ROOT / "app" 
DATA_DIR = PROJECT_ROOT /"processes"/ "data"
CONFIG_DIR = PROJECT_ROOT / "config"
WEAPONS_FILE_PATH = DATA_DIR / "weapons.txt"

# --- Settings Loading ---
# Load settings from the JSON file for easy modification without changing source code.
SETTINGS_FILE_PATH = CONFIG_DIR / "settings.json"
try:
    with open(SETTINGS_FILE_PATH, 'r') as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {}
    print(f"WARNING: Configuration file not found at {SETTINGS_FILE_PATH}. Using defaults.")

# --- Expose settings as easily accessible module-level variables ---
DB_NAME = settings.get("DB_NAME", "default_db")
COLLECTION_NAME = settings.get("COLLECTION_NAME", "default_collection")
API_TITLE = settings.get("API_TITLE", "Default API")
API_DESCRIPTION = settings.get("API_DESCRIPTION", "A default API description.")
API_VERSION = settings.get("API_VERSION", "1.0.0")
OUTPUT_COLUMNS = settings.get("OUTPUT_COLUMNS", ["id", "Text", "rarest_word", "sentiment", "weapons_detected"])
TEXT_COLUMN = settings.get("TEXT_COLUMN", "Text")


TOPIC_OUTPUT_RETRIVAL_ANTISEMITIC = settings.get("TOPIC_OUTPUT_RETRIVAL_ANTISEMITIC", "topic")
TOPIC_OUTPUT_RETRIVAL_NOT_ANTISEMITIC = settings.get("TOPIC_OUTPUT_RETRIVAL_NOT_ANTISEMITIC", "topic")

TOPIC_OUTPUT_CLEANER_NOT_ANTISEMITIC =settings.get("TOPIC_OUTPUT_CLEANER_NOT_ANTISEMITIC", "topic")
TOPIC_OUTPUT_CLEANER_ANTISEMITIC = settings.get("TOPIC_OUTPUT_CLEANER_ANTISEMITIC", "topic")

TOPIC_OUTPUT_ENRICHER_ANTISEMITIC = settings.get("TOPIC_OUTPUT_ENRICHER_ANTISEMITIC", "topic")
TOPIC_OUTPUT_ENRICHER_NOT_ANTISEMITIC = settings.get("TOPIC_OUTPUT_ENRICHER_NOT_ANTISEMITIC", "topic")