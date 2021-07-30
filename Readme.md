# Currency-Api
At this point this is a quick minimal implementation implementation of an API to compute currency exchange rates. 
## To Run
The dockerfile hasn't been verified yet. During the process of checking it out my Docker Desktop had a catostrophic error so I'll complete the docker piece after I debug my Docker Desktop.

In the meantime you can run the api in Visual Code by by doing the following:

    # Open a bash terminal and clone the git repository
    git clone https://github.com/timeonator/currency-api .
    cd currency-api

    # Setup python virtual environment
    python3 -m venv .venv
    # activate the venv like this
    source .venv/Scripts/activate

    # install the library dependencies
    pip install -r requierments.txt
    
    # run the app
    flask run

## End Points

     localhost:/convert/<from_currency>/<to_currency>
give the exchange rate from the <from_currency> to the <to_currency>

     localhost:/rates
List the rates relative to USD for all the currencies available from (https://freecurrencyapi.net/api/v1/rates?base_currency=USD)

