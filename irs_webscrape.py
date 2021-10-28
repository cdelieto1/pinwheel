"""Taking a list of tax form names (ex: "Form W-2", "Form 1095-C"), search the website and
return some informational results. Specifically, you must return the "Product Number",
the "Title", and the maximum and minimum years the form is available for download. The
forms returned should be an exact match for the input (ex: "Form W-2" should not return
"Form W-2 P", etc.) The results should be returned as json, in the format of the following
example:

[
{
"form_number": "Form W-2",
"form_title": "Wage and Tax Statement (Info Copy Only)",
"min_year": 1954,
"max_year": 2021
}
...
]

Next, Take a tax form name (ex: "Form W-2") and a range of years (inclusive, 2018-2020
should fetch three years), download all PDFs available within that range. The forms
returned should be an exact match for the input (ex: "Form W-2" should not return "Form
W-2 P", etc.) The downloaded PDFs should be downloaded to a subdirectory under your
script's main directory with the name of the form, and the file name should be the "Form
Name - Year" (ex: Form W-2/Form W-2 - 2020.pdf)


"""

# START SOLUTION

import os 
import requests
import json
from bs4 import BeautifulSoup, SoupStrainer


# Hard code a sample form for testing purposes and format for proper URL query.
form_input = "Form W-2"
formatted_form = form_input.rstrip().replace(" ", "+").lower()

# Base website 
website = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"

# Do a search on a form and append the sort arrow. This ensures you only get data about the exact form in the query.  
URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value=" + formatted_form + "&isDescending=false"

# Request site's content if status = 200.
try:
    site = requests.get(URL)
except:
    print("IRS website couldn't be reached just now.")


form_info = []

# Parse the even/odd Class to pull the values out of the td elements. SoupStrainer doesn't parse faster but saves memory. 
def grab_json_values():
    for ele in BeautifulSoup(site.content, parse_only=SoupStrainer(True, {'class':['even','odd']}), features="html.parser"):

        form_number = ele.find("td", class_="LeftCellSpacer")

        # Grab the text specifying the exact form within the html
        form_product_number = form_number.text.strip()

        # The <a> tag is embedded within the LeftCellSpacer. Alternate: form_direct_link = ele.find('a', href=True)
        form_link = form_number.a["href"]
        final_form_number = ""
        form_title = ele.find("td", class_="MiddleCellSpacer")
        form_year = ele.find("td", class_="EndCellSpacer")

        # I had to check against the product number text in order to pull an exact match only.  
        if form_number and form_number != "" and form_input.strip().lower() == form_product_number.lower():
            form_info.append({"form_number": form_number.text.strip(), "form_title": form_title.text.strip(), "form_year": form_year.text.strip() })

            # # DO NOT TOUCH (over-indentation pulls extra similar matches!) 
            create_dir_for_form(formatted_form, form_link)
        elif not ele:
            print("No downloads available due to this form being invalid. Check your spelling and try again.")
            break    


    # Info is populated into array and a print statement shows the year in descending order. 
    # print(form_info[0]['form_number'])
    # print(form_info[0]['form_title'])
    # print(form_info[0]['form_year'])
    # print(form_info[len(form_info)-1]['form_year'])


    #max_year = min_year = int(form_info[0]['form_year'])
    final_values =[]

    # for i in range(len(form_info)):
    #     if int(form_info[i]['form_year']) > max_year:
    #         max_year = int(form_info[i]['form_year'])
    #     elif int(form_info[i]['form_year']) < min_year:
    #         min_year = int(form_info[i]['form_year'])
    #         return (max_year, min_year)   
        

    if form_info and form_info[0]['form_year'] <= form_info[0]['form_year'] :
        final_values.append(({"form_number": form_number.text.strip(),
                                              "form_title": form_title.text.strip(),
                                              "min_year": form_info[len(form_info)-1]['form_year'], 
                                              "max_year": form_info[0]['form_year']}))
        print(" ")
        print("JSON representation of form number, title, oldest date available and newest date available: ")
        print(" ")
        print(json.dumps(final_values, indent=4))

        # # #  WILL ONLY DOWNLOAD 1 PDF IF YOU CALL FUNCTION FROM HERE
        # create_dir_for_form(formatted_form, form_link)


# Save .pdf filename to path='Form W-2/Form W-2 - 2020.pdf for all available years.
def create_dir_for_form(formatted_form, form_link):

    formatted_folder = formatted_form.replace("+"," ")

    # grab the name of the unique .pdf only.
    path = os.path.join(formatted_folder, form_link.split("/")[-1])

    # create the subdirectory if it doesn't exist. Will not prevent overwriting the .pdfs into the file. 
    if not os.path.exists(formatted_folder):
        os.makedirs(formatted_folder)

    print(f"Saving form link= {form_link} to subdirectory = {path}")
    with open(path, "wb") as f_out:
         f_out.write(requests.get(form_link).content)



# END SOLUTION

if __name__ == '__main__':

    grab_json_values()


