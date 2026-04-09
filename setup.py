import os
import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Parse metadata from __version__.py without importing the package
metadata = {}
with open(os.path.join(HERE, "bromelia", "__version__.py")) as f:
    for line in f:
        for field in ("__version__", "__title__", "__license__", "__author__",
                      "__author_email__", "__description__", "__url__"):
            if line.startswith(field):
                metadata[field] = line.split("=", 1)[1].strip().strip('"\'')

# The text of the README file
with open(os.path.join(HERE, "README.md"), encoding="utf-8", mode="r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=metadata["__title__"],
    version=metadata["__version__"],
    license=metadata["__license__"],
    author=metadata["__author__"],
    author_email=metadata["__author_email__"],
    description=metadata["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=metadata["__url__"],
    download_url=f"https://github.com/heimiricmr/bromelia/releases/tag/v{metadata['__version__']}",
    packages=setuptools.find_packages(),
    include_package_data=True,
    keywords=[
        "DIAMETER", "3GPP", "EPC", "4G", "IMS",
        "TELECOM", "TELCO", "RFC6733", "RFC3588",
        "IETF", "VoLTE", "VoWiFi"
    ],
    install_requires=[
        "pyyaml"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony"
    ],
    python_requires=">=3.7"
)
