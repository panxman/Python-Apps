## Example of creating Webmaps with the Folium package.

You first need to install the following packages for the python script to work:

1) pip install folium
2) pip install pandas

##### This is just a fast tutorial on how to use Folium with data from external files.

This application creates an html file that contains the World Map, different colors depending on the population of each country,
and some volcanoes that exist in the USA.

The population count is from **2005**.

### POPULATION COLORS:
- 0 - 9,999,999 ![#80ff80](https://placehold.it/15/80ff80/000000?text=+)
- 10,000,000 - 19,999,999 ![#00ff00](https://placehold.it/15/00ff00/000000?text=+)
- 20,000,000 - 49,999,999 ![#ffff66](https://placehold.it/15/ffff66/000000?text=+)
- 50,000,000 - 99,999,999 ![#ff9900](https://placehold.it/15/ff9900/000000?text=+) 
- 100,000,000+  ![#f03c15](https://placehold.it/15/f03c15/000000?text=+)

### VOLCANO COLORS depending on Elevation:
- 0 - 1999m ![#00ff00](https://placehold.it/15/00ff00/000000?text=+)
- 2000 - 2999m ![#ff9900](https://placehold.it/15/ff9900/000000?text=+)
- 3000m + ![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
