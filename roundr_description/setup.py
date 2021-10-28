from setuptools import setup

package_name = 'roundr_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='linzhank',
    maintainer_email='linzhank@gmail.com',
    description='RoundRobot description package',
    license='GNU General Public License version 3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
