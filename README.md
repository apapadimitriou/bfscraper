# bfscraper

---

The package scrapes Betfair price data (BSP, WAP etc) for Australian horse racing markets.

---

You can use the package in the following way:

```python
from bfscraper import bfscraper

df = bfscraper.scrape("2018-01-01", "2018-12-31")

print(df)
```

---

The above code would scrape the relevant data from January 1, 2018 till December 31, 2018.

There may be scope in the future to expand this package to other jurisdictions and racing codes.
