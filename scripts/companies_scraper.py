# 01.impoer libraries
import pandas as pd
import io
import time
import requests
import urllib
import sys

# 02.SET UP COMPANIES AND PERIOD
egx_companies_list = pd.read_csv(r"D:\My Projects\Python\EGX Scrapper\EGX-Scrapper\scripts\egx_companies.csv")

tadawul_companies_list = pd.read_csv(r"D:\My Projects\Python\EGX Scrapper\EGX-Scrapper\scripts\tadawul_companies.csv")
# add market column to filters data source
egx_companies_list["market"] = "EGX"
tadawul_companies_list["market"] = "Tadawul"

companies = pd.concat([egx_companies_list ,tadawul_companies_list] , ignore_index =True)
companies.to_csv("companies_master.csv", index=False)
