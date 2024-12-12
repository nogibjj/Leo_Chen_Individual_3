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

        API_KEY = os.getenv("XAI_API_KEY")
        BASE_URL = "https://api.x.ai/v1"

        self.client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL,
        )

        current_app.logger.info("X.AI client initialized")

    def generate_response(self, prompt, chart_context=None):
        try:
            current_app.logger.info(
                f"Generating response for prompt: {prompt}")

            # Create a system message
            system_message = "You are a helpful AI assistant. Respond in a clear and friendly manner."

            # If there is chart data, add it to the system message
            if chart_context:
                context_info = []

                # Process genre data
                if chart_context.get('genreData'):
                    genre_data = chart_context['genreData']
                    context_info.append(
                        f"There is a movie genre analysis chart showing data from {genre_data['startYear']} "
                        f"to {genre_data['endYear']}. The genres analyzed include: "
                        f"{', '.join(g['name'] for g in genre_data['genres'])}."
                    )

                # Process popularity data
                if chart_context.get('popularityData'):
                    pop_data = chart_context['popularityData']
                    top_movies = [f"{m['title']} (popularity: {m['popularity']:.1f})"
                                  for m in pop_data['topMovies'][:3]]
                    bottom_movies = [f"{m['title']} (popularity: {m['popularity']:.1f})"
                                     for m in pop_data['bottomMovies'][:3]]

                    context_info.append(
                        f"There is a movie popularity chart for year {pop_data['year']}. "
                        f"Top 3 most popular movies: {', '.join(top_movies)}. "
                        f"Bottom 3 least popular movies: {', '.join(bottom_movies)}."
                    )

                if context_info:
                    system_message += "\n\nCurrent context:\n" + \
                        "\n".join(context_info)
                    system_message += "\n\nPlease consider this context when answering questions."

            messages = [
                {"role": "system", "content": system_message},
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
