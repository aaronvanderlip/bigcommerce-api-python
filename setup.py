from setuptools import setup, find_packages

setup(
        name = 'bigcommerce-api',
        packages = find_packages(exclude=['tests']),
        include_package_data = True,
        version = '0.2',
        zip_safe = False,
        description = 'Python interface for connecting to BigCommerce API service',
        url = 'https://github.com/aaronvanderlip/bigcommerce-api-python'
        )
