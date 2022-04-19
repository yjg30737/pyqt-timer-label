from setuptools import setup, find_packages

setup(
    name='pyqt-timer-label',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QLabel for timer feature',
    url='https://github.com/yjg30737/pyqt-timer-label.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-responsive-label @ git+https://git@github.com/yjg30737/pyqt-responsive-label.git@main'
    ]
)