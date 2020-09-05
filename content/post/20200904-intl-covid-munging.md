---
layout:     post

title:      "Munging Global COVID stats"
date:       2020-09-04
author:     "Patrick Lam"
tags:       ["covid"]
categories: []
published:  true
showtoc:    false
markup:     mmark
image:      "/img/20200904-intl-covid-munging/coronavirus.jpg"

---

<a href="/post/20200408-nz-covid-munging/">Previously (NZ stats);</a> banner image from US CDC: <a href="https://phil.cdc.gov/Details.aspx?pid=23354">https://phil.cdc.gov/Details.aspx?pid=23354</a>.

It hasn't been discussed in either the Canadian or NZ news from what I
can see, but I'm vaguely aware that some countries are having a legit
resurgence. I understand that people who are more closely connected to
European countries have been talking about it more. Quebec is worrying
about one but the Canada-wide numbers are still better than many
European countries. Of course we should worry about what is going to
happen when schools are back.

A number of countries had controlled the pandemic for a while but had
new clusters come up, most notably Australia and particularly
Melbourne in Victoria state, which is still under a lockdown as I
write this. Auckland also had a couple of weeks of lockdown in New
Zealand. But I had the feeling that the numbers in New Zealand are way
smaller than elsewhere, and wanted to check that.

I started looking at data manually and then went programmatic, writing
some Python code to munge the ourworldindata.org data, helpfully
provided in <a href="https://covid.ourworldindata.org/data/owid-covid-data.json">JSON format</a>.

* Q: How does the number of new cases/day compare to peak?

I do not believe in
per-capita numbers for evaluating outbreak size; even in the United
States, I think the uninfected population is essentially infinite.  So
I claim that what matters is the absolute size of the outbreak. And
it's not going to generally be evenly-distributed across the whole
country, but rather in a couple of hotspots.  We saw, for instance,
how New York was a hotspot for the US, and how Quebec was a hotspot
for Canada. (I will agree that per-capita numbers in e.g. a city say
something about how likely it is to encounter a case in that city.
[Edit: A valid implication is that per-capita numbers in a city can serve
as an approximation of the risk level involved in being out and around
in that city; but I'll reiterate that I don't think that one should say
that X is doing better or worse than Y because its per-capita number
is lower or higher.])

So here are the results of my data munging.

{{< tableCovid "/assets/200904-intl-covid-munging/stats.csv" >}}

These are the countries that are somewhat on my radar; there are, of course,
many other countries. I don't know much about African and many Asian countries.

## Highly-controlled: essentially-zero and double-digits.

I've put five countries in the essentially-zero club: Mongolia,
Taiwan, Vietnam, New Zealand, and Bhutan.  NZ may be one of the few
countries that distinguishes community transmission from imported
cases; I don't think there are good worldwide stats about that. Gotta
read local news for details.  NZ's community-transmission number was 0
for 103 days. Vietnam almost as good.

Almost as good are some countries with double-digit numbers of new
cases.  One could have questions about early numbers from China but I
guess they're good now.  Looks like Singapore has controlled the dorm
outbreak.

## Hundreds

The next group is countries with new-cases in the triple digits. There are two
groups here: those that are well below their peak (Australia, Ireland, Sweden,
South Korea, Switzerland, Canada, and Japan), and those that are uncomfortably close
to their peak, or peaking (Greece, Czech Republic). The Czech Republic has a page
where they estimate R<sub>t</sub> and it has been close to 1 all summer, but not quite
under 1. So the number of new cases keeps on slowly increasing, from dozens (April-June)
to hundreds (July onwards).

## Thousands

I'd read about Israel really not doing well, and I'd looked at France's numbers.
In the thousands category, Germany, Italy and the UK are well below their historical peaks,
while Israel keeps on increasing (I've read multiple pieces about how it was controlled
and then got away), and France is at mid-thousands and near its peak.

## PS

(I had also made an observation that some countries had a trough&mdash;NZ's was close
to 0 for over 100 days&mdash;and then resurged, but I had no way of evaluating that.
I think the technical analysis of stocks people would have some tools
(although I don't believe in technical analysis itself). I did evaluate this
by eye and tried some calculations but didn't get anything satisfactory.)

## Code

{{< highlight python "linenos=inline" >}}
#!/usr/bin/python3

import json
import datetime
from dateutil.parser import parse

def lookup(C, data, csv):
    for country in data:
        if (data[country]["location"] == C):
            biggest_date = parse('2000-01-01')
            biggest_new_cases = 0
            biggest_new_cases_date = 0
            for days in data[country]["data"]:
                thisdate = parse(days['date'])
                if 'new_cases' in days:
                    if days['new_cases'] > biggest_new_cases:
                        biggest_new_cases_date = thisdate
                        biggest_new_cases = days['new_cases']
                if thisdate > biggest_date:
                    biggest_date = thisdate
                    if 'total_cases' in days:
                        total_cases = days['total_cases']
                    if 'new_cases_smoothed' in days:
                        new_cases_smoothed = days['new_cases_smoothed']
            ratio_today_over_peak = new_cases_smoothed / biggest_new_cases
            if csv:
                print ("\"{0}\",{1:%d}-{1:%b},{2:.0f},{3:.1f},{4:.0f},{5:%d}-{5:%b},{6:.2f}".format(C, biggest_date, total_cases,
                                                                                                    new_cases_smoothed, biggest_new_cases,
                                                                                                    biggest_new_cases_date,
                                                                                                    ratio_today_over_peak))
            else:
                print ("{0}".format(C))
                print ("date {0:%d}-{0:%b}, total cases {1:.0f}, new cases smoothed {2}".format(biggest_date, total_cases, new_cases_smoothed))
                print ("biggest new cases {0:.0f} on date {1:%d}-{1:%b}, today/biggest is {2:.2f}".format(biggest_new_cases, biggest_new_cases_date, ratio_today_over_peak))

countries = ["Mongolia", "New Zealand", "Vietnam", "Bhutan", "Taiwan", "Singapore",
	     "China", "Australia",  "Ireland", "Sweden", "South Korea", "Switzerland",
	     "Canada", "Japan", "Greece", "Czech Republic", "Germany", "Italy",
	     "United Kingdom", "Israel", "France", "United States"]

# https://covid.ourworldindata.org/data/owid-covid-data.json
with open ('owid-covid-data.json') as jsonfile:
    data = json.load(jsonfile)
    for C in countries:
        lookup(C, data, True)
{{< /highlight >}}