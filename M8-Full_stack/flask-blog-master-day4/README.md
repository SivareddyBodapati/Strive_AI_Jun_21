
# Flask Blog


<img src="src/static/blog.png">



## How to run project?

Write following terminal commands to run this project.


- Create .env file in root folder 


```

DATABASE_URL=postgresql://postgres:123456@localhost:5432/postgres
AUTH0_CALLBACK =http://localhost:5000/auth0/callback
AUTH0_DOMAIN=https://dev-0kcdjhuk.us.auth0.com
AUTH0_CLIENT_ID=uC1yDr9HRwSL8XPJPOQB9q6G39dogAL6
AUTH0_CLIENT_SECRET=-vMd3WsThssFvixtZ1ayi4WWdf_tFTPm6pl6_1pKf9PKi-NwCURAYNqXdRiI_TCH
FLASK_APP_SECRET_KEY=90a6e4a75e612142438943ffb4b5d651b4adaf6b3cdb79f7d40f448f3526c899

```


```sh

    git clone https://github.com/ubeytdemirr/flask-blog

    cd flask-blogs

    ## macos 

     python3 -m venv venv

    ## windows

    py -3 -m venv venv

    ## macos 

    . venv/bin/activate

    ## windows


    venv\Scripts\activate

    pip3 install -r requirements.txt

    python app.py


    * Serving Flask app 'app' (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 128-953-685


```


Go to  http://127.0.0.1:5000/  in your browser!
