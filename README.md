# jupyter-vapor-vnc-proxy
Extensión de JupyterLab para ejecutar VAPOR desde un servidor VNC

Instrucciones:

1. Se crea un usuario a traves de ssh. Para mayor información dirigirse al siguiente enlace:
   
https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04

2. Se inicia sesión usando el protocolo SSH:
```bash
ssh usuario@ip_de_host
```
3. Se instalan paquetes importantes como noVNC, websockify, xfce4 y TigerVNC
```bash
sudo apt update
sudo apt install xfce4 xfce4-goodies novnc websockify -y
sudo apt install tigervnc-standalone-server
```
4. Se inicializa vncserver:
```bash
vncserver #Se indica contraseña
vncserver -kill :1
```
5. Se descarga e instala Miniforge:
```bash
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```
6. Creamos un entorno e instalamos los siguientes paquetes:
```bash
mamba install jupyterlab
mamba install -c conda-forge jupyter-server-proxy
```
7. Inicializamos el servidor JupyterLab para que se cree la carpeta "/.jupyter"
```bash
jupyter-lab --no-browser
```   
8. Instalar NCAR Vapor. Dejando la carpeta con los archivos bin en el directorio principal $HOME (home/usuario)
```bash
curl -L -O https://github.com/NCAR/VAPOR/releases/download/3.8.1/VAPOR3-3.8.1-Ubuntu18.sh
bash VAPOR3-3.8.1-Ubuntu18.sh
```
9. Se instalan las siguientes paqueterías para que Vapor pueda funcionar:
```bash
sudo apt-get install lsb-core
sudo add-apt-repository ppa:kisak/kisak-mesa #Estos son los drivers de la tarjeta grafica "AMD" que actualizan OpenGL. Para el fabricante "NVIDIA" deben buscarse los drivers correspondientes.
sudo apt updatesudo apt full-upgrade
```
10. Descargar la extensión de jupyter-vapor-vnc-proxy de este repositorio:
```bash
python -m pip install https://github.com/AntonioOlay/jupyter-vapor-vnc-proxy/archive/0.0.1.tar.gz
```
11. Movemos el archivo "config_novnc.sh" a la carpeta .jupyter
