from setuptools import setup, find_packages

setuptools.setup(
    name="jupyter-vapor-vnc-proxy",
    packages=setuptools.find_packages(where='.'),
    version='0.0.2',
    description="Extension de Jupyter que ejecuta NCAR Vapor desde VNC",
    keywords=["Jupyter"],
    entry_points={
        'jupyter_serverproxy_servers': [
            'VAPOR_VNC_SERVER = jupyter_vapor_vnc_proxy:setup_vapor_desktop',
        ]
    },
    install_requires=['jupyter-server-proxy>=1.4.0'],
    package_data={'jupyter_vapor_vnc_proxy': ['resources/*']},
    include_package_data=True,
    zip_safe=False
)
