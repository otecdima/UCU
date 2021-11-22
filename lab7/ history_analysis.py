"""Lab7.4"""
def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> sites_on_date([('google1.com', 'GOOGLE1', "2021-09-09", '13:45:10:10', \
'2020')], "2021-09-09")
    {'google1.com'}
    """
    visitedurl1 = set()
    for site in visits:
        if date == site[2]:
            visitedurl1.add(site[0])
    return visitedurl1
# print(sites_on_date([('pornhub.com', 'PORNHUB', '2021-11-08', '07:27:16:09', 8765456),
# ('porn365.com', 'porn365','2021-11-86', '11:54:37:12', 87654),
# ('gitcum.com', 'gitcum', '2021-11-04', '12:31:41:25', 87654345),
# ('bilochkiporn365.com', 'porn365','2021-11-07', '11:54:37:12', 234569),
# ('bilochkiporn365.com', 'porn365','2021-11-05', '11:54:37:12', 9876543),
# ('porn365.com', 'porn365','2021-11-02', '11:54:37:12', 887654),
# ('gitcum.com', 'gitcum', '2021-11-02', '12:31:41:25', 434423),
# ('gitcum.com', 'gitcum', '2021-11-01','12:31:41:25', 28468)], "2021-11-02"))

def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> most_frequent_sites([('google1.com', 'GOOGLE1', "2021-09-09", '13:45:10:10', '2020')], 1)
    {'google1.com'}
    """
    try:
        siteslist = [site[0] for site in visits]
        newlist = []
        mylist = list(dict.fromkeys(siteslist))
        for item in mylist:
            numberofsites = siteslist.count(item)
            newlist.append((numberofsites, item))
        newlist.sort()
        newlist.reverse()
        new_set_of_sites = set()
        try:
            for item1 in range(number):
                new_set_of_sites.add(newlist[item1][1])
        except IndexError:
            return new_set_of_sites
        return new_set_of_sites
    except IndexError:
        return set()

print(most_frequent_sites([('pornhub.com', 'PORNHUB', '2021-11-08', '07:27:16:09', 8765456),
('porn365.com', 'porn365','2021-11-86', '11:54:37:12', 87654),
('gitcum.com', 'gitcum', '2021-11-04', '12:31:41:25', 87654345),
('bilochkiporn365.com', 'porn365','2021-11-07', '11:54:37:12', 234569),
('bilochkiporn365.com', 'porn365','2021-11-05', '11:54:37:12', 9876543),
('porn365.com', 'porn365','2021-11-03', '11:54:37:12', 887654),
('gitcum.com', 'gitcum', '2021-11-02', '12:31:41:25', 434423),
('gitcum.com', 'gitcum', '2021-11-01','12:31:41:25', 28468)], 3))

def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([('google12.com', 'GOOGLE12', "2021-09-09", \
'13:45:11.10', 2021)], "google12.com")
    ('GOOGLE12', '2021-09-09', '13:45:11.10', 1, 2021.0)
    """
    try:
        new_list = [item for item in visits if item[0] == url]
        len_of_new_list = len(new_list)
        list_for_dates_hours = []
        generalduration = 0
        if visits == [] and new_list == []:
            return ("", "", "", 0, 0)
        title = new_list[0][1]
        for item1 in new_list:
            date = item1[2]
            thetime = item1[3]
            list_for_dates_hours.append((date, thetime))
            the_duration = item1[4]
            generalduration = generalduration + the_duration
        maxofdatesandthetimes = max(list_for_dates_hours)
        thefinalduration = generalduration / len_of_new_list
        return (title, maxofdatesandthetimes[0], maxofdatesandthetimes[1], \
        len_of_new_list, thefinalduration)
    except IndexError:
        return ("", "", "", 0, 0)

# print(get_url_info([('url','topic','2022-1-11','2:15:36.66',97865), ('url','topic','2022-1-11','11:05:36.66',9876)], 'url1'))
# print(get_url_info([], 'url'))
