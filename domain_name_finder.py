import sys
def main():
    url = str(sys.argv[1])
    print(get_domain(url))


# find the domain name by removing the prefix and trailing text
def get_domain(url):
    # Checks for http protocols, removes them if found
    if url.find("http") != -1:
        url = remove_http(url)
    # if program finds www, call remove_www
    if url.find("www") != -1:
        url = remove_www(url)
    # call remove_tld to remove the top level domain, then return it to main
    return remove_TLD(url)


def remove_www(url):
    www_count = 0
    index = 0
    # check the url, when you find 3 w's, return the text after the 3 w's + 1 (the dot)
    for char in url:
        if char == "w":
            www_count += 1
        if www_count > 2:
            return url[index + 2:]

        index += 1


# find the dot (.), remove whatever's after it, then return the text
def remove_TLD(url):  # top level domain
    index = 0
    for char in url:
        if char == ".":
            return url[:index]

        index += 1


def remove_http(url):
    slash_count = 0
    index = 0
    for char in url:
        # search through url
        # when find 2 // in a row, remove everything before last index of /
        if char == "/":
            slash_count += 1
        if slash_count > 1:
            return url[index + 1:]
        index += 1


if __name__ == '__main__':
    main()
