from setuptools import setup

setup(
    install_requires=["schedule"],
    entry_points={
        "console_scripts": [
            "alarm = app:main"
        ]
    }
)
