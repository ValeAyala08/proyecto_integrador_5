from setuptools import setup, find_packages

setup(
    name="Proyecto_integrador_5",
    version="0.0.1",
    author="Valentina Ayala",
    author_email="",
    description="",
    py_modules=["actividad_1","actividad_2"],
    install_requires=[
        "pandas==2.2.3",
        "openpyxl",
        "requests==2.32.3",
        "yfinance==0.2.59"
    ]
) 