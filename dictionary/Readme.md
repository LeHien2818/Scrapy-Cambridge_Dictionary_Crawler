# Cambridge dictionary crawling project

This project for learning and practicing purpose. Please don't use it for violating policy of any organization.


#  TECH STACK 

This project use Scrapy framework to crawl data from Cambridge website. Specifically, words and it's meanings in Vietnamese.

##  Getting started

Clone the project from this repository, and you need to install python to your machine first if you didn't do it before. Once you've done, run this command to sync all the dependencies inside the project
`source venv/bin/activate` (**For Linux**)
``venv\Scripts\activate`` (**For Window**)

After that, open the terminal and navigate to dictionary directory by using following command:
`cd dictionary`

Finally, you can start crawling data from Cambridge website by type this line in terminal:
`scrapy crawl books`
if you want to save the data in a file you can also use it command:
`scrapy crawl books -O <your_file_name>.csv`

### Note
Optional way to store the data: You can go to pipelines.py file to add any method to save your own data( PostgresSQL, MongoDB, MySQL, ...)

## Reference

The idea of this project came from this blog:
https://realpython.com/web-scraping-with-scrapy-and-mongodb/#prepare-the-scraper-scaffolding