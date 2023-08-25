LIBNAME chap6 '~/sasuser.v94/Chapter6';
* a. combine two data sources to create a data set that identifies the treatment group for each subject;
DATA visits;
	SET chap6.visits;
RUN;
PROC SORT DATA = visits;
	BY ID;
RUN;

DATA txgroup;
	SET chap6.txgroup;
RUN;

DATA mergeByID;
	MERGE visits txgroup;
	BY ID;
	IF TX = 0 THEN TreatmentGroup = "Placebo";
		ELSE TreatmentGroup = "Treated";
RUN;

* b. eliminate any duplicate entries;
DATA mergeByIDUnique;
	MERGE visits txgroup;
	BY ID;
	IF FIRST.ID = 1;
	IF TX = 0 THEN TreatmentGroup = "Placebo";
		ELSE TreatmentGroup = "Treated";
RUN;

* c. using b, calculate median cholesterol, create variable that groups subjects as
     less than or equal to median or more than median;
PROC MEANS DATA = mergeByIDUnique MEDIAN;
	VAR B_Cholesterol;
	OUTPUT OUT = summaryData MEDIAN(B_Cholesterol) = Median;
RUN;

PROC SQL;
	CREATE TABLE compareToMedian AS
	SELECT ID, B_Cholesterol, MEDIAN(B_Cholesterol) AS Median
	FROM mergeByIDUnique;
QUIT;

DATA compareToMedian;
	SET comparetomedian;
	IF B_Cholesterol > Median Then HiLo = "GT Median";
		ELSE HiLo = "LE Median";
RUN;

* I couldn't quite tell whether the instructions require a sorting. They say to create a variable that groups subjects 
  but didn't explicitly say to actually group them.;
PROC SORT DATA = compareToMedian;
	BY HiLo;
RUN;