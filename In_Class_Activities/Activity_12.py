"""
Activity #12
"""
import HW3
# import the necessary files
from In_Class_Practices import Web_Scraping as wb
from Homeworks import HW3org

# Global variables, accessed by all method in this file
link = link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist" \
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


def GetBugTitles(page_link):
    """
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: N/A
    """
    main_tree = wb.get_web_tree(page_link)

    bug_list = main_tree.xpath('//*[@class="bugtitle"]//text()')
    # Get rid of # in each bug id, and return the clean list
    return [ele.replace('#', '') for ele in bug_list]



def main():
    """
    Main screen for HW #3.
    :return:N/A
    """
    # Display initial info
    bugsTotal = GetBugIDs(link)
    BugPackages = GetBugPackages(link)
    bugTitles = GetBugTitles(link)
    print('ID of all  Bugs:\t', bugsTotal)
    print('Packages of all  Bugs:\t', BugPackages)
    print('Titles of all  Bugs:\t', bugTitles)
    print(str(len(bugTitles)))



if __name__ == "__main__":
    main()
