#JOB WEB SCRAPER
import time
from bs4 import BeautifulSoup
import requests

#gets location to filter from user
place=input("Is there anywhere you won't work? ").lower()

#scrapes webpage for needed info
def find_jobs():
    url=requests.get("https://jobs.seattletimes.com/search?keyword=python+software+engineering&location=Seattle%2C+WA&page=1&radius_mi=50&experience=").text
    soup=BeautifulSoup(url,"lxml")
    jobs=soup.find_all('h3',class_='job-title')
    for index, job in enumerate(jobs):
        info = soup.find('span', class_='item-location').text.strip()
        company = soup.find('a', class_='company-name').text.strip()
        link = soup.find('h3', class_='job-title').a['href']
        if place not in info.lower():
            with open(f"{index}.txt","w") as file:
                file.write(f"JOB: {job.text.strip()}\n")
                file.write(f"COMPANY: {company}\n")
                file.write(f"LOCATION: {info}\n")
                file.write(f"LINK: {link}")
                file.write("")

#runs program every ten minutes
if __name__=='__main__':
    while True:
        find_jobs()
        times=10
        time.sleep(60*times)