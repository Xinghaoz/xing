import re

# http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+MSFT&f=snabcc1p2kjwj6k5t8

def extract(item):
    with open("ori_" + item + ".txt", "r") as f:
        # print f.read()
        text = f.read()
        # print type(text), len(text), text
        stocks = re.findall("\\((.*?)\\)", text)
        string = ''
        for stock in stocks[:-1]:
             string += stock + "+"
        string += stocks[-1]
        with open("stocklist_" + item + ".txt", "w") as f2:
            f2.write(string)
            f2.write('\nhttp://download.finance.yahoo.com/d/quotes.csv?s=' +
                     string +
                     '&f=sabc1p2jkj6k5t8')


# with open("ori_finance.txt", "r") as f:
#     # print f.read()
#     text = f.read()
#     # print type(text), len(text), text
#     stocks = re.findall("\\((.*?)\\)", text)
#     string = ''
#     for stock in stocks[:-1]:
#          string += stock + "+"
#     string += stocks[-1]
#     print stocks[-1]
#     print string
#     print stocks[-1]

# with open("stocklist.txt", 'r') as f:
#     text = f.read()
#     # print type(text), text
#     string = ''
#     # print text.split("\n")
#     text = text.strip().split("\n")
#     for t in text:
#         string += t + "+"
#     string += text[-1]
#     print string

if __name__ == "__main__":
    extract('finance')
    extract('food')
    extract('tech')
    extract('car')
    extract('grocery')
    extract('etc')
