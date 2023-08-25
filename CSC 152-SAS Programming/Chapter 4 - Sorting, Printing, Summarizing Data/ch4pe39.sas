LIBNAME chap4 '~/sasuser.v94/Chapter4';
DATA gas;
	SET chap4.gas;
RUN;

* a. The label for GasPrice is "U.S. average price of unleaded regular gasoline(per gallon)".;
*    The variable type is numeric.;

* b.;
PROC MEANS MIN MAX DATA = gas MAXDEC = 2;
	CLASS Year;
	Var GasPrice;
	TITLE 'Minimum and Maximum Prices Per Year';
RUN;

* c.;
PROC FORMAT;
	VALUE quarter 1-3 = "Q1"
				  4-6 = "Q2"
				  7-9 = "Q3"
				  10-12 = "Q4";
RUN;				  

DATA gas;
	SET chap4.gas;
	Quarter = PUT(Month, quarter.);
	FORMAT GasPrice DOLLAR6.2;
RUN;
				  
* d.;
PROC MEANS MEAN STDDEV DATA = gas MAXDEC = 2;
	CLASS Year Quarter;
	Var GasPrice;
	TITLE 'Average Price and Standard Deviation of Price Per Quarter Per Year';
RUN;

* e.;
PROC MEANS MEAN STDDEV DATA = gas;
	CLASS Year Quarter;
	VAR GasPrice;
	OUTPUT OUT = gaspricedata
		MEAN(GasPrice) = AvgPrice
		STDDEV(GasPrice) = StdDev;
RUN;

PROC PRINT DATA = gaspricedata (firstobs= 22 obs = 85) NOOBS;
	TITLE 'Average Price and Standard Deviation of Price Per Quarter Per Year';
RUN;		
	
* The instructions say to only show the year, quarter, avg price, and stddev, but I can't figure out how to omit 
* the _TYPE_ and _FREQ_ columns. In the Instructor Recording, you note that they are automatically included, and
* my google skills apparently aren't good enough to find out how to get rid of them.