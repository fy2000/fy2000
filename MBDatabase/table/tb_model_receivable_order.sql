CREATE TABLE tb_model_receivable_order ( 
	iindex INTEGER NOT NULL DEFAULT 1 PRIMARY KEY AUTOINCREMENT UNIQUE, 
	strdocumenttype TEXT NOT NULL,
	strdocumentcode TEXT NOT NULL,
	strstartdate TEXT NOT NULL,
	strcustomer TEXT NOT NULL,
	strcurrencytypes TEXT NOT NULL,
	rtotalpriceincludtax REAL,
	strsettlementunit TEXT,
	strsalesunit TEXT,
	strdocumentstatus TEXT,
	strlastday TEXT,
	strsalesmen TEXT,
	strmaterielcode TEXT,
	strmaterielname TEXT,
	strpriceunit TEXT,
	rquantity REAL,
	runitpriceincludtax REAL,
	runitprice REAL,
	strtaxmix TEXT,
	rtaxrate REAL,
	rdiscountrate REAL,
	rtotalprice REAL,
	rdiscountprice REAL,
	rtaxprice REAL,
	rtotalpricetax REAL,
	rbasicquantity REAL,
	rtotalprice_rmb REAL,
	rinvoiceamount REAL,
	strordernumber TEXT,
	strpayee TEXT,
	strbusinessstype TEXT,
	strcostbearingDepartment TEXT,
	strgift TEXT,
	strinventoryunit TEXT,
	rinventoryquantity REAL,
	rbaseinventoryquantity REAL,
	rcost REAL,
	rSettledamount REAL,
	strcustomercode TEXT,
	strproductioncode TEXT
)