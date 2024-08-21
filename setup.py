from setuptools import find_packages, setup



setup(
    name="Tradingbot",
    version="0.0.1",
    author="svmamidi",
    author_email="satya.mamidi09@gmail.com",
    packages =find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]
)