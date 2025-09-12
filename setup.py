from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="rag_medical_chatbot",
    version="0.1",
    author="huongtd",
    packages=find_packages(),
    install_requires = requirements,
)