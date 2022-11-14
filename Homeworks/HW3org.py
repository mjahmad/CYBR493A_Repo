from In_Class_Practices import Web_Scraping as wb
import re


def Generate_Links_For_All_Bugs_Pages(link):
    """
       A method which creates an entire list of bug report URL pages of the initial link
       :param link: link to launchpad bug reports passed from main
       :return: list of URLs, each to a page
    """
    numberOfPages = GetTotalNumberOfBugs(link)
    noOfPages = (int(numberOfPages / 75)) + 1
    #print("Total pages:   " + str(noOfPages))

    pageCounter = 0
    startCounter = 0
    newStart = ""
    bug_pages_list = []
    while pageCounter < noOfPages:
        startCounter = pageCounter * 75
        #print("startCounter")
        #print(startCounter)

        # Remove numbers at the end
        link = re.sub(r'\d+$', '', link)

        # combine page number with start string
        newStart = ('&start=' + str(startCounter))

        # combine page number with memo string
        memo = '&memo=' + str(startCounter)
        # print("newStart")
        # print(newStart)
        linkx = link.replace('&start=0', newStart)
        linkx = linkx.replace('&memo=75', memo)
        #print(pageCounter)
        # print(linkx)
        bug_pages_list.append(linkx)
        pageCounter += 1
    return bug_pages_list


def GetBugIDs(page_link):
    """
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: N/A
    """
    main_tree = wb.get_web_tree(page_link)

    bug_list = main_tree.xpath('//*[@class="bugnumber"]//text()')
    # Get rid of # in each bug id, and return the clean list
    return [ele.replace('#', '') for ele in bug_list]


def GetBugPackages(page_link):
    """
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: N/A
    """
    main_tree = wb.get_web_tree(page_link)
    bug_package = main_tree.xpath('//*[@class="buginfo-extra"]/span/text()')
    # cleanup package names and only include elements which are not empty.
    bug_package = [ele for ele in ([ele.strip() for ele in bug_package]) if ele != '']
    return bug_package


def GetTotalNumberOfBugs(page_link):
    # Extract and clean total number of bugs
    main_tree = wb.get_web_tree(page_link)
    noOfBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td/text()')[2]
    noOfBugs = [int(i) for i in noOfBugs.split() if i.isdigit()][0]
    return noOfBugs


def GetTotalNumberOfPages(page_link):
    # Extract and clean total number of bugs
    main_tree = wb.get_web_tree(page_link)
    noOfBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td/text()')[2]
    noOfBugs = [int(i) for i in noOfBugs.split() if i.isdigit()][0]
    #print(noOfBugs)
    noOfPages = (int(noOfBugs / 75)) + 1
    return noOfPages
