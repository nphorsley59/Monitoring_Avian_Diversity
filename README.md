# <div align="center">Monitoring Avian Diversity</div>

### <div align="center">Project Overview</div>
Skills Demonstrated: *data sourcing, data wrangling, data cleaning, lambda functions, data visualization*<br />
Libraries and Programs: *Python, Spyder, Tableau, numpy, pandas*<br />

In 2019, a colleague and I launched the Monitoring of Beneficial Birds in Agricultural Ecosystems Initiative. The purpose of this project is to connect sustainable land use practices with changes in native bird communities. As the sole analyst, I am responsible for transforming raw data into a format that can be quickly and easily communicated with landowners and funding agencies. For the Spring 2020 dataset, I used standard data wrangling, data cleaning, and data visualization techniques to create an interactive report.

### <div align="center">Data Wrangling</div>

Avian count data is collected and entered as 4-letter "Alpha" codes. While these codes are meaningful to ornithologists, they do a poor job of communicating study results to the general public. I decided I'd need to present full species names when reporting data for this project. I used Python to turn this table (Figure 1) published by The Institute for Bird Populations<sup>2</sup> into a Python dictionary (Figure 2). I then used the dictionary to connect 4-letter "Alpha" codes in my dataset to the full English species names.<br />

**Figure 1.** A small sample of the over 2,100 bird species that have been assigned 4-letter "Alpha" codes.<br />

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Bird_Species_Codes_Table1.png "Alpha Codes to English Names Table")<br />

**Figure 2.** The same sample after being transformed into a Python dictionary.<br />

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Bird_Species_Codes_Table2.png "Alpha Codes to English Names Dictionary")<br />

### <div align="center">Data Cleaning</div>

After establishing an "Alpha" codes reference dictionary, I began cleaning the Monitoring of Beneficial Birds in Agricultural Ecosystems Initiative dataset. I find data cleaning to be most effecient and thorough when divided into phases. For this project, I used the following approach:

#### Phase 1 - Identification
The first phase was to identify general problems with the dataset. I used .dtypes and a .value_counts() loop to create a fast summary of each column. I then used this summary to list out obvious tasks (Figure 3). While this was a good start, I had not addressed the possibility of NaNs in the dataset. To view NaNs, I used .isna().sum().sort_values(ascending=False) to view NaNs by column (Figure 4). Again, I listed out any obvious cleaning tasks.

**Figure 3.** An organized approach to cleaning data.<br /> 

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Data_Cleaning_Table1.png "Data Cleaning Tasks")<br />

**Figure 4.** A simple method for summarizing NaNs in a dataset.<br /> 

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Data_Cleaning_Table2.1.png "Table of NaNs by Column")<br />

#### Phase 2 - Cleaning
The second phase was to complete tasks identified in Phase 1. I used common indexing functions, such as .loc/iloc and .at/iat, to identify and address typos and other minor errors. More widespread problems were addressed using more powerful functions and techniques, such as .replace(), .fillna(), lambda functions, loops, and custom functions (Figure 5).

**Figure 5.** A loop used to move data that had been entered into the wrong column.<br />

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Data_Cleaning_Table3.png "Moving Data with a Loop")<br />

#### Phase 3 - Quality Assurance
The third phase was to repeat Phase 1 and, if necessary, Phase 2 to ensure nothing was missed in the initial cleaning process. In this particular project, I was unable to link English species names to the "Alpha" codes in my dataset until some obvious errors had been fixed i.e. until after Phases 1 and 2. However, after linking the English species names to the "Alpha" codes, it quickly became clear that errors existed in the "Alpha" codes column (Figure 6). These errors were difficult to catch in Phases 1 and 2 because they existed in a diverse categorical variable with no 'reference' set available for verification. I find this second round of cleaning, which I call "Quality Assurance", to be most useful in large or error-prone datasets.

**Figure 6.** Identifying rows with "Alpha" code (SpeciesCode column) errors.<br />

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Data_Cleaning_Table4.png "Alpha Code Errors")<br />

#### Phase 4 - Usability
The final phase was to increase the usability and readability of the dataset. A "clean" dataset that is difficult to understand/interpret is not very useful for analysis. For this dataset, I cleaned up uneccesary codes, renamed some columns, reordered the columns, and transformed some discrete data (e.g. StartTime) into continuous data. The final product was a clean, organized, easy-to-read dataset that was ready for analysis (Figure 7).

**Figure 7.** A cleaned sample from the Spring 2020 dataset.<br />

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/Data_Cleaning_Table5.1.png "Cleaned Dataset")<br />

### <div align="center">Visualization Using Tableau</div>

I used Tableau to visualize the results of our Spring 2020 surveys. I have included a sample plot below (Figure 8). The full workbook<sup>3</sup> can be found on Tableau Public.<br />

**Figure 8.** A bar chart showing prominent members of the bird community (>10 individuals) at each site.

![alt text](https://github.com/nphorsley59/Monitoring_Avian_Diversity/blob/master/Figures/BirdCbS_Sp2020_Table1.png "Bird Community by Site")<br />

### <div align="center">Resources</div>
<sup>1</sup> https://www.cowcreekorganics.com/about<br />
<sup>2</sup> https://www.birdpop.org/docs/misc/Alpha_codes_eng.pdf<br />
<sup>3</sup> https://public.tableau.com/profile/noah.horsley#!/<br />
