import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="owotranslator",
    version="0.0.3",
    author="Vimal",
    author_email="usvimal@gmail.com",
    description="A package that owoifies your text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usvimal/owotranslator",
    download_url = 'https://github.com/usvimal/owotrans/archive/0.0.3.tar.gz',
    packages=setuptools.find_packages(),
    use_scm_version={'write_to': '%s/_version.py' % 'owotrans'},
    setup_requires=['setuptools_scm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
