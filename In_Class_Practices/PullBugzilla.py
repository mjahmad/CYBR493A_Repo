import Web_Scraping as wb


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://bugzilla.redhat.com/buglist.cgi?bug_status=__closed__&bug_status=CLOSED&classification=Red%20Hat&classification=Fedora&f1=short_desc&f2=alias&f3=longdesc&j_top=OR&limit=0&o1=anywordssubstr&o2=anywordssubstr&o3=anywordssubstr&order=priority%2Cbug_severity&product=Fedora&product=Red%20Hat%20Enterprise%20Linux%202.1&product=Red%20Hat%20Enterprise%20Linux%203&product=Red%20Hat%20Enterprise%20Linux%204&product=Red%20Hat%20Enterprise%20Linux%205&product=Red%20Hat%20Enterprise%20Linux%206&product=Red%20Hat%20Enterprise%20Linux%207&product=Red%20Hat%20Enterprise%20Linux%208&query_format=advanced&resolution=WONTFIX&resolution=DEFERRED&resolution=CURRENTRELEASE&resolution=RAWHIDE&resolution=ERRATA&resolution=UPSTREAM&resolution=NEXTRELEASE&short_desc=CVE-&short_desc_type=anywordssubstr&v1=CVE-&v2=CVE-&v3=CVE-")
    bug_list = main_tree.xpath('//table[@id="bz_buglist"]/tr')
    #bug_list = main_tree.xpath('/table/html/body/div[2]/div[3]/table/tbody')
    #print(str((bug_list)))

    for bug in bug_list:
        print(bug)
        bug_id = bug.xpath('./tr/td/a/text()')
        print("ID: ",bug_id)

if __name__ == "__main__":
    main()
