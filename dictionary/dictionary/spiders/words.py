import scrapy

from dictionary.items import DictionaryItem

class WordsSpider(scrapy.Spider):
    name = "words"
    allowed_domains = ["dictionary.cambridge.org"]
    start_urls = ["https://dictionary.cambridge.org/vi/browse/english-vietnamese"]
    base_url = "https://dictionary.cambridge.org"

    def parse(self, response):
        original_url = "https://dictionary.cambridge.org/vi/browse/english-vietnamese/"

        if response.url != original_url:
            len_checker = len(response.url)

            if len_checker == (len(original_url) + 2):
                list_of_category = response.css('body > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > a')
                category_url = []
                for category in list_of_category:
                    category_url.append(category.css('a::attr(href)').get())
                for url in category_url:
                    yield scrapy.Request(url=url, callback=self.parse)

            elif len_checker > (len(original_url) + 2) and (response.url[len(response.url) - 1] == '/'):
                list_of_words = response.css('body > div:nth-of-type(2) > .pr > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(3) > div > div')
                word_urls = []
                for word in list_of_words :
                    next_page_url = self.base_url +  word.css('a::attr(href)').get()
                    word_urls.append(next_page_url)
                for url in word_urls:
                    yield scrapy.Request(url=url, callback=self.parse)
            else:
                Word = DictionaryItem()
                word_definitions = response.css("body > div:nth-of-type(2) > div > div > div:nth-of-type(2) > article > .entry-body > div > .link ")
                name = response.css(".link > div > div:nth-of-type(3) > h2::text").get()
                format_meaning = ""
                for definition in word_definitions:
                    type_of_word =  definition.css("div > div:nth-of-type(3) > span > div > span::text").get()
                    format_meaning += "- " + type_of_word + "\n"
                    meanings = definition.css("div > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > div:nth-of-type(3) > span")
                    for meaning in meanings:
                        meaning_text = meaning.css("span::text").get()
                        format_meaning += "+ " + meaning_text + "\n"
                
                Word['name'] = name
                Word['meaning'] = format_meaning
                yield Word
                
        else:
            list_of_alphabets = response.css("body > div:nth-of-type(2) .pr > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > ul > li")
            alphabet_url = []
            for alphabet in list_of_alphabets:
                alphabet_url.append(alphabet.css("a::attr(href)").get())
            for url in alphabet_url:
                yield scrapy.Request(url, callback=self.parse)
        
