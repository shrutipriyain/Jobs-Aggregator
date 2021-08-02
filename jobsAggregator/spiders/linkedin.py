# import scrapy
# import csv

# header = ["Job Profile", "Company", "Location", "Date Posted", "Apply here"]
# with open("Jobs Listed on LinkedIn.csv", 'w', encoding='UTF8') as file:
#     writer = csv.writer(file)
#     # write the header
#     writer.writerow(header)


# class LinkedinSpider(scrapy.Spider):
#     name = 'linkedin'
#     allowed_domains = ['www.linkedin.com']
#     start_urls = [
#         'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Software%2BDeveloper&location=India&trk=public_jobs_jobs-search-bar_search-submit&f_E=1&position=1&pageNum=0&start=0']
#     start_number = 25
#     custom_settings = {
#         "AUTOTHROTTLE_ENABLED": True
#     }

#     def parse(self, response):
#         job_cards = response.xpath("//div[@class='base-search-card__info']")
#         for job in job_cards:
#             Profile = job.xpath(
#                 "normalize-space(.//h3[@class='base-search-card__title']/text())").get()
#             Link = job.xpath(".//../@href").get()
#             Company = job.xpath("normalize-space(.//h4/a/text())").get()
#             if(Company is None):
#                 Company = job.xpath("normalize-space(.//h4/div/text())").get()
#             metaData = job.xpath(".//div[@class='base-search-card__metadata']")
#             Location = metaData.xpath(
#                 "normalize-space(.//span[@class='job-search-card__location']/text())").get()
#             Time = metaData.xpath("normalize-space(.//time/text())").get()
#             try:
#                 # yield{
#                 #     'Job Profile': Profile,
#                 #     'Company ': Company,
#                 #     'Job Location': Location,
#                 #     'Date Posted': Time,
#                 #     'Apply here ↗': Link
#                 # }
#                 dataRow = [Profile, Company, Location, Time, Link]
#                 with open("Jobs Listed on LinkedIn.csv", 'a', encoding='UTF8', newline="") as file:
#                     writer = csv.writer(file)
#                     writer.writerow(dataRow)
#             except Exception as e:
#                 print(str(e))
#             finally:
#                 next_page_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Software%2BDeveloper&location=India&trk=public_jobs_jobs-search-bar_search-submit&f_E=1&position=1&pageNum=0&start={self.start_number}'
#                 if(next_page_url):
#                     self.start_number += 25
#                     yield scrapy.Request(url=next_page_url, callback=self.parse)


import scrapy
import csv

header = ["Job Profile", "Company", "Location", "Date Posted", "Apply here"]
with open("Jobs Listed on LinkedIn.csv", 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    # write the header
    writer.writerow(header)


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['www.linkedin.com']
    start_urls = [
        'https://www.linkedin.com/jobs/search/?currentJobId=2622983319&f_TPR=r604800&geoId=104246759&keywords=internship&location=%C3%8Ele-de-France%2C+France&pageNum=0&start=0']
    start_number = 25
    custom_settings = {
        "AUTOTHROTTLE_ENABLED": True
    }

    def parse(self, response):
        job_cards = response.xpath("//div[@class='base-search-card__info']")
        for job in job_cards:
            Profile = job.xpath(
                "normalize-space(.//h3[@class='base-search-card__title']/text())").get()
            Link = job.xpath(".//../@href").get()
            Company = job.xpath("normalize-space(.//h4/a/text())").get()
            if(Company is None):
                Company = job.xpath("normalize-space(.//h4/div/text())").get()
            metaData = job.xpath(".//div[@class='base-search-card__metadata']")
            Location = metaData.xpath(
                "normalize-space(.//span[@class='job-search-card__location']/text())").get()
            Time = metaData.xpath("normalize-space(.//time/text())").get()
            try:
                # yield{
                #     'Job Profile': Profile,
                #     'Company ': Company,
                #     'Job Location': Location,
                #     'Date Posted': Time,
                #     'Apply here ↗': Link
                # }
                dataRow = [Profile, Company, Location, Time, Link]
                with open("Jobs Listed on LinkedIn.csv", 'a', encoding='UTF8', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(dataRow)
            except Exception as e:
                print(str(e))
            finally:
                next_page_url = f'https://www.linkedin.com/jobs/search/?currentJobId=2622983319&f_TPR=r604800&geoId=104246759&keywords=internship&location=%C3%8Ele-de-France%2C+France&pageNum=0&start={self.start_number}'
                if(next_page_url):
                    self.start_number += 25
                    yield scrapy.Request(url=next_page_url, callback=self.parse)
