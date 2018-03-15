JSON Vault
----------

When you're not Google-scale, and just need a little vault to hold some JSON data for later
processing.

Getting Started
===============

We'll use `pipenv` to handle the virtual environment, if that's new to you, check
out the project, it's useful (and the recommended way to do it going forward).

The idea is pretty basic-- you create projects in the app, and tokens to access
the storage API, then from your own app, or whatever application you care to
write a basic `requests` wrapper for, you can `POST` data to the app for
later

Clone the project down from github

    git clone https://github.com/doobeh/jsonvault.git
    cd jsonvault
    pipenv --three
    pipenv shell
    python setup.py install develop

Next we need to do the app configuration, which is easy:

    export FLASK_APP=app.py
    flask app init

You'll need to create a project and some tokens:

    git project create example
    git token create example

Then we're off to the races-- here's an example project I use to record
some Internet speed-test data:

    # example-logger.py

    import speedtest
    import requests

    servers = [1779]
    token = 'zaFxGyq4JOPRUHLQUpAJL3tMwTZP4vynDF0U7ulWyEn0RbZpsnmgUw'

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()

    r = requests.post(
        'http://192.168.1.100/example/store/',
        json={
            'token': token,
            'data': results_dict}
    )



