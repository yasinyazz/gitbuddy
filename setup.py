# setup.py
from setuptools import setup

setup(
    name="gitbuddy",
    version="1.0.0",
    py_modules=["gitbuddy"],
    entry_points={
        "console_scripts": [
            "gitbuddy=gitbuddy:main_menu",
        ],
    },
)
