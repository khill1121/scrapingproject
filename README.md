# Scraping GSA Auctions

This folder contains three files:
- README.md (this file)
- project.py 
- project.csv

## Goal of Scraping GSA Auctions

I originally planned to scrape all of the vehicles from the GSA Auction page. This would include information about the type of vehicle, current bid, location, and the date the auction closed. This would be useful for someone wanting to source a vehicle through government auctions, or someone that had an interest on what type of things the government auctions away (i.e. research).

### Step 1

It was clear from the urls on the page that I would need to use Selenium in order to scrape this website. The first step that I took was installing Selenium and used the web driver to click through each page. Originally, this script was very long. I eventually made it into a function so it would look more concise and would be easier to follow.

### Step 2

The next thing I did was run a test on one of the vehicles so I could try to seperate the information out into a clean format. I originally thought I'd be able to get some of the information from the main pages rather than needing to get everything from the detail page. However, the format made it so that all the information I needed would have to be extracted from each vehicle's page.

### Step 3

Knowing that having each vehicle's page would be **very** important made the next step an easy choice. I began to compile a list of partial urls for the vehicle pages. I expected this to be one of the easiest parts of this project, but it became one of the most challenging. The first function in the project.py file was created to make these partial urls into a list. This was done using the get_url function. The click of the button using Selenium was built into this function to make a concise file. The format of the urls meant they needed to be split. They inlcuded the numbers that made up partial urls for the vehicles, but not in the correct format.

### Step 4

The following for loop in the file is what makes formatting the partial urls possible. It splits the href attribute and then combines the base url with the portions of the partial url that we needed.

### Step 5 

The file function of the file was based around the test that I did on a vehicle page in step 2. I used what I knew worked on the individual page and made the write_csv function with a built in for loop that would loop through every url in the list built in the previous step and write them into rows on the file.

### Step 6

Finally I added a random sleep to the web driver portion of the first function so that I would be able to get more of the vehicles onto the csv file consistently.

## Challenges

I talked about many of the challenges in the steps outlined above. The most difficult challenges I encountered were definitely formatting the urls and getting a high percentage of vehicles returned to the csv consistently.
