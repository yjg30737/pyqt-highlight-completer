from setuptools import setup, find_packages

setup(
    name='pyqt-highlight-completer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt highlight completer',
    url='https://github.com/yjg30737/pyqt-highlight-completer.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)