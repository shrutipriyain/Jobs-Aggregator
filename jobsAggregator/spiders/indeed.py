import scrapy
import csv

header = ["Job Title", "Company", "Location", "Apply here"]
with open("Jobs Listed on Indeed.csv", 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    # write the header
    writer.writerow(header)


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["in.indeed.com"]
    start_urls = ["https://in.indeed.com/software-developer-fresher-jobs"]
    start_index = 10  # will be used to crawl the next pages

    def parse(self, response):
        job_cards = response.xpath(
            "//div[contains(@class, 'jobsearch-SerpJobCard')]")
        for job_card in job_cards:
            title = job_card.xpath("normalize-space(.//h2/a/@title)").get()
            company = job_card.xpath(
                "normalize-space(.//div/div/span[@class='company']/text())").get()
            location = job_card.xpath(
                "normalize-space(.//div/span[contains(@class,'location')]/text())").get()

            apply = job_card.xpath(".//h2/a/@href").get()

            if(not title):
                title = "No Job Title Found"

            if(not company):
                company = "Company Not Specified"

            if(not location):  # to check if it exists or not
                location = "unspecified"
            if(apply is None):
                apply_here = "Couldn't find the link"
            else:
                apply_here = f"https://in.indeed.com{apply}"

                #     # yield{
                #     #     'title': title,
                #     #     'Company': company,
                #     #     'Location': location,
                #     #     'Apply here': apply_here
                #     # }
            if(title != "No Job Title Found" and company != "Company Not Specified" and location != "unspecified" and apply_here != "Couldn't find the link"):
                dataRow = [title, company, location, apply_here]
                # print(dataRow)
                with open('Jobs Listed on Indeed.csv', 'a', encoding='UTF8', newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(dataRow)
        print(f"Page {self.start_index/10} done! ")

        next_page = f"https://in.indeed.com/jobs?q=software+developer+fresher&start={self.start_index}"
        self.start_index += 10
        if(next_page):
            yield scrapy.Request(url=next_page, callback=self.parse)
