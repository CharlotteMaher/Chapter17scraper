############################################################################## Chapter 17.
###############################################################################

import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
#defining parameter here - can change root to any word in this function (jim example)- put filling here 
def scrape_table(root):
    rows = root.cssselect("table.Trolley.table tr") # selects all <tr> blocks within <table class="Trolley table"> 
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("td")
        if table_cells: 
            table_cellsurls = table_cells[1].cssselect("a")
            record['HospitalURL'] = table_cellsurls[1].attrib.get('href')
            record['Date'] = table_cells[0].text
            record['Hospital'] = table_cells[1].text
            record['Region'] = table_cells[2].text
            record['Trolley total'] = table_cells[3].text
            record['Ward total'] = table_cells[4].text
            # Print out the data we've gathered
            print record, '------------'
           # Finally, save the record to the datastore - 'Artist' is our unique key
        scraperwiki.sqlite.save(["Hospital"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
#url in this example is the parameter (general filling)- defining the parameter- can put startingurl here and will work.
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    print html
    #root here is being defined as argument- the specific filling. 
    root = lxml.html.fromstring(html)
    scrape_table(root)
#deleted previous code from chapter 16 scraper because only scraping one page
# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then call a function to scrape it
starting_url = 'http://inmo.ie/6022'
scrape_and_look_for_next_link(starting_url)
#the starting url is the argument (specific filling) - defining the actual argument used in the function above. 


