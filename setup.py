import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dexec",
    version_config=True,
    setup_requires=["setuptools-git-versioning"],
    author="Albert Peschar",
    author_email="albert@peschar.net",
    description="Easily run commands inside your projects' Docker containers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apeschar/dexec",
    project_urls={
        "Bug Tracker": "https://github.com/apeschar/dexec/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["dexec=dexec:main"]},
)
