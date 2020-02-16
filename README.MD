# OpenShift Flask Template

It's the example for using flask on OpenShift.

## Development

### Structure
```bash
openshift-flask-template  # Project name
├── .s2i
│   └── environment       # Settings for s2i image. Already listed common settings for the image.
├── apis
│   ├── __init__.py       # Collect all apis
│   └── time.py           # An api example.  
├── configs
│   └── production.py     # Settings for gunicorn, you can create another for testing purpose.
├── core
│   ├── __init__.py
│   └── connection.py     # The feature related with server/RDB connection. 
├── nginx.conf            # [Optional] If you want to deploy with nginx, this file can help you.
├── requirements.txt      # List required packages.
└── wsgi.py               # Entry point for the project
```

### Procedures
1. git clone this project.
2. Create a virtual environment through conda or other python virtual environment tool. More information can check following pages:
    * [Flask-Restplus official website](https://flask-restplus.readthedocs.io/en/stable/)
    * [Scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html)
    * [Request Parsing](https://flask-restplus.readthedocs.io/en/stable/parsing.html)
    * [Response marshalling](https://flask-restplus.readthedocs.io/en/stable/marshalling.html)
   
3. Rely on IDE's feature to install package automatically or use following command:
    ```bash
    pip install -r requirements.txt
    ```
4. Add new api to ```apis``` folder and modiftied ```__init__.py``` as well.
5. Run for debugging. You can use IDE to run wsgi.py main function or
    ```bash
    # Execution by python
    python wsgi.py
   
    # Execute with gunicorn
    gunicorn -c configs/production.py -b 0.0.0.0:8080 wsgi application
    ```

## Deployment on OpenShift
There're 2 images can help you to deploy your application easily.
 
### OpenShift's Python image
OpenShift offers a Python image which support deploy pthon code or Django application.
You can just select the ```python template``` from OpenShift console and given this git repo.
And everything should work fine.
 * Default port: 8080

### A predefined Python-Nginx image
If you want to make the web application work behind Nginx as a single application on OpenShift, you can follow by [the repo](https://github.com/justinhsz/image-bank/tree/master/python/nginx) to build your own.
 * Gunicorn port: 8081
 * Nginx port: 8080  

If you already have a application which is using OpenShift Python image, change the base image to this new one can even work fine.

I also provide a Django example with SimpleUI for this customized image, you should refer to [the repo](https://github.com/justinhsz/openshift-django-simpleui).