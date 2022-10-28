"""
Activyt #8 solution
Get bug ids and bug packages from each page
"""

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
    main_tree = wb.get_web_tree(link)

    bug_list = main_tree.xpath('//*[@class="bugnumber"]//text()')
    # Get rid of # in each bug id, and return the clean list
    bug_list=  [ele.replace('#', '') for ele in bug_list]
    print(bug_list)
    bug_package = main_tree.xpath('//*[@class="buginfo-extra"]/span/text()')
    # cleanup package names and only include elements which are not empty.
    bug_package = [ele for ele in ([ele.strip() for ele in bug_package]) if ele != '']
    print(bug_package)


if __name__ == "__main__":
    main()
