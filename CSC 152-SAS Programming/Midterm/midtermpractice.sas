data myvotes;
infile '~/my_shared_file_links/michaelweinberg0/ExamData/Votes.csv' dlm = ',' dsd missover;
input county :$16. state $ voting_pct median_age mean_savings
    per_capita_income pct_in_poverty pct_veterans percent_female pop_density crime_index;
run;


*1.;
data noDC;
	infile '~/my_shared_file_links/michaelweinberg0/ExamData/Votes.csv' dlm = ',' dsd missover;
	input county :$16. state $ @;
	if state = 'DC' then delete;
	input voting_pct median_age mean_savings
    	per_capita_income pct_in_poverty pct_veterans percent_female pop_density crime_index;
run;

* 2.;
data noDCLowestMedianAge;
	infile '~/my_shared_file_links/michaelweinberg0/ExamData/Votes.csv' dlm = ',' dsd missover;
	input county :$16. state $ @;
	if state = 'DC' then delete;
	input voting_pct median_age mean_savings
    	per_capita_income pct_in_poverty pct_veterans percent_female pop_density crime_index;
    retain Lowest;
	Lowest = min(Lowest, median_age);
run;	
	
* 3. ;
proc tabulate data = noDCLowestMedianAge;
	class state ;
	var voting_pct;
	table state, max*voting_pct min*voting_pct mean*voting_pct;
run;

* 4. ;
proc report data = noDC;
	column state voting_pct, (mean min max);
	define state  / group;
run;

*5.;
proc means data = noDC;
	class state;
	var voting_pct;
	output out = stateInfo
		mean(voting_pct) = MeanVotingPercentage
		min(voting_pct) = MinimumVotingPercentage
		max(voting_pct) = MaximumVotingPercentage;
run;
proc print data = stateInfo (firstobs = 2) noobs ;
	var state MeanVotingPercentage MinimumVotingPercentage MaximumVotingPercentage;
run;

proc means data = noDC mean min max;
	class state;
	var voting_pct;
run;


* 6.;
PROC FORMAT;
	VALUE alpha_voting_pct 0 -< 40 = 'Low'
						  40 -< 45 = 'Medium'
						  45 -< 100 = 'High';
						  
proc print data = noDC noobs;
	var state county per_capita_income voting_pct;
	format voting_pct alpha_voting_pct.;
run;