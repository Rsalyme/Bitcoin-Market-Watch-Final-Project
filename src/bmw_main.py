# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 17:06:16 2014

@author: RuudSalym
"""
import api

#we select the exchanges we want to track

ripple =api.Exchange('Ripple', 'https://ripple.com/')
bitstamp =api.Exchange('Bitstamp','https://www.bitstamp.net/')
itBit =api.Exchange('Itbit', 'https://www.itbit.com/')
#we now bring in the api from bitcoin charts in order to later use this data to get our market prices
bitcoin = api.Web_api('Bitcoin','http://api.bitcoincharts.com/v1/markets.json')
#this reads the json api and then
bitcoin.openapi()
#we now save that data in variable called
market_data = bitcoin.data
#this function pulls the data and converts the json array into a dictionary so that we can manipulate the data we're looking for
def currency_watch(market_data):
    inc = 0
    my_output = {}
    
    while inc < len(market_data):
        #This is when we go through each individual dictionary
        currency = market_data[inc]['currency']
        ask = market_data[inc]['ask']
        exchange = market_data[inc]['symbol']
        if market_data[inc]["currency"] == "USD":
            my_output[exchange] = [exchange, ask]
            market_update = str(exchange) + " $" + str(ask) + " " + str(currency)
        inc = inc + 1
    return my_output
#we save the dictionaries into a variable so that we can reference them later when we want the output of the prices       
markets_dict = currency_watch(market_data) 

#each exchange that we selected earlier in the program is now called and saved into a variable where the output is properly formatted        
ripple_out = markets_dict['rippleUSD'][0] +  str(" $") + str(markets_dict['rippleUSD'][1])
bitstamp_out = markets_dict['bitstampUSD'][0] +  str(" $") + str(markets_dict['bitstampUSD'][1])
itBit_out = markets_dict['itbitUSD'][0] +  str(" $") + str(markets_dict['itbitUSD'][1])
#this shows us that the variables print the prices and exchnages properly
print ripple_out 
print bitstamp_out
print itBit_out
#we save our final output in this variable so that we can now use the variable exchange to send our text message 
exchanges = str("These are the current prices for bitcoin right now: ") + ripple_out + str(" ")+ bitstamp_out+ str(" ")+ itBit_out
#this is what the exchanges variable looks like
print exchanges


#we now import the twilio api and use it to send a text to our phone
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)


#the variable exchanges is now used to send the text message as demonstrated earlier 
message = client.messages.create(body= exchanges,
#this actually features my number so use your own if needed
    to="+your number here",    # Replace with your phone number
    from_="+18607852845") # Replace with your Twilio number
    
print message.sid

#these open the webpages of the exchanges we're tracking so that if we see enough variance in price we can act accordingly and buy or sell our bitcoin
ripple.openurl()
bitstamp.openurl()
itBit.openurl()
