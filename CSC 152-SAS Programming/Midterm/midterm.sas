* Gregory Campbell 	Midterm Exam 	March 2, 2022;

data covid;
	infile '~/my_shared_file_links/michaelweinberg0/ExamData/midtermSP2022.csv'
    	dlm = ',' firstobs = 2 dsd missover;
	input submission_date :MMDDYY10. state $ new_case new_death;
run;

* 1.;
proc sort data = covid out = covidSorted;
	by state submission_date;
run;

proc print data = covidSorted noobs;
	var state submission_date new_case new_death;
	format submission_date mmddyy10.;
run;

* 2.;
proc tabulate data = covidSorted format = comma12.0;
	class state;
	var new_case;
	table state ALL, sum*new_case mean*new_case max*new_case;
	title 'Total, Mean, and Daily Maximum of New Cases - Proc Tabulate';
run;

* 3.;
proc report data = covidSorted;
	column state new_case, (sum mean max);
	define state / group;
	define new_case / format = comma12.0;
	rbreak after / summarize;
	title 'Total, Mean, and Daily Maximum of New Cases - Proc Report';
run;

* 4.;
proc means data = covidSorted sum mean max;
	class state;
	var new_case;
	output out = covidAnalysis
		sum(new_case) = SumNewCases
		mean(new_case) = MeanNewCases
		max(new_case) = MaxNewCases;
run;

proc print data = covidAnalysis noobs;
	var state SumNewCases MeanNewCases MaxNewCases;
	format SumNewCases comma12.0 MeanNewCases comma8.0 MaxNewCases comma8.0;
	title 'Total, Mean, and Daily Maximum of New Cases - Proc Means';
run;

* 5.;
data covidNCJan22;
	infile '~/my_shared_file_links/michaelweinberg0/ExamData/midtermSP2022.csv'
   	  dlm = ',' firstobs = 2 dsd missover;
	input submission_date :MMDDYY10. @;
	if submission_date < 22646 or submission_date > 22676 then delete;
	input state $ @;
	if state ^= 'NC' then delete;
	input new_case new_death;
	MortalityRate = new_death / new_case;
run;

proc sort data = covidNCJan22 out = covidNCSorted;
	by state submission_date;
run;

proc print data = covidNCSorted noobs;
	var state submission_date new_case new_death MortalityRate;
	format submission_date mmddyy10. MortalityRate percent.2;
	title 'New Cases, Deaths, and Mortality Rate, January 2022, North Carolina';
run;






