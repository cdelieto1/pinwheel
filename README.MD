# Webscrape Coding Challenge - IRS Form Webscrape and .Pdf Download.

This exercise contains two parts:

1. Using BeautifulSoup4, scrape the IRS webiste (website = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html") to return a list of results for only the specified requested form name (ex: "Form W-2", "Form 1095-C"). Results will be returned as JSON for an exact match only and only inlude the newest + oldest year available for a given form:


[
{
"form_number": "Form W-2",
"form_title": "Wage and Tax Statement (Info Copy Only)",
"min_year": 1954,
"max_year": 2021
}
...
]

2. Create and download a subdirectory that downloaded the form name onto the current working directory and downloaded each individual .pdf available into the folder as an exact match only: (ex: Form W-2/Form W-2 - 2020.pdf).

## Installation:

$ cd pinwheel
$ virtualenv env
$ source env/bin/activate 
$ pip3 install -r requirements
$ python3 irs_webscrape.py


## Version of Python3: 

python3 --version (Python 3.6.9)

### Challenges (in order of how they appeared):
* Which URL to scrape from. 
* 

