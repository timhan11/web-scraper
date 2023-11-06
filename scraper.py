import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()


#!Must replace URL with your website of choice
#!Will need to change the id and classes as they contain the information to scrape

#website ulr
URL = os.getenv("WEB_URL")

page = requests.get(URL)

#parse through
soup = BeautifulSoup(page.content, 'html.parser')

#find the results container id
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
#job elements are all where class is card-content

#python jobs is all h2 HTML elemtns with the text python
#lowercase as to ensure uppercase text is not excluded
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

#find parent of each h2 HTML
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#number of jobs is the length of python jobs found
numOfJobsFound = len(python_jobs)


#for each job in python job element set the links equal to each anchor tag
#for each link set the link url to the href of the HTML anchor tag

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")


print(f"Found {numOfJobsFound} jobs available")
#print(len(python_jobs))






