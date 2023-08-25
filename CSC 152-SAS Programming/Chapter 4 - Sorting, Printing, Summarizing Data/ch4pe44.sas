LIBNAME Chap4 '~/sasuser.v94/Chapter4';
* a.;
PROC SQL;
	CREATE TABLE diving AS	
		SELECT *
		FROM Chap4.diving
		ORDER BY Name;
QUIT;

PROC REPORT DATA = Chap4.diving;
	COLUMN Score1, (MEAN MIN MAX) Score2, (MEAN MIN MAX);
	TITLE 'Overall Mean, Minimum, and Maximum of the Two Scoring Methods';
RUN;

* b.;
PROC MEANS DATA = Chap4.diving;
	CLASS Name;
	VAR Score2;
	OUTPUT OUT = totals
		SUM(Score2) = TotalScore;
RUN;

PROC SORT DATA = totals OUT = sortedtotals;
	BY DESCENDING TotalScore;
RUN;

PROC PRINT DATA = sortedtotals (FIRSTOBS = 2) NOOBS;
	VAR Name TotalScore;
	TITLE 'Total Score by Diver';
RUN;

* Gold: ZAKHAROV Ilya;
* Silver: QIN Kai;
* Bronze HE Chong;

* c.;
PROC FORMAT;
	VALUE alphaScore 0 -< 0.5 = 'Completely Failed'
				   0.5 -< 2.5 = 'Unsatisfactory'
				   2.5 -< 5.0 = 'Deficient'
				   5.0 -< 7.0 = 'Satisfactory'
				   7.0 -< 8.5 = 'Good'
				   8.5 -< 9.5 = 'Very Good'
				   9.5 -< 100 = 'Excellent';
				   
PROC PRINT DATA = Chap4.diving NOOBS;
	VAR Name J1 J2 J3 J4 J5 J6 J7;
	FORMAT J1 alphaScore. J2 alphaScore. J3 alphaScore. J4 alphaScore. J5 alphaScore. J6 alphaScore. J7 alphaScore.;
	TITLE 'Formatted Scores by Dive by Judge';
RUN;

* d.;
PROC SORT DATA = Chap4.diving OUT = sortedscores;
	BY Name Dive;
RUN;

PROC REPORT DATA = sortedscores;
	COLUMN Name Dive MinScore MaxScore;
	DEFINE MinScore / COMPUTED;
	DEFINE MaxScore / COMPUTED;
	COMPUTE MinScore;
		MinScore = MIN(J1, J2, J3, J4, J5, J6, J7);
	ENDCOMP;
	COMPUTE MaxScore;
		MaxScore = MAX(J1, J2, J3, J4, J5, J6, J7);
	ENDCOMP;
	TITLE 'Minimum and Maximum Scores per Diver per Dive';
RUN;

* I'm getting missing values and I can't figure out why.








	
					