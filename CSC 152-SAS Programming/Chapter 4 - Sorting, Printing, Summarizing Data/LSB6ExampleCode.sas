***1.1***;

* Convert miles to kilometers;
DATA distance;
   Miles = 26.22;
   Kilometers = 1.61 * Miles;
RUN; 
PROC PRINT  DATA = distance; /* Print the results */  
RUN;

***1.6***;

* Create a SAS data set named distance;
* Convert miles to kilometers;
DATA distance;
   Miles = 26.22;
   Kilometers = 1.61 * Miles;
RUN;
* Print the results;
PROC PRINT DATA = distance;
RUN;

***2.2***;

DATA distance; 
   Miles = 26.22;
   Kilometers = 1.61 * Miles;
RUN;

DATA '~/sasuser.v94/MySASLibdistance'; 
   Miles = 26.22;
   Kilometers = 1.61 * Miles;
RUN;

LIBNAME marathon '~/sasuser.v94/MySASLib'; 
DATA marathon.distance; 
   Miles = 26.22;
   Kilometers = 1.61 * Miles;
RUN;

***2.3***;

* Use PROC CONTENTS to describe the CARS data set in the SASHELP library;
PROC CONTENTS DATA = SASHELP.CARS;
RUN;

***2.4***;

LIBNAME sasfiles '~/sasuser.v94/MySASLib';
* Read an Excel spreadsheet using PROC IMPORT;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyExcel/Trees.xlsx' OUT = sasfiles.magnolia
   DBMS = XLSX REPLACE;
RUN;

***2.5***;

* Read an Excel spreadsheet using XLSX LIBNAME;
LIBNAME exfiles XLSX '~/sasuser.v94/MyExcel/Trees.xlsx';
PROC PRINT DATA = exfiles.sheet1;
   TITLE 'PROC PRINT of Excel File';
RUN;

* Read Excel into a permanent SAS data set;
LIBNAME exfiles XLSX '~/sasuser.v94/MyExcel/Trees.xlsx';
LIBNAME sasfiles '~/sasuser.v94/MySASLib';
DATA sasfiles.magnolia;
   SET exfiles.sheet1;
RUN;

***2.6***;

PROC IMPORT DATAFILE ='~/sasuser.v94/MyRawData/Bands2.csv' OUT = music REPLACE;
RUN;

***2.7***;

* Read internal data into SAS data set uspresidents;
DATA uspresidents;
   INPUT President $ Party $ Number;
   DATALINES;
Adams F 2
Lincoln R 16
Grant R 18
Kennedy D 35
   ;
RUN;

* Read data from external file into SAS data set;
DATA uspresidents;
   INFILE '~/sasuser.v94/MyRawData/President.dat';
   INPUT President $ Party $ Number;
RUN;

***2.8***;

* Create a SAS data set named toads;
* Read the data file ToadJump.dat using list input;
DATA toads;
   LENGTH ToadName $ 9;
   INFILE '~/sasuser.v94/MyRawData/ToadJump.dat';
   INPUT ToadName Weight Jump1 Jump2 Jump3;
RUN;

***2.9***;

* Create a SAS data set named sales;
* Read the data file OnionRing.dat using column input;
DATA sales;
   INFILE '~/sasuser.v94/MyRawData/OnionRing.dat';
   INPUT VisitingTeam $ 1-20 CSales 21-24 BSales 25-28
         OurHits 29-31 TheirHits 32-34 OurRuns 35-37 TheirRuns 38-40;
RUN;

***2.10***;

LIBNAME pump '~/sasuser.v94/MySASLib';
* Create a permanent SAS data set named contest;
* Read the file Pumpkin.dat using formatted input;
DATA pump.contest;
   INFILE '~/sasuser.v94/MyRawData/Pumpkin.dat';
   INPUT Name $16. Age 3. +1 Type $1. +1 Date MMDDYY10.
         (Score1 Score2 Score3) (4.1);
RUN;

***2.12***;

* Create a SAS data set named nationalparks;
* Read a data file NatPark.dat mixing input styles;
DATA nationalparks;
   INFILE '~/sasuser.v94/MyRawData/NatPark.dat';
   INPUT ParkName $ 1-22 State $ Year @40 Acreage COMMA9.;
RUN;

***2.13***;

DATA canoeresults;
  INFILE '~/sasuser.v94/MyRawData/Canoes.dat';
  INPUT CanoeName & $13. @'School' School $ @'Time' RaceTime :STIMER8.;
RUN;

***2.14***;

* Create a SAS data set named highlow;
* Read the data file using line pointers;
DATA highlow;
   INFILE '~/sasuser.v94/MyRawData/Temperature.dat';
   INPUT City $ State $ 
         / NormalHigh NormalLow
         #3 RecordHigh RecordLow;
RUN;

***2.15***;

* Input more than one observation from each record;
DATA rainfall;
   INFILE '~/sasuser.v94/MyRawData/Precipitation.dat';
   INPUT City $ State $ NormalRain MeanDaysRain @@;
RUN;

***2.16***;

* Use a trailing @, then delete surface streets;
DATA freeways;
   INFILE '~/sasuser.v94/MyRawData/Traffic.dat';
   INPUT Type $ @;
   IF Type = 'surface' THEN DELETE;
   INPUT Name $ 9-38 AMTraffic PMTraffic;
RUN;

***2.17***;

DATA icecream;
   INFILE '~/sasuser.v94/MyRawData/IceCreamSales.dat' FIRSTOBS = 3;
   INPUT Flavor $ 1-9 Location BoxesSold;
RUN;

DATA icecream;
   INFILE '~/sasuser.v94/MyRawData/IceCreamSales2.dat' FIRSTOBS = 3 OBS=5;
   INPUT Flavor $ 1-9 Location BoxesSold;
RUN;

DATA class102;
   INFILE '~/sasuser.v94/MyRawData/AllScores.dat' MISSOVER;
   INPUT Name $ Test1 Test2 Test3 Test4 Test5;
RUN; 

DATA homeaddress;
   INFILE '~/sasuser.v94/MyRawData/Address.dat' TRUNCOVER;
   INPUT Name $ 1-15 Number 16-19 Street $ 22-37;
RUN;


***3.1***;

LIBNAME hotels '~/sasuser.v94/MySASLib';
DATA hotels.kyotohotels;
  INFILE '~/sasuser.v94/MyRawData/KyotoHotels.dat';
  INPUT Hotel $ 1-25 Yen Kilometers;
  USD = Yen * 0.0089;
RUN;

LIBNAME hotels '~/sasuser.v94/MySASLib';
DATA hotels;
  SET hotels.kyotohotels;
  Miles = Kilometers * 0.62;
RUN; 

***3.2***;

* Read csv file with PROC IMPORT;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Garden.csv' OUT = homegarden REPLACE;
RUN;
* Modify homegarden data set with assignment statements;
DATA homegarden;
   SET homegarden;
   Zone = 14;
   Type = 'home';
   Zucchini = Zucchini * 10;
   Total = Tomato + Zucchini + Peas + Grapes;
   PerTom = (Tomato / Total) * 100;
RUN;

***3.3***;

LIBNAME pump '~/sasuser.v94/MySASLib';
*Use SAS functions to create and modify variables;
DATA pumpkin;
   SET pump.contest;
   AvgScore = MEAN(Score1, Score2, Score3);
   DayEntered = DAY(Date);
   Type = UPCASE(Type);
RUN;

***3.6***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Auction.txt' OUT = oldcars REPLACE;
RUN;
*Use IF-THEN statements to create and modify variables;
DATA oldcars;
   SET oldcars;
   IF YearMade < 1890 THEN Veteran = 'Yes';
   IF Model = 'F-88' THEN DO;
      Make = 'Oldsmobile';
      Seats = 2;
   END;
RUN;

***3.7***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Home.txt' OUT = homeimp REPLACE;
RUN;
DATA homeimprovements;
   SET homeimp;
   *Group observations by cost;
   LENGTH CostGroup $6;
   IF Cost = . THEN CostGroup = 'TBD';
      ELSE IF Cost < 2000 THEN CostGroup = 'low';
      ELSE IF Cost < 10000 THEN CostGroup = 'medium';
      ELSE CostGroup = 'high';
RUN;

***3.8***;

LIBNAME feed'~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Zoo.csv' OUT = feed.zoo REPLACE;
RUN;
*Choose only mammals;
DATA mammals;
   SET feed.zoo;
   IF Class = 'Mammalia';
   IF Enclosure =: 'E' THEN Area = 'East';
     ELSE IF Enclosure =: 'W' THEN Area = 'West';
RUN;

***3.9***;

LIBNAME feed'~/sasuser.v94/MySASLib';
*Choose only mammals;
PROC SQL;
   CREATE TABLE mammals AS
     SELECT *
     FROM feed.zoo
     WHERE Class = 'Mammalia';
QUIT;

***3.10***;

LIBNAME feed'~/sasuser.v94/MySASLib';
*Create data sets for morning and afternoon feedings;
DATA morning afternoon;
   SET feed.zoo;
   IF FeedTime = 'am' THEN OUTPUT morning;
      ELSE IF FeedTime = 'pm' THEN OUTPUT afternoon;
      ELSE IF FeedTime = 'both' THEN OUTPUT;
RUN;

***3.11***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Schedule.csv' OUT = GameDates
            REPLACE;
RUN;
DATA Games;
  SET GameDates;
  *If a double header, output twice;
  IF Type = 'D' THEN DO;
    OUTPUT;
    OUTPUT;
  END;
  *Else if not a double header output only once;
  ELSE OUTPUT;
RUN; 

* Create three observations for each data line read
*   using three OUTPUT statements;
DATA theaters;
   INFILE '~/sasuser.v94/MyRawData/Movies.dat';
   INPUT Month $ Location $ Tickets @;
   OUTPUT;
   INPUT Location $ Tickets @;
   OUTPUT;
   INPUT Location $ Tickets;
   OUTPUT;
RUN;

***3.12***;

DATA numyears;
   DO InterestRate = 0.02 TO 0.06 BY 0.01;
     *Initialize Savings and Year for each interest rate;
     Savings = 100;
     Years = 0;

     *Find number of years until savings greater than $1000;
     DO UNTIL (Savings > 1000);
        Years = Years + 1;
        Savings = Savings + (InterestRate * Savings);
     END;

     *Write results to years data set;
     OUTPUT;
   END;
RUN;

***3.13***;

DATA librarycards;
   INFILE '~/sasuser.v94/MyRawData/Library.dat' TRUNCOVER;
   INPUT Name $11. + 1 BirthDate MMDDYY10. +1 IssueDate ANYDTDTE10.
      DueDate DATE11.;
   DaysOverDue = TODAY() - DueDate;
   CurrentAge = INT(YRDIF(BirthDate, TODAY(), 'AGE'));
   IF IssueDate > '01JAN2020'D THEN NewCard = 'yes';
RUN;
PROC PRINT DATA = librarycards;
   FORMAT Issuedate MMDDYY8. DueDate WEEKDATE17.;
   TITLE 'SAS Dates without and with Formats';
RUN;

***3.15***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Games.txt' OUT = gamestats REPLACE;
RUN;
* Using RETAIN and sum statements to find most runs and total runs;
DATA gamestats;
   SET gamestats;
   RETAIN MaxRuns;
   MaxRuns = MAX(MaxRuns, Runs);
   RunsToDate + Runs;
RUN;

***3.16***;

* Create a permanent SAS data set;
LIBNAME radio '~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/KBRK.csv' OUT = radio.songs REPLACE;
RUN;

* Change all 9s to missing values;
DATA fixsongs;
   SET radio.songs;
   ARRAY song (5) wj kt tr filp ttr;
   DO i = 1 TO 5;
      IF song(i) = 9 THEN song(i) = .;
   END;
RUN;

***3.17***;

LIBNAME radio '~/sasuser.v94/MySASLib';
DATA fixsongs;
   SET radio.songs;
   ARRAY new (5) Song1 - Song5;
   ARRAY old (5) wj -- ttr;
   DO i = 1 TO 5;
      IF old(i) = 9 THEN new(i) = .;
         ELSE new(i) = old(i);
   END;
   AvgScore = MEAN(OF Song1 - Song5);
RUN;

***3.18***;

*Read data using ANY rules for variable names;
OPTIONS VALIDVARNAME = ANY;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/CampEquip.txt'  
     OUT = campequipment_any REPLACE;
RUN;
DATA campequipment_any;
   SET campequipment_any;
   IF 'Country of Origin'N = 'USA';
   PriceDiff = 'Store$'N - 'Online$'N;
RUN;

*Read data using V7 rules for variable names;
OPTIONS VALIDVARNAME = V7;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/CampEquip.txt'  
     OUT = CampEquipment_V7 REPLACE;
RUN;
DATA CampEquipment_V7;
   SET CampEquipment_V7;
   IF Country_of_Origin = 'USA';
   PriceDiff = Store_ - Online_;
RUN;

***4.2***;

* Import CSV file of artists;
LIBNAME art '~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Artists.csv' OUT = art.style REPLACE;
RUN;
* Print list of Impressionist painters;
PROC PRINT DATA = art.style;
   WHERE Genre = 'Impressionism';
   TITLE 'Impressionist Painters';
   FOOTNOTE 'F = France U = USA';
RUN;


***4.3***;

DATA marine;
   INFILE '~/sasuser.v94/MyRawData/Lengths.dat';
   INPUT Name $ Family $ Length @@;
RUN;
* Sort the data and remove duplicates;
PROC SORT DATA = marine OUT = seasort NODUPKEY;
   BY Family Name;
RUN;
* Print the sorted data;
PROC PRINT DATA = seasort;
   TITLE 'Whales and Sharks';
RUN;

***4.4***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Mail.txt' OUT = addresses REPLACE;
RUN;
* Sort addresses using linguistic sorting with numeric collation;
PROC SORT DATA = addresses OUT = sortout 
      SORTSEQ = LINGUISTIC (STRENGTH = PRIMARY NUMERIC_COLLATION = ON);
   BY State City Street;
RUN;
* Print the liguistically sorted data;
PROC PRINT DATA = sortout;
   TITLE 'Addresses Sorted by State, City, and Street';
RUN;

***4.5***;

LIBNAME class '~/sasuser.v94/MySASLib';
DATA class.sales;
   INFILE '~/sasuser.v94/MyRawData/CookieSales.dat';
   INPUT Name $ Class DateReturned MMDDYY10. CookieType $ Quantity @@;
   Profit = Quantity * 2.5;
RUN;
PROC SORT DATA = class.sales OUT = salessort;
   BY Class;
RUN;
PROC PRINT DATA = salessort;
   BY Class;
   SUM Profit;
   VAR Name DateReturned CookieType Profit;
   TITLE 'Cookie Sales for Field Trip by Class';
RUN;

***4.6***;

LIBNAME class '~/sasuser.v94/MySASLib';
* Print cookie sales data with formatted values;
PROC PRINT DATA = class.sales;
   VAR Name DateReturned CookieType Profit;
   FORMAT DateReturned DATE9. Profit DOLLAR6.2;
   TITLE 'Cookie Sale Data Using Formats';
RUN;

***4.8***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Cars.csv' OUT = carsurvey REPLACE;
RUN;
PROC FORMAT;
   VALUE gender 1 = 'Male'
                2 = 'Female';
   VALUE agegroup 13 -< 20 = 'Teen'
                  20 -< 65 = 'Adult'
                  65 - HIGH = 'Senior';
   VALUE $col  'W' = 'Moon White'
               'B' = 'Sky Blue'
               'Y' = 'Sunburst Yellow'
               'G' = 'Rain Cloud Gray';
RUN;
* Print data using user-defined and standard formats;
PROC PRINT DATA = carsurvey;
   FORMAT Sex gender. Age agegroup. Color $col. Income DOLLAR8.;
   TITLE 'Survey Results Printed with User-Defined Formats';
RUN;

***4.9***;

* Write a report with FILE and PUT statements;
LIBNAME class '~/sasuser.v94/MySASLib';
DATA _NULL_;
   SET class.sales;
   FILE 'c:\MyTextFiles\Student.txt' PRINT;
   TITLE;
   PUT @5 'Cookie sales report for ' Name 'from classroom ' Class
     // @5 'Congratulations!  You sold ' Quantity 'boxes of cookies'
     / @5 'and earned ' Profit DOLLAR6.2 ' for our field trip.';
   PUT _PAGE_;
RUN;

***4.10***;

LIBNAME garden '~/sasuser.v94/MySASLib';
DATA garden.plants;
    INFILE '~/sasuser.v94/MyRawData/Flowers.dat';
    INPUT CustID $ @9 SaleDate MMDDYY10. Petunia SnapDragon Marigold;
    Month = MONTH(SaleDate);
    FORMAT SaleDate MMDDYY10;
RUN;
* Calculate means by Month for flower sales;
PROC MEANS DATA = garden.plants MAXDEC = 0;
    CLASS Month;
    VAR Petunia SnapDragon Marigold;
    TITLE 'Summary of Flower Sales by Month';
RUN;

***4.11***;

LIBNAME garden '~/sasuser.v94/MySASLib';
* Calculate means by CustID, output sum and max to new data set;
PROC MEANS NOPRINT DATA = garden.plants;
   CLASS CustID;
   VAR Petunia SnapDragon Marigold;
   OUTPUT OUT = totals  
      MAX(Petunia SnapDragon Marigold) = MaxP MaxS MaxM
      SUM(Petunia SnapDragon Marigold) = Petunia SnapDragon Marigold;
RUN;

***4.12***;

LIBNAME drinks '~/sasuser.v94/MySASLib';
DATA drinks.orders;
   INFILE '~/sasuser.v94/MyRawData/Coffee.dat';
   INPUT Coffee $ Window $ @@;
RUN;
* Print tables for Window and Coffee;
PROC FREQ DATA = drinks.orders;
   TABLES Window Coffee;
   TITLE 'Coffee Sales by Window and by Type of Drink';
RUN;

***4.13***;

LIBNAME drinks '~/sasuser.v94/MySASLib';
* Print two tables for Window by Coffee;
PROC FREQ DATA = drinks.orders;
   TABLES Window * Coffee;
   TABLES Window * Coffee /  MISSING NOPERCENT NOCOL NOROW;
   TITLE 'Coffee Sales by Window and Type of Drink';
RUN;

***4.14***;

*Define formats to group the data;
PROC FORMAT;
   VALUE $typ
        'bio','non','ref' = 'Non-Fiction'
        'fic','mys','sci' = 'Fiction';
   VALUE agegpa
         0-18    = '0 to 18'
         19-25   = '19 to 25'
         26-49   = '26 to 49'
         50-HIGH = '  50+ ';
   VALUE agegpb
         0-25    = '0 to 25'
         26-HIGH = '  26+ ';
RUN;
DATA books;
   INFILE '~/sasuser.v94/MyRawData/LibraryBooks.dat';
   INPUT Age Book $ @@;
   BookType = PUT(Book,$typ.);
RUN;
*Create two way table with Age grouped into four categories;
PROC FREQ DATA = books;
   TITLE 'Patron Age by Book Type: Four Age Groups';
   TABLES BookType * Age / NOPERCENT NOROW NOCOL;
   FORMAT Age agegpa.;
RUN;
*Create two way table with Age grouped into two categories;
PROC FREQ DATA = books;
   TITLE 'Patron Age by Book Type: Two Age Groups';
   TABLES BookType * Age / NOPERCENT NOROW NOCOL;
   FORMAT Age agegpb.;
RUN;

***4.15***;

LIBNAME trips '~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Boats.txt' OUT = trips.boats REPLACE;
RUN;
* Tabulations with three dimensions;
PROC TABULATE DATA = trips.boats;
   CLASS Port Type Vessel;
   TABLE Port, Type, Vessel;
   TITLE 'Number of Boats by Port, Type, and Vessel';
RUN;

***4.16***;

LIBNAME trips '~/sasuser.v94/MySASLib';
* Tabulations with two dimensions and statistics;
PROC TABULATE DATA = trips.boats;
   CLASS Type Vessel;
   VAR Price;
   TABLE Type ALL, MEAN*Price*(Vessel ALL);
   TITLE 'Mean Price by Type and Vessel';
RUN;

***4.17***;

LIBNAME trips '~/sasuser.v94/MySASLib';
* PROC TABULATE report with options;
PROC TABULATE DATA = trips.boats FORMAT = DOLLAR7.2;
   CLASS Type Vessel;
   VAR Price Length;
   TABLE Type ALL, 
         MEAN * (Price Length*FORMAT=2.0) * (Vessel ALL)
         /BOX='Full Day Excursions' MISSTEXT='none';
   TITLE;
RUN;

***4.18***;
LIBNAME trips '~/sasuser.v94/MySASLib';
* Changing headers;
PROC FORMAT;
   VALUE $ves  'cat' = 'catamaran'
               'sch' = 'schooner'
               'yac' = 'yacht';
RUN;
PROC TABULATE DATA = trips.boats FORMAT=DOLLAR7.2;
   CLASS Type Vessel;
   VAR Price;
   FORMAT Vessel $ves.;
   TABLE Type='' ALL, 
      MEAN=''*Price='Mean Price by Kind of Vessel'*(Vessel='' ALL)
      /BOX='Full Day Excursions' MISSTEXT='none';
   TITLE;
RUN;

***4.19***;

LIBNAME visit '~/sasuser.v94/MySASLib';
DATA visit.natparks;
   INFILE '~/sasuser.v94/MyRawData/Parks.dat';
   INPUT Name $ 1-21 Type $ Region $ Museums Camping;
RUN;
PROC REPORT DATA = visit.natparks;
   TITLE 'Report with Character and Numeric Variables';
RUN;
PROC REPORT DATA = visit.natparks;
   COLUMN Museums Camping;
   TITLE 'Report with Only Numeric Variables';
RUN;

***4.20***;

LIBNAME visit '~/sasuser.v94/MySASLib';
* PROC REPORT with ORDER variable, MISSING option, and column header;
PROC REPORT DATA = visit.natparks MISSING;
   COLUMN Region Name Museums Camping;
   DEFINE Region / ORDER;
   DEFINE Camping / ANALYSIS 'Campgrounds';
   TITLE 'National Parks and Monuments Arranged by Region';
RUN;

***4.21***;

LIBNAME visit '~/sasuser.v94/MySASLib';
* Region and Type as GROUP variables;
PROC REPORT DATA = visit.natparks;
   COLUMN Region Type Museums Camping;
   DEFINE Region / GROUP;
   DEFINE Type / GROUP;
   TITLE 'Summary Report with Two Group Variables';
RUN;
* Region as GROUP and Type as ACROSS with sums;
PROC REPORT DATA = visit.natparks;
   COLUMN Region Type,(Museums Camping);
   DEFINE Region / GROUP;
   DEFINE Type / ACROSS;
   TITLE 'Summary Report with a Group and an Across Variable';
RUN;

***4.22***;

LIBNAME visit '~/sasuser.v94/MySASLib';
* PROC REPORT with breaks;
PROC REPORT DATA = visit.natparks;
   COLUMN Name Region Museums Camping;
   DEFINE Region / ORDER;
   BREAK AFTER Region / SUMMARIZE;
   RBREAK AFTER / SUMMARIZE;
   TITLE 'Detail Report with Summary Breaks';
RUN;

***4.23***;

LIBNAME visit '~/sasuser.v94/MySASLib';
*Statistics in COLUMN statement with two group variables;
PROC REPORT DATA = visit.natparks;
   COLUMN Region Type N (Museums Camping),MEAN;
   DEFINE Region / GROUP;
   DEFINE Type / GROUP;
   TITLE 'Statistics with Two Group Variables';
RUN;
*Statistics in COLUMN statement with group and across variables;
PROC REPORT DATA = visit.natparks;
   COLUMN Region N Type,(Museums Camping),MEAN;
   DEFINE Region / GROUP;
   DEFINE Type / ACROSS;
   TITLE 'Statistics with a Group and Across Variable';
RUN;

***4.24***;

LIBNAME visit '~/sasuser.v94/MySASLib';
* COMPUTE new variables that are numeric and character;
PROC REPORT DATA = visit.natparks;
   COLUMN Name Region Museums Camping Facilities Note;
   DEFINE Museums / ANALYSIS SUM NOPRINT;
   DEFINE Camping / ANALYSIS SUM NOPRINT;
   DEFINE Facilities / COMPUTED 'Campgrounds/and/Museums';
   DEFINE Note / COMPUTED;
   COMPUTE Facilities;
      Facilities = Museums.SUM + Camping.SUM;
   ENDCOMP;
   COMPUTE Note / CHAR LENGTH = 10;
      IF Camping.SUM = 0 THEN Note = 'No Camping';
   ENDCOMP;
   TITLE 'Report with Two Computed Variables'; 
RUN;

***5.2***;

LIBNAME ocean '~/sasuser.v94/MySASLib';
DATA ocean.marine;
   INFILE '~/sasuser.v94/MyRawData/Lengths8.dat';
   INPUT Name $ Family $ Length @@;
RUN;
* Create the HTML file and remove procedure name;
ODS HTML PATH = 'c:\MyHTMLFiles' BODY = 'Marine.html' 
   STYLE = BARRETTSBLUE;
ODS NOPROCTITLE;
PROC MEANS DATA = ocean.marine MEAN MIN MAX;
   CLASS Family;
   TITLE 'Whales and Sharks';
RUN;
PROC PRINT DATA = ocean.marine;
RUN;
ODS HTML CLOSE;

***5.3***;

* Create an RTF file;
LIBNAME ocean '~/sasuser.v94/MySASLib';
ODS RTF PATH = 'c:\MyRTFFiles' FILE= 'Marine.rtf' 
   BODYTITLE STARTPAGE = NO;
ODS NOPROCTITLE;
PROC MEANS DATA = ocean.marine MEAN MIN MAX;
   CLASS Family;
   TITLE 'Whales and Sharks';
RUN;
PROC PRINT DATA = ocean.marine;
RUN;
ODS RTF CLOSE;

***5.4***;

* Create the PDF file;
LIBNAME ocean '~/sasuser.v94/MySASLib';
ODS PDF FILE = 'c:\MyPDFFiles\Marine.pdf' STARTPAGE = NO;
ODS NOPROCTITLE;

PROC MEANS DATA = ocean.marine MEAN MIN MAX;
   CLASS Family;
   TITLE 'Whales and Sharks';
RUN;
PROC PRINT DATA = ocean.marine;
RUN;
ODS PDF CLOSE;

***5.5***;

* Create the text output and remove procedure name;
LIBNAME ocean '~/sasuser.v94/MySASLib';
ODS LISTING FILE = 'c:\MyTextFiles\Marine.lst';
ODS NOPROCTITLE;
PROC MEANS DATA = ocean.marine MEAN MIN MAX;
   CLASS Family;
   TITLE 'Whales and Sharks';
RUN;
PROC PRINT DATA = ocean.marine;
RUN;
ODS LISTING CLOSE;

***5.7***;

LIBNAME skate '~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Mens5000.csv' OUT = skate.results 
   REPLACE;
RUN;
PROC PRINT DATA = skate.results;
   ID Place;
   VAR Name Country Time;
   TITLE "Men's 5000m Speed Skating";
RUN;

* Use STYLE= option in PROC, ID, and VAR statements;
PROC PRINT DATA = skate.results
      STYLE(DATA) = {BACKGROUNDCOLOR = GRAY COLOR = WHITE};
   ID Place / STYLE(DATA) = {TEXTALIGN = CENTER};
   VAR Name / STYLE(DATA) = {FONTSTYLE = ITALIC};
   VAR Country Time;
   TITLE "Men's 5000m Speed Skating";
RUN;

***5.8***;

LIBNAME skate '~/sasuser.v94/MySASLib';
PROC REPORT DATA = skate.results;
   COLUMN Country Name Time Place;
   DEFINE Country / ORDER;
   TITLE "Men's 5000m Speed Skating";
RUN;

* Use STYLE= option in PROC and DEFINE statements;
PROC REPORT DATA = skate.results SPANROWS 
      STYLE(COLUMN) = {BACKGROUNDCOLOR = GRAY COLOR = WHITE};
   COLUMN Country Name Time Place;
   DEFINE Country / ORDER;
   DEFINE Name / STYLE(COLUMN) = {FONTSTYLE = ITALIC};
   DEFINE Place / STYLE(COLUMN) = {TEXTALIGN = CENTER};
   TITLE "Men's 5000m Speed Skating";
RUN;

***5.9***;

LIBNAME ocean '~/sasuser.v94/MySASLib';
PROC TABULATE DATA = ocean.marine;
   CLASS Family;
   VAR Length;
   TABLE Family, Length*(Min Max Mean);
   TITLE 'Whales and Sharks';
RUN;

* Use STYLE= option in PROC, CLASS, and VAR statements;
PROC TABULATE DATA = ocean.marine
      STYLE = {BACKGROUNDCOLOR = GRAY COLOR = WHITE};
   CLASS Family / STYLE = {FONTSTYLE = ITALIC};
   VAR Length / STYLE = {FONTSTYLE = ITALIC};
   TABLE Family, Length*(Min Max Mean);
   TITLE 'Whales and Sharks';
RUN;

***5.10***;

LIBNAME skate '~/sasuser.v94/MySASLib';
PROC PRINT DATA = skate.results;
   ID Place;
   TITLE "Men's 5000m Speed Skating";
RUN;

* Create user-defined format for colors;
PROC FORMAT;
   VALUE rec 0 -< 378.72 = 'LIGHT GRAY'
             378.72 -< 382.20 = 'VERY LIGHT GRAY'
             382.20 - HIGH = 'WHITE';
RUN;
* Use STYLE= option to apply format in VAR statement;
PROC PRINT DATA = skate.results;
   ID Place;
   VAR Name Country;
   VAR Time / STYLE = {BACKGROUNDCOLOR = rec.};
   TITLE "Men's 5000m Speed Skating";
RUN;

***5.12***;

LIBNAME tomatoes '~/sasuser.v94/MySASLib';
DATA tomatoes.giant;
   INFILE '~/sasuser.v94/MyRawData/GiantTom.dat' DSD;
   INPUT Name :$15. Color $ Days Weight @@;
RUN;
* Trace PROC MEANS;
ODS TRACE ON;
PROC MEANS DATA = tomatoes.giant;
   BY Color;
RUN;
ODS TRACE OFF;

* Print only the first BY group; 
PROC MEANS DATA = tomatoes.giant;
   BY Color;
ODS SELECT Means.ByGroup1.Summary;
RUN;

***5.13***;

LIBNAME tomatoes '~/sasuser.v94/MySASLib';
ODS TRACE ON;
PROC TABULATE DATA = tomatoes.giant;
   CLASS Color;
   VAR Days Weight;
   TABLE Color ALL, (Days Weight) * MEAN;
RUN;
ODS TRACE OFF;

PROC TABULATE DATA = tomatoes.giant;
   CLASS Color;
   VAR Days Weight;
   TABLE Color ALL, (Days Weight) * MEAN;
   TITLE 'Standard TABULATE Output';
ODS OUTPUT Table = tabout;
RUN;


***6.1***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/South.csv' OUT = southent REPLACE;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/North.csv' OUT = northent REPLACE;
RUN; 
* Create a data set, both, combining northent and southent;
* Create a variable, AmountPaid, based on value of variable Age;
DATA both;
   SET southent northent;
   IF Age = . THEN AmountPaid = .;
      ELSE IF Age < 3  THEN AmountPaid = 0;
      ELSE IF Age < 65 THEN AmountPaid = 35;
      ELSE AmountPaid = 27;
RUN;

***6.2***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/South.csv' OUT = southent REPLACE;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/North.csv' OUT = northent REPLACE;
RUN;
PROC SORT DATA = northent;
   BY PassNumber;
RUN;
* Interleave observations by PassNumber;
DATA interleave;
   SET southent northent;
   BY PassNumber;
RUN;

***6.3***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Chocolate.txt' OUT = names REPLACE;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Chocsales.txt' OUT = sales REPLACE;
RUN;
PROC SORT DATA = sales;
   BY Code;
RUN;
* Merge data sets by Code;
DATA chocolates;
   MERGE sales names;
   BY Code;
RUN;

***6.4***;

LIBNAME athshoes '~/sasuser.v94/MySASLib';
DATA athshoes.shoedata;
   INFILE '~/sasuser.v94/MyRawData/Shoe.dat';
   INPUT Style $ 1-15 ExerciseType $ RegularPrice;
RUN;
PROC SORT DATA = athshoes.shoedata OUT = regular;
   BY ExerciseType;
RUN;
DATA athshoes.discount;
   INFILE '~/sasuser.v94/MyRawData/Disc.dat';
   INPUT ExerciseType $ Adjustment;
RUN;
* Perform many-to-one match merge;
DATA prices;
   MERGE regular athshoes.discount;
   BY ExerciseType;
   NewPrice = ROUND(RegularPrice - (RegularPrice * Adjustment), .01);
RUN;

***6.5***;

LIBNAME athshoes '~/sasuser.v94/MySASLib';
* Perform an inner join using PROC SQL;
PROC SQL;
   CREATE TABLE prices AS
   SELECT *
   FROM athshoes.shoedata, athshoes.discount 
   WHERE shoedata.ExerciseType = discount.ExerciseType;
QUIT;

***6.6***;

LIBNAME athshoes '~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Shoesales.txt' 
            OUT = athshoes.shoesales REPLACE;
RUN;
PROC SORT DATA = athshoes.shoesales OUT = shoes;
   BY ExerciseType;
RUN;
* Summarize sales by ExerciseType;
PROC MEANS NOPRINT DATA = shoes;
   VAR Sales;
   BY ExerciseType;
   OUTPUT OUT = summarydata SUM(Sales) = Total;
RUN;
* Merge totals with the original data set;
DATA shoesummary;
   MERGE shoes summarydata;
   BY ExerciseType;
   Percent = Sales / Total * 100;
RUN;
PROC PRINT DATA = shoesummary LABEL;
   ID ExerciseType;
   VAR Style Sales Total Percent;
   LABEL Percent = 'Percent By Type';
   TITLE 'Sales Share by Type of Exercise';
RUN;

***6.7***;

LIBNAME athshoes '~/sasuser.v94/MySASLib';
* Output grand total of sales to a data set;
PROC MEANS NOPRINT DATA = athshoes.shoesales;
   VAR Sales;
   OUTPUT OUT = summarydata SUM(Sales) = GrandTotal;
RUN;
* Combine the grand total with the original data;
DATA shoesummary;
   IF _N_ = 1 THEN SET summarydata;
   SET athshoes.shoesales;
   Percent = Sales / GrandTotal * 100;
RUN;
PROC PRINT DATA = shoesummary;
   ID Style;
   VAR ExerciseType Sales GrandTotal Percent;
   TITLE 'Overall Sales Share';
RUN;

***6.8***;

LIBNAME athshoes '~/sasuser.v94/MySASLib';
*Create summary variables by exercise type;
PROC SQL; 
   CREATE TABLE shoesums AS
   SELECT *, SUM(Sales) AS TotalByType, 
             (Sales/SUM(Sales))*100 AS PercentByType
   FROM athshoes.shoesales
   GROUP BY ExerciseType;
QUIT;

*Create summary variables for whole data set;
PROC SQL;
   CREATE TABLE shoetotal AS
   SELECT *, SUM(Sales) AS GrandTotal, 
             (Sales/SUM(Sales))*100 AS Percent
   FROM athshoes.shoesales;
QUIT;

***6.9***;

LIBNAME records '~/sasuser.v94/MySASLib';
DATA records.patientmaster;
   INFILE '~/sasuser.v94/MyRawData/Admit.dat';
   INPUT Account LastName $ 8-16 Address $ 17-34
      BirthDate MMDDYY10. Sex $ InsCode $ 48-50 @52 LastUpdate MMDDYY10.;
   FORMAT BirthDate LastUpdate Date9.;
RUN;


LIBNAME records '~/sasuser.v94/MySASLib';
DATA transactions;
   INFILE '~/sasuser.v94/MyRawData/NewAdmit.dat';
   INPUT Account LastName $ 8-16 Address $ 17-34 
      BirthDate MMDDYY10. Sex $ InsCode $ 48-50 @52 LastUpdate MMDDYY10.;
RUN;
PROC SORT DATA = transactions;
   BY Account;
RUN;
* Update patient data with transactions;
DATA records.patientmaster;
   UPDATE records.patientmaster transactions;
   BY Account;
RUN;

***6.11***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/CustAdd.txt' OUT = customer REPLACE;
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/OrdersQ3.txt' OUT = orders REPLACE;
RUN;
PROC SORT DATA = orders;
   BY CustNum;
RUN;
* Combine the data sets using the IN= option;
DATA noorders;
   MERGE customer orders (IN = Recent);
   BY CustNum;
   IF Recent = 0;
RUN;

***6.12***;

*Input the data and create two subsets;
DATA tallpeaks (WHERE = (Height > 6000)) 
     american (WHERE = (Continent CONTAINS ('America')));
   INFILE '~/sasuser.v94/MyRawData/Mountains.dat';
   INPUT Name $1-14 Continent $15-28 Height;
RUN;
PROC PRINT DATA = tallpeaks;
   TITLE 'Members of the Seven Summits above 6,000 Meters';
RUN;
PROC PRINT DATA = american; 
   TITLE 'Members of the Seven Summits in the Americas';
RUN;

***6.13***;

PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Transpos.csv' OUT = baseball REPLACE;
PROC SORT DATA = baseball;
   BY Team Player;
RUN;
* Transpose data so salary and batavg are variables;
PROC TRANSPOSE DATA = baseball OUT = flipped;
   BY Team Player;
   ID Type;
   VAR Entry;
RUN;

***6.14***;

DATA walkers;
   INFILE '~/sasuser.v94/MyRawData/Walk.dat';
   INPUT Entry AgeGroup $ Time @@;
RUN;
PROC SORT DATA = walkers;
   BY Time; RUN;
* Create a new variable, Place;
DATA ordered;
   SET walkers;
   Place = _N_;
RUN;
PROC PRINT DATA = ordered;
   ID Place;
   TITLE 'Results of Walk';
RUN; 
PROC SORT DATA = ordered;
   BY AgeGroup Time;
RUN;
* Keep the first observation in each age group;
DATA winners;
   SET ordered;
   BY AgeGroup;
   IF FIRST.AgeGroup = 1;
PROC PRINT DATA = winners;
   ID Place;
   TITLE 'Winners in Each Age Group';
RUN;

***7.2***;

%LET FlowerType = Ginger;
* Read the raw data and create a permanent SAS data set;
LIBNAME tropical '~/sasuser.v94/MySASLib';
DATA tropical.flowersales;
   INFILE '~/sasuser.v94/MyRawData/TropicalFlowers.dat';
   INPUT Location CustomerID $4. @8 SaleDate MMDDYY10. @19 Variety $9. 
         SaleQuantity SaleAmount;
   FORMAT SaleDate MMDDYY10.;
RUN;
* Print the report using a macro variable;
PROC PRINT DATA = tropical.flowersales;
   WHERE Variety = "&FlowerType";
   FORMAT SaleAmount DOLLAR7.;
   TITLE "Sales of &FlowerType";
RUN;

***7.3***;

%LET SumVar = Quantity;
LIBNAME tropical '~/sasuser.v94/MySASLib';
* Create RTF file with today's date in the file name;
ODS RTF PATH = 'c:\MyRTFFiles' FILE = "FlowerSales_&SYSDATE..rtf";
* Summarize the sales for the selected variable;
PROC MEANS DATA = tropical.flowersales SUM MIN MAX MAXDEC=0;
   VAR Sale&SumVar;
   CLASS Variety;
   TITLE "Summary of Sales &SumVar by Variety";
RUN;
* Close the RTF file;
ODS RTF CLOSE;

***7.4***;

LIBNAME tropical '~/sasuser.v94/MySASLib';

* Macro to print 5 largest sales;
%MACRO Sample;
   PROC SORT DATA = tropical.flowersales OUT = salesout;
      BY DESCENDING SaleQuantity;
   RUN;
   PROC PRINT DATA = salesout (OBS = 5);
      FORMAT SaleAmount DOLLAR7.;
      TITLE 'Five Largest Sales by Quantity';
   RUN;
%MEND Sample;
* Invoke the macro;
%Sample

***7.5***;

LIBNAME tropical '~/sasuser.v94/MySASLib';

* Macro with parameters;
%MACRO Select(Customer=,SortVar=);
   PROC SORT DATA = tropical.flowersales OUT = salesout;
      BY &SortVar;
      WHERE CustomerID = "&Customer";
   RUN;
   PROC PRINT DATA = salesout;
      FORMAT SaleAmount DOLLAR7.;
      TITLE1 "Orders for Customer Number &Customer";
      TITLE2 "Sorted by &SortVar";
   RUN;
%MEND Select;

*Invoke the macro;
%Select(Customer = 356W, SortVar = SaleQuantity)
%Select(Customer = 240W, SortVar = Variety)

***7.6***;

LIBNAME tropical '~/sasuser.v94/MySASLib';

*This macro selects which report to run based on the day of the week;
%MACRO DailyReports;
   %IF &SYSDAY = Monday %THEN %DO;
      PROC PRINT DATA = tropical.flowersales;
         FORMAT SaleAmount DOLLAR7.;
         TITLE 'Monday Report: Current Flower Sales';
      RUN;
   %END;
   %ELSE %IF &SYSDAY = Tuesday %THEN %DO;
      PROC MEANS DATA = tropical.flowersales MEAN MIN MAX MAXDEC = 2;
         CLASS Variety;
         VAR SaleQuantity;
         TITLE 'Tuesday Report: Summary of Flower Sales';
      RUN;
   %END;
%MEND DailyReports;

%DailyReports

***7.7***;

LIBNAME tropical '~/sasuser.v94/MySASLib';

*This macro creates summary data sets for each value of location;
%MACRO MeanSales;
  %DO Loc = 1 %TO 2;
    PROC MEANS DATA = tropical.flowersales NOPRINT;
      WHERE Location = &Loc;
      VAR SaleQuantity SaleAmount;
      OUTPUT OUT = salesloc&Loc
         SUM(SaleQuantity SaleAmount) = TotalQuantity TotalAmount;
    RUN;
  %END;
%MEND MeanSales;

%MeanSales

***7.8***;

LIBNAME tropical '~/sasuser.v94/MySASLib';

* Sort the data by descending SaleAmount and save to a temporary data set;
PROC SORT DATA = tropical.flowersales OUT = salessorted;
   BY DESCENDING SaleAmount;
RUN;

* Find biggest order and pass the customer id to a macro variable;
DATA _NULL_;
   SET salessorted ;
   IF _N_ = 1 THEN CALL SYMPUTX("SelectedCustomer",CustomerID);
   STOP;
RUN;

PROC PRINT DATA = tropical.flowersales;
   WHERE CustomerID = "&SelectedCustomer";
   FORMAT SaleAmount DOLLAR7.;
   TITLE "Customer &SelectedCustomer Had the Single Largest Order";
RUN;

***7.9***;

LIBNAME tropical '~/sasuser.v94/MySASLib';
*Find customer with largest single sale amount;
PROC SQL NOPRINT;
  SELECT CustomerID 
    INTO :SelectedCustomer 
    FROM tropical.flowersales
    HAVING SaleAmount = MAX(SaleAmount);
QUIT;
PROC PRINT DATA = tropical.flowersales;
   WHERE CustomerID = "&SelectedCustomer";
   FORMAT SaleAmount DOLLAR7.;
   TITLE "Customer &SelectedCustomer Had the Single Largest Order";
RUN;


***8.2***;

DATA chocolate;
   INFILE '~/sasuser.v94/MyRawData/Choc.dat';
   INPUT AgeGroup $ FavoriteFlavor $ @@;
RUN;
PROC FORMAT;
   VALUE $AgeGp 'A' = 'Adult' 'C' = 'Child';
RUN;
* Bar chart for favorite flavor;
PROC SGPLOT DATA = chocolate;
   VBAR FavoriteFlavor / GROUP = AgeGroup GROUPDISPLAY = CLUSTER;
   FORMAT AgeGroup $AgeGp.;   
   LABEL FavoriteFlavor = 'Flavor of Chocolate';
   TITLE 'Favorite Chocolate Flavors by Age';
RUN;

***8.3***;

DATA contest;
   INFILE '~/sasuser.v94/MyRawData/Reading.dat';
   INPUT Name $ NumberBooks @@;
RUN;
PROC SGPLOT DATA = contest;
   HISTOGRAM NumberBooks / BINWIDTH = 2 SHOWBINS SCALE = COUNT;
   DENSITY NumberBooks;
   DENSITY NumberBooks / TYPE = KERNEL;
   TITLE 'Reading Contest';
RUN;

***8.4***;

DATA bikerace;
   INFILE '~/sasuser.v94/MyRawData/Criterium.dat';
   INPUT Division $ NumberLaps @@;
RUN;
* Create box plot;
PROC SGPLOT DATA = bikerace;
   VBOX NumberLaps / CATEGORY = Division;
   TITLE 'Bicycle Criterium Results by Division';
RUN;

***8.5***;

LIBNAME flight '~/sasuser.v94/MySASLib';
DATA flight.wings;
   INFILE '~/sasuser.v94/MyRawData/Birds.dat';
   INPUT Name $12. Type $ Length Wingspan @@;
RUN;
* Plot Wingspan by Length;
PROC FORMAT;
   VALUE $birdtype
      'S' = 'Songbirds'
      'R' = 'Raptors';
RUN;
PROC SGPLOT DATA = flight.wings;
   SCATTER X = Wingspan Y = Length / GROUP = Type;
   FORMAT Type $birdtype.;
   TITLE 'Comparison of Wingspan vs. Length';
RUN;

***8.6***;

DATA electricity;
   INFILE '~/sasuser.v94/MyRawData/Hourly.dat';
   INPUT Time kWh @@;
RUN;
* Plot temperatures by time;
PROC SGPLOT DATA = electricity;
   SERIES X = Time Y = kWh / MARKERS;
   TITLE 'Hourly Use of Electricity';
RUN;

***8.7***;

DATA weekly1500;
   INFILE '~/sasuser.v94/MyRawData/Weekly1500.dat';
   INPUT Week Time @@;
RUN;
PROC SGPLOT DATA = weekly1500;
   LOESS X = Week Y = Time / NOMARKERS CLM NOLEGCLM;
   REG X = Week Y = Time;
   LABEL Time = 'Time in Seconds';
   TITLE 'Times for 1500 Meter Run';
RUN;

***8.8***;

DATA cities;
   INFILE '~/sasuser.v94/MyRawData/ThreeCities.dat';
   INPUT Month IntFalls Raleigh Yuma @@;
RUN;
* Plot average high and low temperatures by city;
PROC SGPLOT DATA = cities;
   SERIES X = Month Y = IntFalls;
   SERIES X = Month Y = Raleigh;
   SERIES X = Month Y = Yuma;
   REFLINE 32 75 / LABEL = ('32 degrees' '75 degrees') TRANSPARENCY = 0.5;
   XAXIS TYPE = DISCRETE;
   YAXIS LABEL = 'Average High Temperature (F)';
   TITLE 'Temperatures for International Falls, Raleigh, and Yuma';
RUN;

***8.9***;

LIBNAME flight '~/sasuser.v94/MySASLib';
* Plot Wingspan by Length;
PROC FORMAT;
   VALUE $birdtype
      'S' = 'Songbirds'
      'R' = 'Raptors';
RUN;
PROC SGPLOT DATA = flight.wings;
   SCATTER X = Wingspan Y = Length / GROUP = Type;
   KEYLEGEND / LOCATION = INSIDE POSITION = BOTTOMRIGHT;
   INSET 'Birds of North America' / POSITION = TOPLEFT;
   FORMAT Type $birdtype.;
   TITLE 'Comparison of Wingspan vs. Length';
RUN;

***8.10***;

LIBNAME flight '~/sasuser.v94/MySASLib';
* Plot Wingspan by Length;
PROC SGPLOT DATA = flight.wings NOAUTOLEGEND;
   REG X = Wingspan Y = Length / 
      LINEATTRS = (THICKNESS = 2MM) TRANSPARENCY = .75;
   SCATTER X = Wingspan Y = Length / 
      MARKERATTRS = (SYMBOL = CIRCLEFILLED SIZE = 2MM);
   TITLE BOLD 'Birds of North America';
   XAXIS LABEL = 'Wingspan (in cm)' LABELATTRS = (WEIGHT = BOLD);
   YAXIS LABEL = 'Body Length (in cm)' LABELATTRS = (WEIGHT = BOLD);
RUN;

***8.11***;

LIBNAME flight '~/sasuser.v94/MySASLib';
* Plot Wingspan by Length;
PROC FORMAT;
   VALUE $birdtype
      'S' = 'Songbirds'
      'R' = 'Raptors';
RUN;
PROC SGPANEL DATA = flight.wings;
   PANELBY Type / NOVARNAME SPACING = 5;
   SCATTER X = Wingspan Y = Length;
   FORMAT Type $birdtype.;
   TITLE 'Comparison of Wingspan vs. Length';
RUN;

***8.12***;

LIBNAME flight '~/sasuser.v94/MySASLib';
* Create BMP image of Wingspan by Length;
ODS LISTING GPATH = 'c:\MyGraphs' STYLE = JOURNAL;
ODS GRAPHICS / RESET IMAGENAME = 'BirdGraph' OUTPUTFMT = BMP 
   HEIGHT = 2IN WIDTH = 3IN;
PROC SGPLOT DATA = flight.wings;
   SCATTER X = Wingspan Y = Length;
   TITLE 'Comparison of Wingspan vs. Length';
RUN;
ODS GRAPHICS / RESET;



***9.1***;

LIBNAME f2020 '~/sasuser.v94/MySASLib'; 
DATA f2020.statclass;
   INFILE '~/sasuser.v94/MyRawData/Scores.dat';
   INPUT Score @@;
RUN;
*Summarize data using PROC UNIVARIATE;
PROC UNIVARIATE DATA = f2020.statclass;
   VAR Score;
   TITLE;
RUN;

***9.2***;

LIBNAME f2020 '~/sasuser.v94/MySASLib';
*Create histogram and probability plot for variable Score; 
PROC UNIVARIATE DATA = f2020.statclass;
   VAR Score;
   HISTOGRAM Score / NORMAL;
   PROBPLOT Score;
   TITLE;
RUN;

***9.3***;

DATA booklengths;
   INFILE '~/sasuser.v94/MyRawData/Picbooks.dat';
   INPUT NumberOfPages @@;
RUN;
*Produce summary statistics;
PROC MEANS DATA = booklengths N MEAN MEDIAN CLM ALPHA = .10;
   TITLE 'Summary of Picture Book Lengths';
RUN;

***9.4***;

LIBNAME results '~/sasuser.v94/MySASLib';
DATA results.swim;
   INFILE '~/sasuser.v94/MyRawData/Olympic50mSwim.dat';
   INPUT Swimmer $ FinalTime SemiFinalTime @@;
RUN;
*Perform paired t test for semifinal and final times;
PROC TTEST DATA = results.swim;
  TITLE '50m Freestyle Semifinal vs. Final Results';
  PAIRED SemiFinalTime * FinalTime;
RUN;

***9.5***;

LIBNAME results '~/sasuser.v94/MySASLib';
*Produce just the Summary and QQ plots;
PROC TTEST DATA = results.swim PLOTS(ONLY) = (SUMMARYPLOT QQPLOT);
  TITLE '50m Freestyle Semifinal vs. Final Results';
  PAIRED SemiFinalTime * FinalTime;
RUN;

***9.6***;

LIBNAME trans '~/sasuser.v94/MySASLib';
DATA trans.bus;
   INFILE '~/sasuser.v94/MyRawData/Bus.dat';
   INPUT BusType $ OnTimeOrLate $ @@;
RUN;
*Perform chi-square analysis on bus data;
PROC FREQ DATA = trans.bus;
   TABLES BusType * OnTimeOrLate / CHISQ;
   TITLE;
RUN;

***9.7***;

LIBNAME trans '~/sasuser.v94/MySASLib';
PROC FORMAT;
  VALUE $type 'R'='Regular'
              'E'='Express';
  VALUE $late 'O'='On Time'
              'L'='Late';
RUN;
*Produce frequency plot grouped horizontally;
PROC FREQ DATA = trans.bus;
   TABLES BusType * OnTimeOrLate / PLOTS=FREQPLOT(TWOWAY=GROUPHORIZONTAL);
   FORMAT BusType $Type. OnTimeOrLate $Late.;
RUN;

***9.8***;

LIBNAME mylib '~/sasuser.v94/MySASLib';
DATA mylib.class;
   INFILE '~/sasuser.v94/MyRawData/Exercise.dat';
   INPUT Score Videos Exercise @@;
RUN;
*Perform correlation analysis;
PROC CORR DATA = mylib.class;
   VAR Videos Exercise;
   WITH Score;
   TITLE 'Correlations for Test Scores';
   TITLE2 'With Hours of Videos and Exercise';
RUN;

***9.9***;

LIBNAME mylib '~/sasuser.v94/MySASLib';
*Generate scatter and matrix plots for correlation analysis;
PROC CORR DATA = mylib.class PLOTS = (SCATTER MATRIX);
   VAR Videos Exercise;
   WITH Score;
   TITLE 'Correlations for Test Scores';
   TITLE2 'With Hours of Videos and Exercise';
RUN;

***9.10***;

LIBNAME tball '~/sasuser.v94/MySASLib';
DATA tball.hits;
   INFILE '~/sasuser.v94/MyRawData/Baseball.dat';
   INPUT Height Distance @@;
RUN;
* Perform regression analysis;
PROC REG DATA = tball.hits;
   MODEL Distance = Height;
   TITLE 'Results of Regression Analysis';
RUN;

***9.11***;

LIBNAME tball '~/sasuser.v94/MySASLib';
*Limit plots generated to diagnostics panel and fit plot;
PROC REG DATA = tball.hits PLOTS(ONLY) = (DIAGNOSTICS FITPLOT);
   MODEL Distance = Height;
   TITLE 'Results of Regression Analysis';
RUN;

***9.12***;

DATA heights;
   INFILE '~/sasuser.v94/MyRawData/GirlHeights.dat';
   INPUT Region $ Height @@;
RUN;
* Use ANOVA to run one-way analysis of variance;
PROC ANOVA DATA = heights;
   CLASS Region;
   MODEL Height = Region;
   MEANS Region / SCHEFFE;
   TITLE "Girls' Heights from Four Regions";
RUN;

***10.2***;

LIBNAME travel '~/sasuser.v94/MySASLib';
PROC IMPORT DATAFILE = '~/sasuser.v94/MyRawData/Golf.txt' OUT = travel.golf REPLACE;
RUN;

LIBNAME travel '~/sasuser.v94/MySASLib';
*Create comma-delimited file;
PROC EXPORT DATA = travel.golf OUTFILE = '~/sasuser.v94/MyRawData/Golf.csv' REPLACE;
RUN;

***10.3***;

LIBNAME travel '~/sasuser.v94/MySASLib';
*Create comma-delimited file from PROC PRINT results;
OPTIONS MISSING = '';
ODS CSV FILE = '~/sasuser.v94/MyRawData/GolfInfo.csv';
PROC PRINT DATA = travel.golf NOOBS;
RUN;
ODS CSV CLOSE;

*Create comma-delimted file from PROC MEANS results;
ODS CSV FILE='~/sasuser.v94/MyRawData/GolfMeans.csv';
PROC MEANS DATA = travel.golf MAXDEC = 0 MEAN MAX;
  CLASS par;
  VAR Yardage GreenFees;
RUN;
ODS CSV CLOSE; 

***10.4***;

LIBNAME travel '~/sasuser.v94/MySASLib';
* Create Microsoft Excel file';
PROC EXPORT DATA = travel.golf OUTFILE = '~/sasuser.v94/MyExcel/Golf.xlsx' 
   DBMS = XLSX REPLACE;
RUN;

***10.5***;

LIBNAME travel '~/sasuser.v94/MySASLib';
*Create one Excel file with two worksheets;
OPTIONS MISSING = '';
ODS EXCEL FILE = '~/sasuser.v94/MyExcel/golfinfo.xlsx';
ODS EXCEL OPTIONS(SHEET_NAME = 'GolfData' AUTOFILTER = '1-5');
PROC PRINT DATA = travel.golf NOOBS;
RUN;
ODS NOPROCTITLE;
ODS EXCEL OPTIONS(SHEET_NAME = 'GolfMeans' AUTOFILTER = 'NONE');
PROC MEANS DATA = travel.golf MAXDEC = 0 MEAN MIN MAX;
   CLASS Par; 
   VAR Yardage GreenFees;
RUN;
ODS EXCEL CLOSE;

***10.6***;

LIBNAME travel '~/sasuser.v94/MySASLib';
*Create raw data file using FILE and PUT statements;
DATA _NULL_;
   SET travel.golf;
   FILE '~/sasuser.v94/MyRawData/Newfile.dat';
   PUT CourseName 'Golf Course' @32 GreenFees DOLLAR7.2 @40 'Par ' Par;
RUN;





