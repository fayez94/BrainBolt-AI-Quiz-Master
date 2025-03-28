from setuptools import find_packages,setup

setup(
    name='BrainBolt',
    version='0.0.1',
    author='Mohammad Fayez Ullah',
    author_email='fayezullahcox1131@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)