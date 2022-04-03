import setuptools

setuptools.setup(name='arrcsv',
    version='0.0.1',
    description='A python package for converting array to csv',
    keywords = ['convert', 'array', 'csv'],
    url='https://github.com/saularis/arrcsv',
    download_url='https://github.com/saularis/arrcsv/archive/refs/tags/v0.0.1.tar.gz',
    author='Abdulla Malik',
    install_requires=['numpy'],
    author_email='hi@abdulla.dev',
    packages=setuptools.find_packages(),
    zip_safe=False
)