PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026> & "c:/Users/Estudiante/Desktop/clase docker 2-7-2026/.venv/Scripts/python.exe" "c:/Users/Estudiante/Desktop/clase docker 2-7-2026/datospython/programa.py"
 * Serving Flask app 'programa'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.209.10:5000
Press CTRL+C to quit
127.0.0.1 - - [02/Jul/2026 17:47:54] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [02/Jul/2026 17:47:54] "GET /favicon.ico HTTP/1.1" 404 -
PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& "c:\Users\Estudiante\Desktop\clase docker 2-7-2026\.venv\Scripts\Activate.ps1")
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026> docker build -t app-python . 
[+] Building 0.1s (1/1) FINISHED                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                  0.0s
 => => transferring dockerfile: 2B                                                    0.0s
ERROR: failed to build: failed to solve: failed to read dockerfile: open Dockerfile: no such file or directory

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/cepwz5893yyulhh30c3r4ilcl

What's next:
    Debug this build failure with Gordon → docker ai "help me fix this build failure"
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026> cd .\datospython\
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> cd .\datospython\

cd : No se encuentra la ruta de acceso 'C:\Users\Estudiante\Desktop\clase docker 
2-7-2026\datospython\datospython\' porque no existe.
En línea: 1 Carácter: 1
+ cd .\datospython\
+ ~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\Estudi...on\datospython\:String)  
   [Set-Location], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationComma 
   nd
 
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker build -t app-python .
[+] Building 9.6s (10/10) FINISHED                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                  0.0s
 => => transferring dockerfile: 227B                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.14-slim                   2.0s
 => [internal] load .dockerignore                                                     0.0s
 => => transferring context: 2B                                                       0.0s
 => [1/5] FROM docker.io/library/python:3.14-slim@sha256:b877e50bd90de10af8d82c57a02  4.2s
 => => resolve docker.io/library/python:3.14-slim@sha256:b877e50bd90de10af8d82c57a02  0.0s
 => => sha256:a6e80813257d3fdcf4f042c5d2d78c823190075e0d513c74bb77a6f775 249B / 249B  0.2s
 => => sha256:10487245a8aa8553a15e03dd034bdf587d83b26bba680a92e085 12.34MB / 12.34MB  3.8s
 => => sha256:606f83be173854196a130115198021e2aea50af13cf2d67480e5d3 1.29MB / 1.29MB  1.2s
 => => extracting sha256:606f83be173854196a130115198021e2aea50af13cf2d67480e5d3fdbe0  0.1s
 => => extracting sha256:10487245a8aa8553a15e03dd034bdf587d83b26bba680a92e085971b9d3  0.2s
 => => extracting sha256:a6e80813257d3fdcf4f042c5d2d78c823190075e0d513c74bb77a6f7756  0.0s
 => [internal] load build context                                                     0.0s
 => => transferring context: 576B                                                     0.0s
 => [2/5] WORKDIR /app                                                                0.0s
 => [3/5] COPY requirements.txt .                                                     0.0s
 => [4/5] RUN python -m pip install --no-cache-dir -r requirements.txt                2.5s
 => [5/5] COPY . .                                                                    0.0s
 => exporting to image                                                                0.6s
 => => exporting layers                                                               0.4s
 => => exporting manifest sha256:3e0617f8b06cc6a444dae95ffd24df29b443025becf063b4afd  0.0s
 => => exporting config sha256:ae0418f831b729837807098a3f081161769354c207cedbe67264b  0.0s
 => => exporting attestation manifest sha256:087376f86cf617c3f4319e0a33b6fa63ae69392  0.0s
 => => exporting manifest list sha256:bbc00d6437b3bc4e9cc63a55e4c0d52db83df1eceebcb3  0.0s
 => => naming to docker.io/library/app-python:latest                                  0.0s
 => => unpacking to docker.io/library/app-python:latest                               0.1s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/2354g74qlu84ovzkafphx1vax
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d -p 3000:5000 --name pythonapp app-python
e9b8556edb84c0e5bd86adb2e9d226ab26dc48f863007cb7be1f6240ad68053c
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker save -o mypython.tar app-python
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker load -i mypython.tar
Loaded image: app-python:latest
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d -p 3000:5000 --name pythonapp app-python
30f00330e0787a5e587fd8f65c1582f265275c99418a9c9c7fb9ec738bccb0c0
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> dockker pull mysql:8.0
dockker : El término 'dockker' no se reconoce como nombre de un cmdlet, función, archivo 
de script o programa ejecutable. Compruebe si escribió correctamente el nombre o, si 
incluyó una ruta de acceso, compruebe que dicha ruta es correcta e inténtelo de nuevo.
En línea: 1 Carácter: 1
+ dockker pull mysql:8.0
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (dockker:String) [], CommandNotFoundExcepti 
   on
    + FullyQualifiedErrorId : CommandNotFoundException
 
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker pull mysql:8.0 
8.0: Pulling from library/mysql
96d30d9fbee8: Download complete 
96d30d9fbee8: Pull complete 
7534d1db9f8d: Pull complete 
49ec2dab01d9: Pull complete 
6ef6c7b50a93: Pull complete 
ab24264a27e9: Pull complete 
e3e5d1ac74c1: Pull complete 
4c8a3e0d4e4b: Pull complete 
0d74d296605b: Pull complete 
edf85873f64e: Pull complete 
a63160a5eda1: Pull complete 
796812c73292: Download complete 
af166387641d: Download complete 
Digest: sha256:7dcddc01f13bab2f15cde676d44d01f61fc9f99fe7785e86196dfc07d358ae2b
Status: Downloaded newer image for mysql:8.0
docker.io/library/mysql:8.0

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview mysql:8.0
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD:123456 -E MYSQL_DATABASE=empresa

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
unknown shorthand flag: 'E' in -E

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run 'docker run --help' for more information
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD:123456 -E MYSQL_DATABASE=empresa -p 0122:3306

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
unknown shorthand flag: 'E' in -E

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run 'docker run --help' for more information
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD:123456 -E MYSQL_DATABASE=empresa -p 0122:3306 -v mysql_data:/var/lib/mysql mysql:8.0

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"
unknown shorthand flag: 'E' in -E

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run 'docker run --help' for more information
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD:123456 -e MYSQL_DATABASE=empresa -p 0122:3306 -v mysql_data:/var/lib/mysql mysql:8.0
fb3570c1930390932ee12e527f626051e8a8635b3332755abd7d5a5ad377985e
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver2 -e MYSQL_ROOT_PASSWORD:123456 -e MYSQL_DATABASE=empresa -p 3609:3306 -v mysql_data:/var/lib/mysql mysql:8.0
9c67764d4f019c70c66619bca0c1aee376b7999a0faae81296435fbb7c56d382
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver2 -e MYSQL_ROOT_PASSWORD:123456 -e MYSQL_DATABASE=empresa -p 3609:3306 -v mysql_data:/var/lib/mysql mysql:8.0
Unable to find image 'mysql:8.0' locally
8.0: Pulling from library/mysql
297d04cfe470: Download complete 
ab24264a27e9: Download complete 
96d30d9fbee8: Download complete 
e3e5d1ac74c1: Download complete 
0d74d296605b: Download complete 
6ef6c7b50a93: Download complete 
4c8a3e0d4e4b: Download complete 
edf85873f64e: Downloading [==================================>                ]  32.51MB/47.31MB
49ec2dab01d9: Downloading [============>                                      ]  33.55MB/129.4MB
a63160a5eda1: Downloading [=================================>                 ]  33.55MB/49.93MB
7534d1db9f8d: Download complete 
796812c73292: Download complete 
af166387641d: Download complete 
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> ^C
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> ^C
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver2 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=empresa -p 3609:3306 -v mysql_data:/var/lib/mysql mysql:8.0
Unable to find image 'mysql:8.0' locally
8.0: Pulling from library/mysql
96d30d9fbee8: Pulling fs layer 
6ef6c7b50a93: Pulling fs layer 
e3e5d1ac74c1: Pulling fs layer 
49ec2dab01d9: Pulling fs layer 
0d74d296605b: Pulling fs layer 
7534d1db9f8d: Pulling fs layer 
4c8a3e0d4e4b: Pulling fs layer 
ab24264a27e9: Pulling fs layer 
a63160a5eda1: Pulling fs layer 
297d04cfe470: Pulling fs layer 
edf85873f64e: Pulling fs layer 
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker run -d --name mysqlserver -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=empresa -p 3609:3306 -v mysql_data:/var/lib/mysql mysql:8.0 
Unable to find image 'mysql:8.0' locally
8.0: Pulling from library/mysql
96d30d9fbee8: Pulling fs layer 
49ec2dab01d9: Pulling fs layer 
ab24264a27e9: Pulling fs layer 
Digest: sha256:7dcddc01f13bab2f15cde676d44d01f61fc9f99fe7785e86196dfc07d358ae2b
Status: Downloaded newer image for mysql:8.0
7fa52cccc2c5aac60c483aeb87ac4523068168035007ddc03a6957539f20b37d
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> docker exec mysqlserver mysqldump -u root -p123456 empresa > empresa.sql                                                                    
mysqldump: [Warning] Using a password on the command line interface can be insecure.
(.venv) PS C:\Users\Estudiante\Desktop\clase docker 2-7-2026\datospython> 