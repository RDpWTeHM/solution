from scrapy import cmdline


def main():
    cmdline.execute("scrapy crawl httpbin".split())


if __name__ == "__main__":
    main()
