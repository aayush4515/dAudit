import os
from bs4 import BeautifulSoup
#import PyPDF2

# Function to extract GPA using the html file and BeautifulSoup object
def extract_gpa(soup):    #html_file stores the file path of the file
    # Find the table with the id 'SummaryTable'
        table = soup.find('table', id='SummaryTable')
        if table:
            # Find all the rows in the table
            rows = table.find_all('tr')
            for row in rows:
                # Check if the row contains the text 'Overall GPA:'
                if 'Overall GPA:' in row.get_text():
                    # Find all <td> elements in this r
                    tds = row.find_all('td')
                    if len(tds) > 2:
                        # Extract the GPA value from the second <td> tag
                        gpa_earned = tds[2].text.strip()
                        return gpa_earned

        return None

# Function to extract overall credits
def extract_credits(soup):
    table = soup.find('table', id='SummaryTable')
    if table:
         rows = table.find_all('tr')
         for row in rows:
              if 'Overall Credits' in row.get_text():
                   tds = row.find_all('td')
                   if len(tds) > 2:
                        credits_earned = tds[2].text.strip()
                        return credits_earned

    return None

# Function to extract IEJ status
def extract_iej_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')                       # Find all rows
          for row in rows:                                  # Iterate through all rows until the row with text 'A: IEJ' is found
               if 'A: IEJ' in row.get_text():               # When the text is found, find all <td> elements, (only one in this HTML file's case)
                    tds = row.find_all('td')
                    for td in tds:                          # Iterate through each <td> element
                         b_class = td.find('b')             # Find the <b> tag, because the status is enclosed inside the Bold tag
                         iej_status = b_class.text.strip()  # Extract the text enclosed inside the <b> tag
                         return iej_status
     return None

# Function to extract RSC status
def extract_rsc_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'B: RSC' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         rsc_status = b_class.text.strip()
                         return rsc_status
     return None

# Function to extract LT status
def extract_lt_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'C: LT' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         lt_status = b_class.text.strip()
                         return lt_status
     return None

# Function to extract FA status
def extract_fa_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'D: FA' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         fa_status = b_class.text.strip()
                         return fa_status
     return None

# Function to extract HA status
def extract_ha_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'E: HA' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         ha_status = b_class.text.strip()
                         return ha_status
     return None

# Function to extract SPA status
def extract_spa_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'F: SPA' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         spa_status = b_class.text.strip()
                         return spa_status
     return None

# Function to extract CBS status
def extract_cbs_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'G: CBS' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         cbs_status = b_class.text.strip()
                         return cbs_status
     return None

# Function to extract PS status
def extract_ps_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'H: PS' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         ps_status = b_class.text.strip()
                         return ps_status
     return None

# Function to extract LS status
def extract_ls_status(soup):
     table = soup.find('table', id='ReqTable')
     if table:
          rows = table.find_all('tr')
          for row in rows:
               if 'I: LS' in row.get_text():
                    tds = row.find_all('td')
                    for td in tds:
                         b_class = td.find('b')
                         ls_status = b_class.text.strip()
                         return ls_status
     return None

# Example usage
html_file = '/Users/aayush/Desktop/Projects/dAudit/example.html'

# Call the functions to extract data from HTML file
with open(html_file, 'r', encoding='utf-8') as file:    # opens the file as read-only and adds to the 'file' variable
    soup = BeautifulSoup(file, 'html.parser')       # creates a BeautifulSoup object names soup by parsing the content of HTML file

    # Call the function to extract the GPA
    overall_gpa = extract_gpa(soup)
    print(f"Overall GPA: {overall_gpa}")

    # Call the function to extract the credits
    credits_earned = extract_credits(soup)
    print(f"Overall Credits: {credits_earned}")

    # Call the function to extract IEJ status
    iej_status = extract_iej_status(soup)
    print(f"IEJ: {iej_status}")

    # Call the function to extract RSC status
    rsc_status = extract_rsc_status(soup)
    print(f"RSC: {rsc_status}")

    # Call the function to extract LT status
    lt_status = extract_lt_status(soup)
    print(f"LT: {lt_status}")

    # Call the function to extract FA status
    fa_status = extract_fa_status(soup)
    print(f"FA: {fa_status}")

    # Call the function to extract HA status
    ha_status = extract_ha_status(soup)
    print(f"HA: {ha_status}")

    # Call the function to extract HA status
    spa_status = extract_spa_status(soup)
    print(f"SPA: {spa_status}")

    # Call the function to extract HA status
    cbs_status = extract_cbs_status(soup)
    print(f"CBS: {cbs_status}")

    # Call the function to extract HA status
    ps_status = extract_ps_status(soup)
    print(f"PS: {ps_status}")

    # Call the function to extract HA status
    ls_status = extract_ls_status(soup)
    print(f"PS: {ls_status}")