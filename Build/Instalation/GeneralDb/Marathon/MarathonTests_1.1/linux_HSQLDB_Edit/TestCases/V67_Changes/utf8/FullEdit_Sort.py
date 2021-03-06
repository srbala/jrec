useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'utf8a_Ams_LocDownload_20041228.txt')
		commonBits.setRecordLayout(select, 'utf8_ams Store')
		click('Edit1')
		click('Filter1')
		click('Filter1')
		select('Table', 'cell:10 - 35|Loc Name,1(VIC West Ad Support)')
		assert_p('Table', 'Text', 'VIC West Ad Support', '10 - 35|Loc Name,1')
		select('Table', 'cell:10 - 35|Loc Name,1(VIC West Ad Support)')
		select_menu('Data>>Sort')
#		select('Table1', 'cell:10 - 35|Loc Name,1(VIC West Ad Support)')
#		select('List', 'utf8_ams Store')
		select('Table', 'cell:Field,0( )')
		click('ScrollPane$ScrollBar', 9, 108)
		select('Table', 'Loc State', 'Field,0')
		select('Table', 'Loc Nbr', 'Field,1')
		select('Table', 'cell:Field,1(Loc Nbr)')
		click('Sort1')
		select('Table', 'cell:10 - 35|Loc Name,0(National Ad Support)')
		assert_p('Table', 'Text', 'cell:10 - 35|Loc Name,0(National Ad Support)')
		select('Table', 'cell:10 - 35|Loc Name,12(Canberra Civic)')
		assert_p('Table', 'Text', 'cell:10 - 35|Loc Name,12(Canberra Civic)')
		select('Table', 'cell:10 - 35|Loc Name,12(Canberra Civic)')
		rightclick('Table', '10 - 35|Loc Name,12')
		select_menu('Edit Record')
		select('Table', 'cell:Data,2(ST)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5096, 5096], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Canberra Civic, Canberra Civic], [Loc Addr Ln1, 45, 40, Target Canberra, Target Canberra], [Loc Addr Ln2, 85, 40, Canberra City Centre, Akuna Ave, Canberra City Centre, Akuna Ave], [Loc Addr Ln3, 125, 35, Canberra, Canberra], [Loc Postcode, 160, 10, 2601, 2601], [Loc State, 170, 3, ACT, ACT]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5096, 5096], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Canberra Civic, Canberra Civic], [Loc Addr Ln1, 45, 40, Target Canberra, Target Canberra], [Loc Addr Ln2, 85, 40, Canberra City Centre, Akuna Ave, Canberra City Centre, Akuna Ave], [Loc Addr Ln3, 125, 35, Canberra, Canberra], [Loc Postcode, 160, 10, 2601, 2601], [Loc State, 170, 3, ACT, ACT], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,2(ST)')
		click('Right')
		select('Table', 'cell:Data,4(Coffs Harbour)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5002, 5002], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Coffs Harbour, Coffs Harbour], [Loc Addr Ln1, 45, 40, Coffs Harbour, Coffs Harbour], [Loc Addr Ln2, 85, 40, Cnr. Park Beach Road & Pacific Hwy, Cnr. Park Beach Road & Pacific Hwy], [Loc Addr Ln3, 125, 35, Coffs Harbour, Coffs Harbour], [Loc Postcode, 160, 10, 2450, 2450], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5002, 5002], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Coffs Harbour, Coffs Harbour], [Loc Addr Ln1, 45, 40, Coffs Harbour, Coffs Harbour], [Loc Addr Ln2, 85, 40, Cnr. Park Beach Road & Pacific Hwy, Cnr. Park Beach Road & Pacific Hwy], [Loc Addr Ln3, 125, 35, Coffs Harbour, Coffs Harbour], [Loc Postcode, 160, 10, 2450, 2450], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,4(Coffs Harbour)')
		click('Right')
		select('Table', 'cell:Data,4(Albury)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5005, 5005], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Albury, Albury], [Loc Addr Ln1, 45, 40, Albury, Albury], [Loc Addr Ln2, 85, 40, Kiewa Street, Kiewa Street], [Loc Addr Ln3, 125, 35, Albury, Albury], [Loc Postcode, 160, 10, 2640, 2640], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5005, 5005], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Albury, Albury], [Loc Addr Ln1, 45, 40, Albury, Albury], [Loc Addr Ln2, 85, 40, Kiewa Street, Kiewa Street], [Loc Addr Ln3, 125, 35, Albury, Albury], [Loc Postcode, 160, 10, 2640, 2640], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,4(Albury)')
		click('RightM')
		select('Table', 'cell:Data,5(Cnr Nicholson & Bannister Rd\'s)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5965, 5965], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, Canning Vale DC, Canning Vale DC], [Loc Addr Ln1, 45, 40, Canning Vale DC, Canning Vale DC], [Loc Addr Ln2, 85, 40, Cnr Nicholson & Bannister Rd\'s, Cnr Nicholson & Bannister Rd\'s], [Loc Addr Ln3, 125, 35, Canning Vale, Canning Vale], [Loc Postcode, 160, 10, 6155, 6155], [Loc State, 170, 3, WA, WA]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5965, 5965], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, Canning Vale DC, Canning Vale DC], [Loc Addr Ln1, 45, 40, Canning Vale DC, Canning Vale DC], [Loc Addr Ln2, 85, 40, Cnr Nicholson & Bannister Rd\'s, Cnr Nicholson & Bannister Rd\'s], [Loc Addr Ln3, 125, 35, Canning Vale, Canning Vale], [Loc Postcode, 160, 10, 6155, 6155], [Loc State, 170, 3, WA, WA], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Cnr Nicholson & Bannister Rd\'s)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:10 - 35|Loc Name,12(Canberra Civic)')
		rightclick('Table', '10 - 35|Loc Name,4')
		select_menu('Sort')
#		select('List', 'utf8_ams Store')
		select('Table', 'Loc Type', 'Field,0')
		select('Table', 'Loc Nbr', 'Field,1')
		select('Table', 'cell:Field,1(Loc Nbr)')
		click('Sort1')
		select('Table', 'cell:10 - 35|Loc Name,0(National Ad Support)')
		assert_p('Table', 'Text', 'National Ad Support', '10 - 35|Loc Name,0')
		select('Table', 'cell:10 - 35|Loc Name,0(National Ad Support)')
		rightclick('Table', '10 - 35|Loc Name,0')
		select_menu('Edit Record')
##		select('Table1', 'cell:10 - 35|Loc Name,0(National Ad Support)')
		select('Table', 'cell:Data,3(National Ad Support)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5109, 5109], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, National Ad Support, National Ad Support], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, , ], [Loc Addr Ln3, 125, 35, , ], [Loc Postcode, 160, 10, , ], [Loc State, 170, 3, , ]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5109, 5109], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, National Ad Support, National Ad Support], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, , ], [Loc Addr Ln3, 125, 35, , ], [Loc Postcode, 160, 10, , ], [Loc State, 170, 3, , ], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,3(National Ad Support)')
		click('Right')
		select('Table', 'cell:Data,3(Head Office)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5700, 5700], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, Head Office, Head Office], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, , ], [Loc Addr Ln3, 125, 35, , ], [Loc Postcode, 160, 10, , ], [Loc State, 170, 3, , ]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5700, 5700], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, Head Office, Head Office], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, , ], [Loc Addr Ln3, 125, 35, , ], [Loc Postcode, 160, 10, , ], [Loc State, 170, 3, , ], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,3(Head Office)')
		click('Right')
		select('Table', 'cell:Data,5(30-68 Taras Ave)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5839, 5839], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, DC - Taras Ave, DC - Taras Ave], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, 30-68 Taras Ave, 30-68 Taras Ave], [Loc Addr Ln3, 125, 35, Altona North, Altona North], [Loc Postcode, 160, 10, 3025, 3025], [Loc State, 170, 3, VIC, VIC]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5839, 5839], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, DC - Taras Ave, DC - Taras Ave], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, 30-68 Taras Ave, 30-68 Taras Ave], [Loc Addr Ln3, 125, 35, Altona North, Altona North], [Loc Postcode, 160, 10, 3025, 3025], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(30-68 Taras Ave)')
		click('Right')
		click('Right')
		click('Right')
		click('Right')
		click('Right')
		click('Right')
		click('Right')
		select('Table', 'cell:Data,4(No 2 Sydney Gate)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5897, 5897], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, Sydney Gate DC, Sydney Gate DC], [Loc Addr Ln1, 45, 40, No 2 Sydney Gate, No 2 Sydney Gate], [Loc Addr Ln2, 85, 40, 830 Bourke Street, 830 Bourke Street], [Loc Addr Ln3, 125, 35, Waterloo, Waterloo], [Loc Postcode, 160, 10, 2017, 2017], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5897, 5897], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, Sydney Gate DC, Sydney Gate DC], [Loc Addr Ln1, 45, 40, No 2 Sydney Gate, No 2 Sydney Gate], [Loc Addr Ln2, 85, 40, 830 Bourke Street, 830 Bourke Street], [Loc Addr Ln3, 125, 35, Waterloo, Waterloo], [Loc Postcode, 160, 10, 2017, 2017], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,4(No 2 Sydney Gate)')
		click('RightM')
		select('Table', 'cell:Data,5(Cnr Grove Way & Golden Grove)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5305, 5305], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Golden Grove, Golden Grove], [Loc Addr Ln1, 45, 40, The Golden Way, The Golden Way], [Loc Addr Ln2, 85, 40, Cnr Grove Way & Golden Grove, Cnr Grove Way & Golden Grove], [Loc Addr Ln3, 125, 35, Golden Grove, Golden Grove], [Loc Postcode, 160, 10, 5125, 5125], [Loc State, 170, 3, SOU, SOU]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5305, 5305], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Golden Grove, Golden Grove], [Loc Addr Ln1, 45, 40, The Golden Way, The Golden Way], [Loc Addr Ln2, 85, 40, Cnr Grove Way & Golden Grove, Cnr Grove Way & Golden Grove], [Loc Addr Ln3, 125, 35, Golden Grove, Golden Grove], [Loc Postcode, 160, 10, 5125, 5125], [Loc State, 170, 3, SOU, SOU], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Cnr Grove Way & Golden Grove)')
		click('Left')
		select('Table', 'cell:Data,5(2-50 Murray Road)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5304, 5304], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Northland Baby Target, Northland Baby Target], [Loc Addr Ln1, 45, 40, Northland Shopping Centre, Northland Shopping Centre], [Loc Addr Ln2, 85, 40, 2-50 Murray Road, 2-50 Murray Road], [Loc Addr Ln3, 125, 35, East  Preston, East  Preston], [Loc Postcode, 160, 10, 3072, 3072], [Loc State, 170, 3, VIC, VIC]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5304, 5304], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Northland Baby Target, Northland Baby Target], [Loc Addr Ln1, 45, 40, Northland Shopping Centre, Northland Shopping Centre], [Loc Addr Ln2, 85, 40, 2-50 Murray Road, 2-50 Murray Road], [Loc Addr Ln3, 125, 35, East  Preston, East  Preston], [Loc Postcode, 160, 10, 3072, 3072], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(2-50 Murray Road)')
		click('Left')
		select('Table', 'cell:Data,5(Gilchrist Drive)')
		assert_p('Table', 'Text', 'Gilchrist Drive', 'Data,5')
		select('Table', 'cell:Data,5(Gilchrist Drive)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5303, 5303], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Macarthur Square, Macarthur Square], [Loc Addr Ln1, 45, 40, Macarthur Square, Macarthur Square], [Loc Addr Ln2, 85, 40, Gilchrist Drive, Gilchrist Drive], [Loc Addr Ln3, 125, 35, Campbelltown, Campbelltown], [Loc Postcode, 160, 10, 2560, 2560], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5303, 5303], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Macarthur Square, Macarthur Square], [Loc Addr Ln1, 45, 40, Macarthur Square, Macarthur Square], [Loc Addr Ln2, 85, 40, Gilchrist Drive, Gilchrist Drive], [Loc Addr Ln3, 125, 35, Campbelltown, Campbelltown], [Loc Postcode, 160, 10, 2560, 2560], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Gilchrist Drive)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
