from bs4 import BeautifulSoup
import requests
import openpyxl

response = requests.get('https://www.brightermonday.co.ke/jobs/software-data/nairobi').text
soup = BeautifulSoup(response, 'lxml')
jobs = soup.find_all('div', class_='flex flex-grow-0 flex-shrink-0 w-full')

# Create a list to store the job data
jobs_data = []

for job in jobs:
    # Extracting the title
    title_element = job.find('p', class_='text-lg font-medium break-words text-link-500')
    title = title_element.text.strip() if title_element else "N/A"

    # Extracting the company name
    company_element = job.find('a', class_='text-loading-animate-link')
    company = company_element.text.strip() if company_element else "N/A"

    # Extracting location
    location_element = job.find('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')
    location = location_element.text.strip() if location_element else "N/A"

    # Extracting job type
    job_type_elements = job.find_all('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')
    job_type = job_type_elements[1].text.strip() if len(job_type_elements) >= 2 else "N/A"

    # Extracting confidentiality
    confidentiality_element = job.find('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')
    confidentiality = confidentiality_element.text.strip() if confidentiality_element else "N/A"

    # Append the job data to the jobs_data list as a tuple
    jobs_data.append((title, company, location, job_type, confidentiality))


# Create a new workbook
workbook = openpyxl.Workbook()

# Access the active sheet (first sheet in the workbook)
sheet = workbook.active

# Set headers
headers = ['Title', 'Company', 'Location', 'Job Type', 'Salary']
sheet.append(headers)

# Write the data to the sheet
for job_data in jobs_data:
    sheet.append(job_data)

# Save the workbook to 'brighter_monday.xlsx'
file_path = 'brighter_monday.xlsx'
try:
    workbook.save(file_path)
    print("Data saved to:", file_path)
except Exception as e:
    print("Error saving data:", e)