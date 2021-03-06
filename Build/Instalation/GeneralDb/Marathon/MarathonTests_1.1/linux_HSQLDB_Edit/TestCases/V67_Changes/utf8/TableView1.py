useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'utf8a_Ams_LocDownload_20041228.txt')
		commonBits.setRecordLayout(select, 'utf8_ams Store')
		click('Edit1')
		select('Table', 'rows:[0,4,8,13,18,23,27],columns:[10 - 35|Loc Name]')
		select_menu('View>>Table View #{Selected Records#}')
##		select('Table2', 'rows:[0,4,8,13,18,23,27],columns:[10 - 35|Loc Name]')
		select('Table', 'cell:8 - 2|Loc Type,1(ST)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[TAR, 5839, DC, DC - Taras Ave, , 30-68 Taras Ave, Altona North, 3025, VIC], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW], [TAR, 5074, ST, Campbelltown, Campbelltown Mall, 303 Queen Street, Campbelltown, 2560, NSW], [TAR, 5091, ST, Chatswood, Frenchs Forest, Unit 2-3, 14 Aquatic Drive, Frenchs Forest, 2086, NSW], [TAR, 5157, ST, Chirnside Park, Kilsyth South, Lot 3 & 4 Southfork Drive, Kilsyth Park, 3137, VIC], [TAR, 5170, ST, Bondi, Building B, Portside Distribution Centre, 2-8 McPherson Street, Botany, 2019, NSW]]')
		else:
			assert_p('Table', 'Content', '[[TAR, 5839, DC, DC - Taras Ave, , 30-68 Taras Ave, Altona North, 3025, VIC, A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5074, ST, Campbelltown, Campbelltown Mall, 303 Queen Street, Campbelltown, 2560, NSW, A], [TAR, 5091, ST, Chatswood, Frenchs Forest, Unit 2-3, 14 Aquatic Drive, Frenchs Forest, 2086, NSW, A], [TAR, 5157, ST, Chirnside Park, Kilsyth South, Lot 3 & 4 Southfork Drive, Kilsyth Park, 3137, VIC, A], [TAR, 5170, ST, Bondi, Building B, Portside Distribution Centre, 2-8 McPherson Street, Botany, 2019, NSW, A]]')
		select('Table', 'cell:10 - 35|Loc Name,3(Campbelltown)')
		assert_p('Table', 'Text', 'Campbelltown', '10 - 35|Loc Name,3')
		select('Table', 'cell:10 - 35|Loc Name,1(Bankstown)')
		rightclick('Table', '10 - 35|Loc Name,1')
		select_menu('Edit Record')
##		select('Table1', 'cell:10 - 35|Loc Name,1(Bankstown)')
		select('Table', 'cell:Data,4(Bankstown)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5015, 5015], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Bankstown, Bankstown], [Loc Addr Ln1, 45, 40, Bankstown, Bankstown], [Loc Addr Ln2, 85, 40, Unit 2, 39-41 Allingham Street, Unit 2, 39-41 Allingham Street], [Loc Addr Ln3, 125, 35, Condell Park, Condell Park], [Loc Postcode, 160, 10, 2200, 2200], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5015, 5015], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Bankstown, Bankstown], [Loc Addr Ln1, 45, 40, Bankstown, Bankstown], [Loc Addr Ln2, 85, 40, Unit 2, 39-41 Allingham Street, Unit 2, 39-41 Allingham Street], [Loc Addr Ln3, 125, 35, Condell Park, Condell Park], [Loc Postcode, 160, 10, 2200, 2200], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,4(Bankstown)')
		click('RightM')
		select('Table', 'cell:Data,4(Building B, Portside Distribution Centre)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5170, 5170], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Bondi, Bondi], [Loc Addr Ln1, 45, 40, Building B, Portside Distribution Centre, Building B, Portside Distribution Centre], [Loc Addr Ln2, 85, 40, 2-8 McPherson Street, 2-8 McPherson Street], [Loc Addr Ln3, 125, 35, Botany, Botany], [Loc Postcode, 160, 10, 2019, 2019], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5170, 5170], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Bondi, Bondi], [Loc Addr Ln1, 45, 40, Building B, Portside Distribution Centre, Building B, Portside Distribution Centre], [Loc Addr Ln2, 85, 40, 2-8 McPherson Street, 2-8 McPherson Street], [Loc Addr Ln3, 125, 35, Botany, Botany], [Loc Postcode, 160, 10, 2019, 2019], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,4(Building B, Portside Distribution Centre)')
		click('LeftM')
		select('Table', 'cell:Data,5(30-68 Taras Ave)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5839, 5839], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, DC - Taras Ave, DC - Taras Ave], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, 30-68 Taras Ave, 30-68 Taras Ave], [Loc Addr Ln3, 125, 35, Altona North, Altona North], [Loc Postcode, 160, 10, 3025, 3025], [Loc State, 170, 3, VIC, VIC]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5839, 5839], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, DC - Taras Ave, DC - Taras Ave], [Loc Addr Ln1, 45, 40, , ], [Loc Addr Ln2, 85, 40, 30-68 Taras Ave, 30-68 Taras Ave], [Loc Addr Ln3, 125, 35, Altona North, Altona North], [Loc Postcode, 160, 10, 3025, 3025], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(30-68 Taras Ave)')
		click('RightM')
		click('Left')
		select('Table', 'cell:Data,5(Lot 3 & 4 Southfork Drive)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5157, 5157], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Chirnside Park, Chirnside Park], [Loc Addr Ln1, 45, 40, Kilsyth South, Kilsyth South], [Loc Addr Ln2, 85, 40, Lot 3 & 4 Southfork Drive, Lot 3 & 4 Southfork Drive], [Loc Addr Ln3, 125, 35, Kilsyth Park, Kilsyth Park], [Loc Postcode, 160, 10, 3137, 3137], [Loc State, 170, 3, VIC, VIC]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5157, 5157], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Chirnside Park, Chirnside Park], [Loc Addr Ln1, 45, 40, Kilsyth South, Kilsyth South], [Loc Addr Ln2, 85, 40, Lot 3 & 4 Southfork Drive, Lot 3 & 4 Southfork Drive], [Loc Addr Ln3, 125, 35, Kilsyth Park, Kilsyth Park], [Loc Postcode, 160, 10, 3137, 3137], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Lot 3 & 4 Southfork Drive)')
		click('Left')
		select('Table', 'cell:Data,5(Unit 2-3, 14 Aquatic Drive)')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5091, 5091], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Chatswood, Chatswood], [Loc Addr Ln1, 45, 40, Frenchs Forest, Frenchs Forest], [Loc Addr Ln2, 85, 40, Unit 2-3, 14 Aquatic Drive, Unit 2-3, 14 Aquatic Drive], [Loc Addr Ln3, 125, 35, Frenchs Forest, Frenchs Forest], [Loc Postcode, 160, 10, 2086, 2086], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5091, 5091], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Chatswood, Chatswood], [Loc Addr Ln1, 45, 40, Frenchs Forest, Frenchs Forest], [Loc Addr Ln2, 85, 40, Unit 2-3, 14 Aquatic Drive, Unit 2-3, 14 Aquatic Drive], [Loc Addr Ln3, 125, 35, Frenchs Forest, Frenchs Forest], [Loc Postcode, 160, 10, 2086, 2086], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
	close()
