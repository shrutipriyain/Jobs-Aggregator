import scrapy
import csv

header = ["Job Title", "Company", "More Details"]
with open("Jobs Listed on Times Now.csv", 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    # write the header
    writer.writerow(header)


class TimesjobsSpider(scrapy.Spider):
    name = 'timesjobs'
    allowed_domains = ['www.timesjobs.com']
    start_urls = [
        'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=32'
    ]

    def parse(self, response):
        job = response.xpath("//h2/a")
        company = response.xpath(
            "//h3[@class='joblist-comp-name']/text()").getall()
        company = [x.strip() for x in company]

        # header = ["Job Title", "Company", "More Details"]
        # with open("Jobs Listed on Times Now.csv", 'a',
        #           encoding='UTF8') as file:
        #     writer = csv.writer(file)
        #     # write the header
        #     writer.writerow(header)
        i = 0
        for j in job:
            job_title = j.xpath(".//text()").get()
            job_title = job_title.strip()
            more_detail = j.xpath(".//@href").get()

            # yield {
            #     'job_title': job_title,
            #     'Company': company[i],
            #     'More_details': more_detail
            # }
            dataRow = [job_title, company[i], more_detail]
            # print(dataRow)
            i += 1
            with open('Jobs Listed on Times Now.csv', 'a',
                      encoding='UTF8', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(dataRow)
        print("Done! Check Your file")
