# Currency-Api
At this point this is a quick minimal implementation implementation of an API to compute currency exchange rates. 
## To Run
### Run From a bash CLI

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
    
## Build and Run a Docker Container
The app is configured to list on port 5000. To build the docker image you can use the following from the project root

     docker build -t currency-api .

To run the image in a container run

     docker run --name currency-api -p 5000:5000 -it -d currency-api

## End Points

     localhost:/convert/<from_currency>/<to_currency>
give the exchange rate from the <from_currency> to the <to_currency>

     localhost:/rates
List the rates relative to USD for all the currencies available from (https://freecurrencyapi.net/api/v1/rates?base_currency=USD)

