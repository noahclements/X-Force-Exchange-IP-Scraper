# X-Force Exchange IP Info Scraper
Takes IP's and outputs their X-Force Exchange risk score if its greater than 4.
This was made to go through hundreds of DNS IP records in minutes rather than hours.

Takes raw copied data from a text file that includes IP's, scrapes for just IP's, then calls the X-Force Exchange API to return the risk score of the IP.
