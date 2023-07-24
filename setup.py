import setuptools

VERSION = "0.1.0"  # PEP-440

NAME = "st_files_connection"

INSTALL_REQUIRES = [
    "streamlit>=1.22",
    "fsspec"
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="Streamlit Connection for cloud and remote file storage.",
    url="https://github.com/streamlit/files-connection",
    project_urls={
        "Source Code": "https://github.com/streamlit/files-connection",
    },
    author="Snowflake Inc",
    author_email="hello@streamlit.io",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["st_files_connection"]
)