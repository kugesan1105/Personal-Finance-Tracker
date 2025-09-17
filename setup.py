from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="personal-finance-tracker",
    version="1.0.0",
    description="A comprehensive personal finance management application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Finance Team",
    author_email="finance@example.com",
    url="https://github.com/yourorg/personal-finance-tracker",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "pytest>=6.0.0",
    ],
    extras_require={
        "dev": [
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "finance-tracker=main:main",
        ],
    },
    keywords="finance, personal finance, money management, budgeting, expenses, income tracking",
)