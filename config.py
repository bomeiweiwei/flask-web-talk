import os

from dotenv import load_dotenv


load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Flask Azure Demo")
DEBUG = os.getenv("DEBUG", "True") == "True"
PROVIDER = os.getenv("PROVIDER", "lmstudio")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:1234/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "lm-studio")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen2.5-vl-7b-instruct")
