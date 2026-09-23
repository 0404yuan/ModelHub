from setuptools import setup, find_packages

setup(
    name="llama",
    version="0.0.1",
    description="Inference code for LLaMA models",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "fairscale",
        "fire",
        "sentencepiece",
    ],
)
