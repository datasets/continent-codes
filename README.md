<a className="gh-badge" href="https://datahub.io/core/continent-codes"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

A list of the seven continents with English names and short, unique and permanent identifying codes.

## Data

Data provides list of continents with their two letter codes. The file `data/continent-codes.csv` has 7 rows and 2 columns: `Code` and `Name`.
Data is made manually. The 7 codes and 7 English names were typed by hand and checked against four sources. No file or table was copied from any of them.

Sources checked:

 - [Country codes](https://www.geonames.org/countries/) from The GeoNames geographical database. GeoNames says its data is under a CC BY licence and asks for credit ([terms](https://www.geonames.org/export/)). GeoNames does not state a version number.
 - [Abbreviations](https://planetarynames.wr.usgs.gov/Abbreviations) from the International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN). The page is maintained by the U.S. Geological Survey (USGS) on behalf of the IAU. USGS says content it authored is in the U.S. public domain and asks for credit ([USGS copyright page](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)). The IAU's own terms for this list: UNCLEAR. None were found.
 - [Wikipedia article](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_%28data_file%29#Data_file) from Wikipedia, the free encyclopedia. Wikipedia's text is under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Only seven plain facts (the codes and names) were taken, and they also appear in the other sources. We judge that this does not make the dataset a copy or adaptation of the page. This is our judgement. Nobody has confirmed it legally.
 - [PHP function](https://www.php.net/manual/en/function.geoip-continent-code-by-name.php) from the PHP manual. The manual says it is under [Creative Commons Attribution 3.0 or later](https://www.php.net/manual/en/copyright.php). Credit is required.

The USGS page calls the code SA "South and Central America". This dataset uses "South America", as the Wikipedia and PHP pages do.

Credit for the sources is in `ATTRIBUTION.txt`.

### Note: "NA" is a code, not a missing value

The code for North America is the two letters `NA`. Many tools read the text `NA` as "missing" by default. For example, `pandas.read_csv("data/continent-codes.csv")` returns an empty value (`NaN`) for North America. To keep it, read the file with `keep_default_na=False` (and `na_values=[""]` if you also want empty cells to count as missing):

```python
import pandas as pd
df = pd.read_csv("data/continent-codes.csv", keep_default_na=False)
```

## License

The maintainers place their own work on this data package under the Public Domain Dedication and License v1.0 (PDDL), whose full text is at https://opendatacommons.org/licenses/pddl/1.0/. That covers the maintainers' selection and the file, and no more than that.

The PDDL does not change the terms of the sources. The sources have different terms (see the list above):

 - GeoNames: CC BY, credit asked.
 - PHP manual: CC BY 3.0 or later, credit required.
 - USGS/IAU page: USGS-authored content is U.S. public domain, credit requested. The IAU's own terms are unclear.
 - Wikipedia: CC BY-SA 4.0 applies to its text and table. Only seven plain facts were taken. Our view that this does not trigger the share-alike term is a judgement, not confirmed legally.

The data is not claimed to be entirely public domain. The credits are in `ATTRIBUTION.txt`.
