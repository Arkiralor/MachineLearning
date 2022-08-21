from .config.settings import BASE_DIR
from os import path

import json

class DataResolver:

    genre = json.loads(
        open(
            path.join(
                BASE_DIR, 
                "src",
                "config", 
                "genre.json"
            ), 
            'rt', 
            encoding='utf-8'
        ).read()
    )
    platform = json.loads(
        open(
            path.join(
                BASE_DIR, 
                "src",
                "config", 
                "platforms.json"
            ), 
            'rt', 
            encoding='utf-8'
        ).read()
    )
    publisher = json.loads(
        open(
            path.join(
                BASE_DIR, 
                "src",
                "config", 
                "publishers.json"
            ), 
            'rt', 
            encoding='utf-8'
        ).read()
    )


    @classmethod
    def resolve_platform(cls, platform):
        for key, value in cls.platform.items():
            if value == platform:
                return key

    @classmethod
    def resolve_genre(cls, genre):
        for key, value in cls.genre.items():
            if value == genre:
                return key

    @classmethod
    def resolve_publisher(cls, publisher):
        for key, value in cls.publisher.items():
            if value == publisher:
                return key