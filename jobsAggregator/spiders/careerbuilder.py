import scrapy
import csv


header = ["Job Profile", "Location", "Job Description", "Apply here"]
with open("Jobs Listed on CareerBuilder.csv", 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    # write the header
    writer.writerow(header)


class CareerbuilderSpider(scrapy.Spider):
    name = 'careerbuilder'
    allowed_domains = ['www.careerbuilder.co.in']
    start_urls = [
        'https://www.careerbuilder.co.in/jobsearch?pg=1&q=Software+developer+']
    page_number = 2

    def parse(self, response):
        jobs = response.xpath("//div[@class='job']")
        for job in jobs:
            job_title = job.xpath(
                "normalize-space(.//div/a[@class='job-title']/text())").get()
            apply_link = job.xpath(
                "normalize-space(.//div/a[@class='job-title']/@href)").get()
            apply_link = f"https://www.careerbuilder.co.in{apply_link}"
            location = job.xpath(
                "normalize-space(.//div/div[@class='snapshot']/a/text())").get()
            job_description = job.xpath("normalize-space(.//a/p/text())").get()
            # yield{
            #     'job': job_title,
            #     'apply': apply_link,
            #     'location': location,
            #     'description': job_description
            # }
            dataRow = [job_title, location, job_description, apply_link]
            with open("Jobs Listed on CareerBuilder.csv", 'a', encoding='UTF8', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(dataRow)
        print("Done with page number ", self.page_number)
        next_page_relative_url = response.xpath(
            "//a[@class='btn-arrow']/@href").get()
        if(next_page_relative_url):
            next_page_absolute_url = f"https://www.careerbuilder.co.in/jobsearch?pg={self.page_number}&q=Software+developer+"
            self.page_number += 1
            yield scrapy.Request(url=next_page_absolute_url, callback=self.parse)
