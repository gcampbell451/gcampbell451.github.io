DATA compUsers;
INFILE "~/sasuser.v94/Chapter2/CompUsers.dat";
INPUT userID classGroup $ fName :$CHAR12. lName  :$CHAR15. 
	  / email :$CHAR35. phone :$CHAR14. department $;
RUN;

PROC PRINT DATA = compUsers;
RUN;

DATA compUsers2;
INFILE "~/sasuser.v94/Chapter2/CompUsers.dat";
INPUT userID classGroup $ @;
IF classGroup = 'Student' THEN DELETE;
INPUT fName :$CHAR12. lName  :$CHAR15. 
	  / email :$CHAR35. phone :$CHAR14. department $;
RUN;

PROC PRINT DATA = compUsers2;
RUN;
`