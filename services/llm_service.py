# llm_service.py
import requests
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
from tenacity import retry, stop_after_attempt, wait_fixed, before_sleep_log
import logging
from dotenv import load_dotenv
load_dotenv()

# logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  


class LLMService:
    def __init__(self, **config):
        self.api_key = os.environ.get("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=self.api_key)
        self.model = config.pop("model", "gemini-2.0-flash")
        self.config = types.GenerateContentConfig(**config)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(2),
        before_sleep=before_sleep_log(logger, logging.WARNING)  
    )
    def generate(self, prompt: str) -> str:
        """Gọi LLM API và trả về text response, retry tối đa 3 lần nếu lỗi."""
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=self.config
            )
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"LLM API Request Error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error in LLM service: {e}")
            raise

         
