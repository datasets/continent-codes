<a className="gh-badge" href="https://datahub.io/core/continent-codes"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

A list of the seven continents with English names and short, unique and permanent identifying codes.

## Data

Data provides list of continents with their two letter codes. The file `data/continent-codes.csv` has 7 rows and 2 columns: `Code` and `Name`.
Data is made manually, according to several sources from internet, that use this kind of format for continent two letter codes.
Several sources that use this format:

 - [Country codes](https://www.geonames.org/countries/) from The GeoNames geographical database.
 - [Abbreviations](https://planetarynames.wr.usgs.gov/Abbreviations) from International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)
 - [Wikipedia article](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_%28data_file%29#Data_file) from Wikipedia, the free encyclopedia
 - [PHP function](https://www.php.net/manual/en/function.geoip-continent-code-by-name.php) from PHP documentation.


### Note: "NA" is a code, not a missing value

The code for North America is the two letters `NA`. Many tools read the text `NA` as "missing" by default. For example, `pandas.read_csv("data/continent-codes.csv")` returns an empty value (`NaN`) for North America. To keep it, read the file with `keep_default_na=False` (and `na_values=[""]` if you also want empty cells to count as missing):

```python
import pandas as pd
df = pd.read_csv("data/continent-codes.csv", keep_default_na=False)
```

## License

This Data Package is made available under the Public Domain Dedication and License v1.0 whose full text can be found at: https://opendatacommons.org/licenses/pddl/1-0/