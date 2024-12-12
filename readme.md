# <p align="center">Matrimilan Python Working Guide</p>
#### <p align="center">A Comprehensive Flask RESTful API for Image Analysis and Moderation</p>
<hr/>
<p align="justify">The Matrimonial Python Working Guide is a developer-centric resource aimed at providing insights into the functionality and usage of the API. This guide offers detailed instructions on installing the API locally, along with explanations on how each endpoint operates. Developers can utilize this guide to understand the inner workings of the API and seamlessly integrate its features into their matrimonial applications.</p>


## 🛠️ Tech Stack
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [OpenCV](https://opencv.org/)
    

## 🚀 Install Dependencies  

### Clone this Repo 
### We need to create a environent for our Flask Program, Let's do that: 

Use this command to create a environment for python program.

```bash
python -m venv .venv #You can use you python version there like python3.10 is you are using multiple versions at same time
```
This will create a new folder name ```.venv``` where you can install all other dependencies.

### Let's go in the environment to install packages.
```bash
source .venv/bin/activate #Press enter to get into venv
```
To deactivate this or to get yourself out from the environment you just have to use 
```bash
deactivate
```

### Lets Install Dependencies:

```bash
pip install -r requirements.txt 
```
This will install every package we need to run this project. 

If you are unable to install there can be one reason that is ```uWSGI==2.0.24``` , you can comment this and reinstall it using ```pip install uWSGI==2.0.24```

You can also try to install all these packages

```python
absl-py==1.4.0
aniso8601==9.0.1
astunparse==1.6.3
better-profanity==0.7.0
cachetools==5.3.0
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
coloredlogs==15.0.1
Flask==3.0.2
Flask-RESTful==0.3.10
flatbuffers==23.3.3
gast==0.4.0
google-auth==2.16.2
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
grpcio==1.51.3
h5py==3.8.0
humanfriendly==10.0
idna==3.4
imageio==2.26.0
itsdangerous==2.1.2
Jinja2==3.1.2
keras==2.11.0
lazy_loader==0.1
libclang==15.0.6.1
Markdown==3.4.1
MarkupSafe==2.1.2
mpmath==1.3.0
networkx==3.0
NudeNetClassifier==2.1.1
numpy==1.24.1
oauthlib==3.2.2
onnxruntime==1.14.1
opencv-contrib-python==4.7.0.72
opencv-python==4.9.0.80
opencv-python-headless==4.7.0.72
opt-einsum==3.3.0
packaging==23.0
Pillow==10.2.0
progressbar2==4.2.0
protobuf==3.19.6
pyasn1==0.4.8
pyasn1-modules==0.2.8
pydload==1.0.9
python-utils==3.5.2
pytz==2022.7.1
PyWavelets==1.4.1
requests==2.28.2
requests-oauthlib==1.3.1
rsa==4.9
scikit-image==0.20.0
scipy==1.10.1
six==1.16.0
sympy==1.11.1
tensorboard==2.11.2
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.11.0
tensorflow-estimator==2.11.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==2.2.0
tifffile==2023.3.15
typing_extensions==4.5.0
urllib3==1.26.15
uWSGI==2.0.24
Werkzeug==2.2.2
wrapt==1.15.0

```
No we have installed everything we need lets run the program

### Running the project

```bash
python main.py #This will run your project on locahost:4000/5006
```


## 🧑🏻‍💻 API Refrence & Return Types 

### To get version of the project ```GET: {{host}}/api/v1/app/version``` [Test Endpoint].

This will return 
```json
{
    "version": String,
    "date": String // In YYYY-MM-DD format
}
```

### To get version of the project ```GET: {{host}}/api/v1/app/hello``` [Test Endpoint].

This will return 
```json
// In Hello there is multiple image so the return data will be something like this.
{
    "data": {
        "total_faces": [
            [
                5
            ],
            [
                1
            ]
        ],
        "nudities": [
            [
                {
                    "unsafe": 0.010312849655747414,
                    "safe": 0.9896871447563171
                }
            ],
            [
                {
                    "safe": 0.49506139755249023,
                    "unsafe": 0.504938542842865
                }
            ]
        ]
    }
}
```

### To get version of the project ```POST: {{host}}/api/v1/app/nudity```.
##### You can find nudity from two kind of data, First ```Local Image``` & ```Image URL```.
- #### Local Image (From Image Blob by uploading image)
> In Postman you can upload image from ```form-data``` using key & type as ```file``` and choosing the image. 

> In JS we can perform this using


- #### Local Image (From Image Blob by uploading image)
In Postman you can upload image from ```form-data``` using key & type as ```file``` and choosing the image. 

This will return 
```json
{
    "version": String,
    "date": String // In YYYY-MM-DD format
}
```




        
        
    