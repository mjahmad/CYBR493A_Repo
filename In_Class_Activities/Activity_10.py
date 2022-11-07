"""
Activity #10 solution
Get bug ids and bug packages from each page
"""
import string
import re

import HW3org
from In_Class_Practices import Web_Scraping as wb


def main():
    """
    Main screen for the web scrapping file
    :return:
    """

    link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist" \
           "=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED" \
           "&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field" \
           ".importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance" \
           "%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type" \
           "%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA" \
           "&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field" \
           ".structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field" \
           ".status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field" \
           ".affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field" \
           ".has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field" \
           ".has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby" \
           "=-importance&memo=75&start=0 "

    # Get tree
    # Extract and clean total number of bugs
    main_tree = wb.get_web_tree(link)
    noOfBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td/text()')[2]
    noOfBugs = [int(i) for i in noOfBugs.split() if i.isdigit()][0]


    noOfPages = (int(noOfBugs / 75))+1
    print("Total pages:   "+str(noOfPages))

    pageCounter= 0
    startCounter = 0
    newStart=""
    bug_pages_list=[]
    while pageCounter < noOfPages:
        startCounter= pageCounter * 75
        print("startCounter")
        print(startCounter)

        # Remove numbers at the end
        link = re.sub(r'\d+$', '', link)

        # combine page number with start string
        newStart=('&start='+str(startCounter))

        # combine page number with memo string
        memo='&memo='+str(startCounter)
        #print("newStart")
        #print(newStart)
        linkx = link.replace('&start=0',newStart)
        linkx = linkx.replace('&memo=75', memo)
        print(pageCounter)
        #print(linkx)
        bug_pages_list.append(linkx)
        pageCounter+=1
    print(bug_pages_list)



if __name__ == "__main__":
    main()
