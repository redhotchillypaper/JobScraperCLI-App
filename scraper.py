import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0/"


def main():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    job_cards = soup.find_all('a', class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]")

    sorted_job_cards = {}
    for job in job_cards:
        job_url = job.attrs['href']
        job_response = requests.get(job_url)
        job_soup = BeautifulSoup(job_response.text, 'html.parser')
        job_salary_response = job_soup.find('div', class_='salary compensation__salary')
        
        job_salary_data = None

        if job_salary_response == None:
            job_salary_data = "No info"
        else:
            job_salary_data = job_salary_response.text.strip()


        sorted_job_cards[f'{job.text.strip()}'] = [f'{job_url}',f'{job_salary_data}']
        



    # print(sorted_job_cards)
    pprint(sorted_job_cards)    




if __name__ == "__main__":
    main()
# <div class="compensation__salary-range">
#             <h3 class="compensation__heading">Base pay range</h3>

# <div class="compensation__salary-range">
#             <h3 class="compensation__heading">Base pay range</h3>
            
  
  
  
  
  
  
  
  

#     <div class="salary compensation__salary">
#       $90,000.00/yr - $120,000.00/yr
#     </div>
  
#           </div>

# attr:
# {'class': ['base-card__full-link', 'absolute', 'top-0', 'right-0', 'bottom-0', 'left-0', 'p-0', 'z-[2]', 'outline-offset-[4px]'], 
# 'href': 'https://www.linkedin.com/jobs/view/director-special-event-sales-at-san-diego-padres-4296944401?position=1&pageNum=0&refId=rhdSMe%2By6v5dSc7zBqWUaA%3D%3D&trackingId=vYTH42t9Zd78Q6H0ffvY0A%3D%3D', 
# 'data-tracking-control-name': 'public_jobs_jserp-result_search-card', 
# 'data-tracking-client-ingraph': '', 'data-tracking-will-navigate': ''}

# <a> class: # base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]