from In_Class_Practices import Web_Scraping as wb
import re
"""
Homework #3 objective is to fill out and complete each of the following methods.    
    """

def Generate_Links_For_All_Bugs_Pages(link):
    """
        20 POINTS
       A method which creates an entire list of URLs of all bug pages of the initial link
       :param link: link to the initial launchpad vulnerabilities (page one) passed from main
       :return: list of URLs, each to a page of bugs
    """
    # Empty list, add all urls to this list
    bug_pages_list = []

    # Each time you create a new link, store it in this variable
    current_link = ''

    # add the current link to the list
    bug_pages_list.append(current_link)

    return bug_pages_list


def GetBugIDs(page_link):
    """
    10 POINTS
        A method which iterates through the entire list of bug reports of any  given link
        :param link: link to launchpad bug report page passed from main
        :return: list of bug IDs of the page_link page
    """
    # Empty list, add all bug IDs to this list
    bug_list=[]

    return bug_list


def GetBugPackages(page_link):
    """
    20 POINTS
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: list of bug packages of the page_link page
    """
    # Empty list, add all bug packages to this list
    bug_package = []
    return bug_package


def GetTotalNumberOfBugs(page_link):
    """
    20 POINTS
        A method which gets extracts total number of bugs from the initial link of Ubuntu Vulnerabilities
        :param link: link to launchpad bug reports page
        :return: the total number of bugs from the first page
    """
    # Extract and clean total number of bugs

    noOfBugs = 0
    return noOfBugs


def GetTotalNumberOfPages(page_link):
    """
    20 POINTS
            A method which calculates the total number of bug pages from the initial link of Ubuntu Vulnerabilities
            :param link: link to launchpad bug reports page
            :return: the total number of bug pages
        """

    # Extract and clean total number of bugs
    GetTotalNumberOfBugs(page_link)
    noOfPages = 0
    return noOfPages
