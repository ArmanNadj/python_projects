#Author and Purpose:
# Author: Arman Nadjarian
# This project is ONLY for the purposes of learning how to interact with API's
# To test the project, run "python3 crypto_exchange_rates.py" in the terminal/cmd prompt
# with a working "python3" interpreter installed.


#Project Goal:
# Implement the CoinLayer API in order to gather and calculate
# exchange rates between two crypto currencies in the current market.

import urllib.request

#open_and_retrieve:
# RETURNS: the dictionary data of all cryptos and their corresponding unit values in the market
# This function enters the internet with a URL linked to my CoinLayer account via access key.
# This URL accesses the CoinLayer API and pulls a formatted dictionary 
# with the needed rates of each crypto.
# After pulling the string in proper decoded format, the string is parsed
# in order to remove unnecessary information and excess characters.
# Following the removal of excess characters, string is parsed again in order to retrieve data

def open_and_retrieve(api_access_url: str):
    fstr = urllib.request.urlopen(api_access_url)
    decoded_string = fstr.read().decode(fstr.headers.get_content_charset())

    #Throw away preliminary information which is useless to our end goal.
    #this line saves the string slice which begins after the key phrase "rates" inside of the formatted
    #string. This ensures the unnecessary data prior to the crypto rates is not captured.
    #We add 8 to the index to make sure we remove the word "rates": entirely from our return string
    formatted_rates = decoded_string[(decoded_string.find('\"rates\":') + 8)::]

    #remove excess characters from the formatted dictionary
    formatted_rates = formatted_rates.replace("{", "")
    formatted_rates = formatted_rates.replace("}", "")
    formatted_rates = formatted_rates.replace("\"", "")
    formatted_rates = formatted_rates.replace("\'", "")

    rates = {str : float}
    pairs = formatted_rates.split(",")                                                                                                                                                                             
    for entry in pairs:                                                                                                                                                                                      
        var, val = entry.split(":")                                                                                                                                                                          
        rates[var] = float(val) 
    
    return rates

#query():
# RETURNS: boolean value representing whether to run another query or not
# This functions runs the query by performing calculations based on
# the data from the open_and_retrieve() function
def query() -> bool:
    #coin_layer_base_url = "http://api.coinlayer.com/api/"
    coin_layer_api_access_url = "http://api.coinlayer.com/api/live?access_key=abe3e46f815c1dc45c71df64e06de867"
    rates = open_and_retrieve(coin_layer_api_access_url)

    #Obtaining first crypto to compare with
    first_crypto = input("Input the beginning crypto name: ")
    while first_crypto.upper() not in rates.keys():
        first_crypto = input("Invalid entry. Enter a valid crypto acronym: ")
    first_crypto = first_crypto.upper()

    #Obtaining second crypto to compare with
    second_crypto = input("Input the name of the desired crypto: ")
    while second_crypto.upper() not in rates.keys():
        second_crypto = input("Invalid entry. Enter a valid crypto acronym: ")
    second_crypto = second_crypto.upper()
    

    #Calculating and printing results

    first_crypto_amount = float(input("How much of " + first_crypto + " are you trading: "))
    while first_crypto_amount < 0:
        first_crypto_amount = float(input("Cannot have crypto amount be less than 0. Try again: "))


    resultant_exchange_rate = (rates[second_crypto] / rates[first_crypto])

    dollar_amt = rates[first_crypto] * first_crypto_amount

    print("\n\nCryptos Selected: ")
    print(f"{first_crypto} is currently trading at ${rates[first_crypto]} per share")
    print(f"{second_crypto} is currently trading at ${rates[second_crypto]} per share")

    print(f"\nThe current exchange rate is:\n\t{resultant_exchange_rate} of {first_crypto}, for each {second_crypto}")
    print(f"\tand {1 / resultant_exchange_rate} of {second_crypto}, for each {first_crypto}\n")
    print(f"\nAfter trading {first_crypto_amount} shares of {first_crypto}, you will have {dollar_amt / rates[second_crypto]} shares of {second_crypto}\n")
    print(f"Thus...you will have ${dollar_amt} of USD invested in {second_crypto}")


    #Perform another query?
    another = input("Perform another query? (yes/no): ")
    if another[0].lower() == 'y':
        print("\nPreparing to run another query...\n")
        return True
    else:
        print("\nGoodbye!\n")
        return False



def main():
    another: bool = query()
    while another:
        another = query()


#main entry into program
if __name__ == "__main__":
    main()