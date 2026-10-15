<a className="gh-badge" href="https://datahub.io/core/continent-codes"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Continent Codes

The seven continents with their English names and short, unique two-letter codes, in one CSV file.

Column definitions and types are in `datapackage.json`.

## Data

`data/continent-codes.csv` has 7 rows, one per continent:

| Column | Meaning |
|---|---|
| `Code` | Two-letter continent code, for example `EU`. Unique. The code for North America is `NA` |
| `Name` | English name of the continent, for example `Europe` |

### Known limitations

* "NA" is a code, not a missing value. The code for North America is the two letters `NA`. Many tools read the text `NA` as "missing" by default. For example, `pd.read_csv("data/continent-codes.csv")` returns an empty value (`NaN`) for North America. To keep it, read the file with `keep_default_na=False`:

  ```python
  import pandas as pd
  df = pd.read_csv("data/continent-codes.csv", keep_default_na=False)
  ```

  If you also want empty cells to count as missing, add `na_values=[""]`.
* The codes follow the lists in the sources below. One of them, the USGS list, calls the code `SA` "South and Central America". This file uses "South America", as the Wikipedia and PHP lists do.

## Data sources

The data is made by hand, according to several sources that use this kind of two-letter continent code. The 7 codes and 7 English names agree with the four sources below.

* [Country codes](https://www.geonames.org/countries/) from the GeoNames geographical database. Licence: CC BY, with credit asked ([terms](https://www.geonames.org/export/)). GeoNames does not state a version number.
* [Abbreviations](https://planetarynames.wr.usgs.gov/Abbreviations) from the International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN). The page is maintained by the U.S. Geological Survey (USGS) on behalf of the IAU. USGS says content it authored is in the U.S. public domain and asks for credit ([USGS copyright page](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)). The IAU's own terms for this list are unclear. None were found.
* [Wikipedia article](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_%28data_file%29#Data_file) from Wikipedia, the free encyclopedia. Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for its text. Only seven plain facts (the codes and names) were taken, and they also appear in the other sources. We judge that this does not make the dataset a copy or adaptation of the page. This is our judgement. Nobody has confirmed it legally.
* [PHP function](https://www.php.net/manual/en/function.geoip-continent-code-by-name.php) from the PHP manual. Licence: [Creative Commons Attribution 3.0 or later](https://www.php.net/manual/en/copyright.php). Credit is required.

Changes made to the source data: none. The file is made by hand according to the sources above, not produced by copying a file or table from them.

Not endorsed by, or affiliated with, GeoNames, the USGS, the IAU, Wikipedia or the PHP Group.

## Preparation

There is no script. The file is edited by hand. A GitHub workflow checks `datapackage.json` with `frictionless validate` on every push to `main` and on every pull request. It does not change the data.

To run the same check yourself:

```
pip install frictionless
frictionless validate datapackage.json
```

## License

The maintainers place their own work on this data package (the selection and the file) under the [Public Domain Dedication and License v1.0 (PDDL)](https://opendatacommons.org/licenses/pddl/1.0/). That covers no more than that. The PDDL does not change the terms of the sources, which differ:

* GeoNames: CC BY, credit asked.
* PHP manual: CC BY 3.0 or later, credit required.
* USGS/IAU page: USGS-authored content is U.S. public domain, credit requested. The IAU's own terms are unclear.
* Wikipedia: CC BY-SA 4.0 applies to its text and table. Only seven plain facts were taken. Our view that this does not trigger the share-alike term is a judgement, not confirmed legally.

The data is not claimed to be entirely public domain. The credits are in [ATTRIBUTION.txt](ATTRIBUTION.txt).
