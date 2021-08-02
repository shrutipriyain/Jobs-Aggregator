import scrapy


class CoronaupdateSpider(scrapy.Spider):
    name = 'coronaupdate'  # spider name(same as the file name)
    allowed_domains = ['www.worldometers.info']
    # allowed domains should not contain the https protocol and the ending /

    start_urls = ['https://www.worldometers.info/coronavirus/']

    # start_urls must add https if not already present

    def parse(self, response):
        country_name = response.xpath("//a[@class='mt_a']")

        for country in country_name:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info/coronavirus/{link}"  #concatenated the relative link to get the absolute link

            # absolute_url = response.urljoin(
            #     link)  # better approach, the argument is the relative url
            # yield scrapy.Request(url=absolute_url)
            # #this allows us to follow the link

            # even better approach: response.follow follows using the relative url
            yield response.follow(
                url=link,  # tells us the link to follow
                callback=self.
                parse_country,  # tells where to send the reponse received
                meta={
                    'country_name': name
                }  # it is the meta deta we want to pass from the first parse method
                # it should be in the form of a dict
            )

    # to catch the response from the response.follow, we define another method
    def parse_country(self, response):
        # to catch the meta data from the parse method:
        name = response.request.meta['country_name']
        total = response.xpath(
            "(//div[@class='maincounter-number']/span)[1]/text()").get()
        death = response.xpath(
            "(//div[@class='maincounter-number']/span)[2]/text()").get()
        recovered = response.xpath(
            "(//div[@class='maincounter-number']/span)[3]/text()").get()

        with open("coronaCases.txt", 'a') as file:
            # opened in append mode so that data is not truncated
            file.write('country:%s\n' % (name))
            file.write('Total Cases:%s\n' % (total))
            file.write('Deceased:%s\n' % (death))
            file.write('Recovered:%s\n' % (recovered))
            file.write("\n")
        # print("Printing")
