# Coding Challenge - IRS Form Webscrape and .Pdf Download.

This exercise contains two parts:

1. Using BeautifulSoup4, scrape the IRS webiste (website = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html") to return a list of results for only the specified requested form name (ex: "Form W-2", "Form 1095-C"). Results will be returned as JSON for an exact match only and only inlude the newest + oldest year available for a given form:

```
[
{
"form_number": "Form W-2",
"form_title": "Wage and Tax Statement (Info Copy Only)",
"min_year": 1954,
"max_year": 2021
}
...
]
```
2. Create and download a subdirectory that downloads the form name onto the current working directory and populates it with each individual .pdf available as an exact match only: (ex: Form W-2/Form W-2 - 2020.pdf).


## Installation:
```
$ cd pinwheel
$ virtualenv env
$ source env/bin/activate 
$ pip3 install -r requirements
$ python3 irs_webscrape.py
```

## Version of Python3: 

python3 --version (Python 3.6.9)


### Challenges (in order of how they appeared):

* Which URL to scrape from. The URL I had constructed originally was throwing an error after >3 get requests. I had to play around with how I was constructing the URL to prevent blocking while debugging (I could have also setup another proxy to call the request from)
* Setting up the JSON for max_year and min_year. I attempted to create a function that checks against all other years to return (max_year, min_year) but had no luck so I just grabbed the first and last elements in the dictionary as the results were sorted in the form (isDescending = False).
* Filtering out similiar form names. I had to add extra logic to ensure the raw input matched the text within the html a href link.
* Nesting functions and if/else conditions. The information either pulled nothing or pulled incorrectly depending upon where it was nested in the logic.
* Invalid forms still created subdirectories with their invalid form and populated 



### Optimizations:

* Offer a fuzzy logic dropdown menu of forms that match the input before proceeding with the scrape. (ex: input: "W-2" ; output: Did you mean "Form W-2" or "Inst W-2 and W-3"? (y/n)). 
* Build current logic into a Class so we can flag it as IS_DEBUG = sandbox for testing and fetching/debugging.  
