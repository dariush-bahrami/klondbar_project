import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="klondbar",
    version="0.1.4",
    author="dAriush Bahrami",
    author_email="dariush.bahrami@ut.ac.ir",
    description="A simple progress bar with lots of customization \(^-^)/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/dariush-bahrami/klondbar_project.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)