#!/bin/python
import twint
# Individually save csv files, TODO use userlist
c = twint.Config()
c.Username = "aoc"
c.Store_csv = True
c.Output = "aoc.csv"
c.Since = "2021-01-01"
c.Lang = "en"
twint.run.Search(c)

c = twint.Config()
c.Username = "benshapiro"
c.Store_csv = True
c.Output = "shapiro.csv"
c.Since = "2021-01-01"
c.Lang = "en"
twint.run.Search(c)

c = twint.Config()
c.Username = "tedcruz"
c.Store_csv = True
c.Output = "cruz.csv"
c.Since = "2021-01-01"
c.Lang = "en"
twint.run.Search(c)

c = twint.Config()
c.Username = "PeteButtigieg"
c.Store_csv = True
c.Output = "buttigieg.csv"
c.Since = "2021-01-01"
c.Lang = "en"
twint.run.Search(c)



