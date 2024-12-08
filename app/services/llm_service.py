"""
LLM Service Module for handling X.AI model interactions.
This module provides a singleton service class that manages the initialization
and interaction with the X.AI API, ensuring thread-safe operations
for concurrent requests.
"""

import threading
import os
from openai import OpenAI
from flask import current_app


class LLMService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_client()
        return cls._instance

    def _initialize_client(self):
        self.client = OpenAI(
            api_key=os.getenv("XAI_API_KEY"),
            base_url="https://api.x.ai/v1",
        )
        current_app.logger.info("X.AI client initialized")

    def generate_response(self, prompt):
        try:
            messages = [
                {"role": "system", "content": "You are a helpful AI assistant. Respond in a clear and friendly manner."},
                {"role": "user", "content": prompt}
            ]

            completion = self.client.chat.completions.create(
                model="grok-beta",
                messages=messages
            )

            response = completion.choices[0].message.content
            current_app.logger.info(f"Response generated: {response[:100]}...")
            return response

        except Exception as e:
            current_app.logger.error(f"Error generating response: {str(e)}")
            raise
