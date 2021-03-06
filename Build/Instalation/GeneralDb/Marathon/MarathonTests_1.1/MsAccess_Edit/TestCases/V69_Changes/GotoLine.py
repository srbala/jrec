useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_LocDownload_20041228.txt')
		click(commonBits.fl('Edit') + '1')
		select('Table', 'cell:4 - 4|Loc Nbr,0(5839)')
		rightclick('Table', '4 - 4|Loc Nbr,5')
#		select('Table', 'cell:4 - 4|Loc Nbr,0(5839)')
		select_menu( commonBits.fl('Edit Record'))
##		select('Table1', 'cell:4 - 4|Loc Nbr,0(5839)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5019, 5019], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Penrith, Penrith], [Loc Addr Ln1, 45, 40, Penrith, Penrith], [Loc Addr Ln2, 85, 40, 58 Leland Street, 58 Leland Street], [Loc Addr Ln3, 125, 35, Penrith, Penrith], [Loc Postcode, 160, 10, 2750, 2750], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		assert_p('TextField', 'Text', '6')
#		select('Table', '')
		rightclick('Table', commonBits.fl('Data') + ',4')
##		zzz
		select_menu(commonBits.fl('Goto Line'))
		select('TextField', '20')
		click(commonBits.fl('Goto'))
		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Record:'))
		assert_p('JTableHeader', 'Text',  commonBits.fl('Field'),  commonBits.fl('Field'))
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, Westfield Phoenix Plaza, Westfield Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
##		select('Table', '')
		rightclick('Table', commonBits.fl('Data') + ',4')
		select_menu(commonBits.fl('Goto Line'))
		select('TextField', '35')
		click(commonBits.fl('Goto'))
		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Record:'))
		assert_p('TextField', 'Text', '35')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5011, 5011], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Cessnock, Cessnock], [Loc Addr Ln1, 45, 40, Cessnock City Centre, Cessnock City Centre], [Loc Addr Ln2, 85, 40, Cnr. North Avenue & Darwin Street, Cnr. North Avenue & Darwin Street], [Loc Addr Ln3, 125, 35, Cessnock, Cessnock], [Loc Postcode, 160, 10, 2325, 2325], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Table:'))
		select('Table', 'cell:4 - 4|Loc Nbr,0(5839)')
		select('Table', 'cell:4 - 4|Loc Nbr,0(5839)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
