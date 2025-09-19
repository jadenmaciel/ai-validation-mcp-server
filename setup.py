#!/usr/bin/env python3
"""
Setup script for AI Validation MCP Server
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-validation-mcp-server",
    version="2.0.0",
    author="AI Validation Team",
    author_email="",
    description="A world-class prompt engineering MCP server for automatic prompt optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jadenmaciel/ai-validation-mcp-server",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-validation-mcp=ai_validation_mcp:main",
        ],
    },
    keywords="mcp model-context-protocol prompt-engineering ai llm cursor-ide",
    project_urls={
        "Bug Reports": "https://github.com/jadenmaciel/ai-validation-mcp-server/issues",
        "Source": "https://github.com/jadenmaciel/ai-validation-mcp-server",
        "Documentation": "https://github.com/jadenmaciel/ai-validation-mcp-server/blob/main/README.md",
    },
)
