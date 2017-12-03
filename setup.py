from distutils.core import setup

setup(
        name='clmenu',
        packages = ['clmenu'],
        version = '1.0',
        description = 'A small tool for making an arrow menu in console applications',
        author = 'Jordan Patterson',
        author_email = 'jordanpatterson2398@gmail.com',
        license='MIT',
        url = 'https://github.com/jordantdkt/menu',
        download_url='https://jordantdk@bitbucket.org/jordantdk/menu.git',
        install_requires=["termcolor"]
)
