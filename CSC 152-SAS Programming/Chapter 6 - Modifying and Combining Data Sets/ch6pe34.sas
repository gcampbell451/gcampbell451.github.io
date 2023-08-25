LIBNAME chap6 '~/sasuser.v94/Chapter6';
* a. note the sort order of observations in data sets, state number of variables in
     both sets and number only in one of the sets;
DATA friends;
	SET chap6.friends;
RUN;
PROC SORT DATA = friends;
	BY ID;
RUN;

DATA newinfo;
	SET chap6.newinfo;
RUN;
PROC SORT DATA = newinfo;
	BY ID;
RUN;
* Both sets are sorted on ID. The variables ID, Last Name, First Name, Address, City, State, and Volunteer appear
  in both data sets. The variables Donation and Campaign appear only in the newinfo set. No unique variables appear 
  in the friends set.
  
* b. merge the data sets, make backup copies of data sets;
DATA friendsBak;
	SET chap6.friends;
RUN;
PROC SORT DATA = friendsBak;
	BY ID;
RUN;

DATA newinfoBak;
	SET chap6.newinfo;
RUN;
PROC SORT DATA = newinfoBak;
	BY ID;
RUN;

DATA friendsBak;
	UPDATE friendsBak newinfoBak;
	BY ID;
RUN;

* c. compute total donations by ID, combine with friends data, produce report listing ID, first and last name, 
     total donations for each friend;
PROC MEANS DATA = newinfoBak;
	VAR Donation;
	BY ID;
	OUTPUT OUT = sumDonations SUM(Donation) = TotalDonations;
RUN;

DATA donationsReport;
	MERGE friendsBak sumDonations;
	BY ID;
RUN;

PROC REPORT DATA = donationsReport;
	COLUMN ID FirstName LastName TotalDonations;
	DEFINE ID / GROUP;
	DEFINE TotalDonations / GROUP;
	TITLE 'Total Donations for Each Friend';
RUN;

