from bs4 import BeautifulSoup
import requests
import time

def scrp() :



    htmltext = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+&txtLocation=').text
    soup = BeautifulSoup(htmltext,"lxml")
    jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")




    for index , job in enumerate(jobs) :
        skills = job.find("span",class_="srp-skills").text.replace(' ',"").strip().replace(","," ")
        name = job.find("h2").text.strip()
        datepost = job.find("span", class_="sim-posted").span.text
        cmp_name = job.header.a["href"]
        with open(f'C:\\Users\\youss\\OneDrive\\Documents\\{index}.txt','w') as f :
            f.write(f" skill : {skills} \n")
            f.write(f" name : {name} \n")
            f.write(f" da&tepost: {datepost} \n")
            f.write(f" more info: {cmp_name} \n")

if __name__ == '__main__':
    print('the program is runing')
    time.sleep(10)
    scrp()
    time.sleep(10)
    print("la fin")
