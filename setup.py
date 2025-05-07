from setuptools import setup, find_packages

setup(
    name="Proyecto_integrador_5",
    version="0.0.1",
    author="Valentina Ayala",
    author_email="",
    description="",
    py_modules=["actividad_1", "actividad_2"],
    install_requires=[
        "pandas==2.1.4",       
        "openpyxl==3.1.2",    
        "requests==2.31.0",   
        "yfinance==0.2.28"   
    ]
)