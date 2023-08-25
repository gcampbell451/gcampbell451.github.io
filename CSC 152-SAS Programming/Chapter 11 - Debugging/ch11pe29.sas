* a.;
LIBNAME sasdata '~/sasuser.v94/Chapter8';

DATA alaska (DROP = Year Month Day); 
	SET sasdata.earthquakes;
	IF State = Alaska;	
	EruptionDate = MDY(Month, Day, Year); 
RUN;

PROC PRINT DATA = alaska NOROWNUM; 
	WHERE Year GT 2005;		
	VAR EruptionDate Magnitude;
	TITLE 'Alaska's Earthquakes in 2005 or Later'; 
	FORMAT EruptionDate DATE10.;
RUN;';

* b. add comments to revised program;
DATA alaska;			    * One of the requirements of the output is the date of the quake. The DROP statement drops that information from the dataset.;
	SET sasdata.earthquakes;
	IF State = 'Alaska';	* Without quotation marks around the state name, this statement creates a variable, but with no conditions, so no observations are added.;
	EruptionDate = MDY(Month, Day, Year);
RUN;

PROC PRINT DATA = alaska NOOBS;	* If you don't want to display observation numbers, the correct option is NOOBS.;
	WHERE Year GE 2005;			* Using the GT operator displays only quakes after 2005. This omits quakes in 2005. Use GE (greater than or equal to) or >= instead.;
	VAR EruptionDate Magnitude;
	TITLE "Alaska's Earthquakes in 2005 or Later";	* When single quotes are used in a string, enclose them with double quotation marks. SAS read the apostrophe as ;
	FORMAT EruptionDate WORDDATE12.;				* closing the string. Note the year in your code is green, so it is being interpreted as a number, not part of a string. ;
RUN;												* The third single quote, instead of closing the string for your title, is interpreted as the start of a new string, ;
													* and everything after it, including the RUN statement, is part of the title string. Note I had to close the PROC ;
													* PRINT statement with a single quote and then semicolon to get the proper code to run below. SAS color strings purple, ;
													* so pay close attention to the color to confirm the quotes enclose the string you want them to.
													*;
													* While your chosen format for the date does satisfy the requirements of the assignment, it is not the easiest ;
													* date format to read.;
													





