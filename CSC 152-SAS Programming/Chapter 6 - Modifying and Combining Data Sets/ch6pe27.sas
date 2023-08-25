LIBNAME chap6 '~/sasuser.v94/Chapter6';
* a. examine all data sets, create variable that is equal to popularity rank;
DATA australia;
	SET chap6.australia;
	Rank = _N_;
RUN;
DATA brazil (RENAME = (Menina = Girl Menino = Boy));
	SET chap6.brazil;
	Rank = _N_;
RUN;
DATA france (RENAME = (Fille = Girl Garcon = Boy));
	SET chap6.france;
	Rank = _N_;
RUN;
DATA india (RENAME = (Laraki = Girl Laraka = Boy));
	SET chap6.india;
	Rank = _N_;
RUN;
DATA russia (RENAME = (Devushka = Girl Malchik = Boy));
	SET chap6.russia;
	Rank = _N_;
RUN;
DATA usa;
	SET chap6.unitedstates;
	Rank = _N_;
RUN;

* b. stack sets, sort results by popularity ranking;
DATA stacked;
	SET australia brazil france india russia usa;
RUN;
PROC SORT DATA = stacked;
	BY Rank;
RUN;

* c. interleave sets by rank;
DATA interleaved;
	SET australia brazil france india russia usa;
	BY Rank;
RUN;

* d. add code to c. that creates a variable representing country name;
DATA interleaved2;
	SET australia (IN = aus)
		brazil (IN = bra)
		france (IN = fra)
		india (IN = ind) 
		russia (IN = rus) 
		usa (IN = usa);
	BY Rank;
	IF aus = 1 THEN Country = 'Australia';
		ELSE IF bra = 1 THEN Country = 'Brazil';
		ELSE IF fra = 1 THEN Country = 'France';
		ELSE IF ind = 1 THEN Country = 'India';
		ELSE IF rus = 1 THEN Country = 'Russia';
		ELSE Country = 'USA';
RUN;

* e. state the number of observations and variables from the data set created in d.;
* There are 60 observations and 4 variables in work.interleaved2.