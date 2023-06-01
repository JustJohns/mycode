#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=6&category=11&difficulty=easy"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

if __name__ == "__main__":
    main()
