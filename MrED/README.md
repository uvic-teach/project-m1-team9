# Mr. ED

The main webpage user interface for the Mr. ED project. Acts as a bridge for the user to access all microservices.

## To install requirements

    $ pip install -r requirements.txt

## To run Mr. ED

 NOTE: The webapp is configured to run on its Google Cloud deployment, located [here](https://mr-ed-dot-extreme-lodge-401820.wl.r.appspot.com/mred/). If the webapp is hosted locally, some source or reference links may not work as intended.

    $ python3 manage.py runserver [Host IP]:[Port]

 But to just run the development server on your local machine (default port is 8000):

    $ python3 manage.py runserver