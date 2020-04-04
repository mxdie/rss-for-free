from setuptools import setup,find_packages
setup(
    name = 'rss_for_free',
    version ='1.1',
    author = 'mxdie',
    python_requires='>=3',
    author_email = 'leurd@qq.com',
    description=("This is a script of pt"),
    entry_points={'console_scripts': [
        'rff = rss_for_free.__main__:main',
    ]},
    packages = find_packages('src'),#['src/rss_for_free'],#
    package_dir = {'' : 'src'},
    install_requires = [],
    zip_safe=False
)
