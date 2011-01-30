useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_03'

	if window('Record Editor'):
		click('Choose File')

		if window('Open'):
			select(commonBits.selectPane(), 'Ams_LocDownload_20041228.txt')
			click('Open')
		close()

		click('Edit1')
		click('Filter')
		select('Table1', 'Loc Type', 'Field,0')
		select('Table1', 'st', 'Value,0')
		select('Table1', 'cell:Field,2(null)')
		click('Save1')
		#select('FileChooser', commonBits.userDir() + 'Filter' + commonBits.fileSep() + 'xx1')
		commonBits.selectFileName(select, commonBits.userDir() + 'Filter' + commonBits.fileSep() + 'xx1')

		click('Save1')
		select_menu('Window>>Ams_LocDownload_20041228.txt>>Filter Options')
		click('Filter1')
		select('Table', 'cell:10 - 35|Loc Name,0(Bankstown)')
		assert_p('Table', 'Text', 'Bankstown', '10 - 35|Loc Name,0')
		select('Table', 'cell:8 - 2|Loc Type,1(ST)')
		rightclick('Table', '8 - 2|Loc Type,1')
		select_menu('Edit Record')
##		select('Table1', 'cell:8 - 2|Loc Type,1(ST)')
		select('Table', 'cell:Data,5(58 Leland Street)')
		assert_p('Table', 'Text', 'Penrith', 'Data,6')
		select('Table', 'cell:Data,5(58 Leland Street)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5019, 5019], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Penrith, Penrith], [Loc Addr Ln1, 45, 40, Penrith, Penrith], [Loc Addr Ln2, 85, 40, 58 Leland Street, 58 Leland Street], [Loc Addr Ln3, 125, 35, Penrith, Penrith], [Loc Postcode, 160, 10, 2750, 2750], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(58 Leland Street)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:8 - 2|Loc Type,1(ST)')
		select('Table', 'cell:8 - 2|Loc Type,1(ST)')
		select_menu('Window>>Ams_LocDownload_20041228.txt>>Table: ')
		select('Table2', 'cell:8 - 2|Loc Type,1(ST)')
		select_menu('View>>Execute Saved Filter')
		##select('FileChooser', commonBits.userDir() + 'Filter'  + commonBits.fileSep() +'xx1')
		commonBits.selectFileName(select, commonBits.userDir() + 'Filter' + commonBits.fileSep() + 'xx1')
		click('Run')
		select('Table', 'cell:10 - 35|Loc Name,2(Blacktown)')
		assert_p('Table', 'Text', 'Blacktown', '10 - 35|Loc Name,2')
		select('Table', 'cell:10 - 35|Loc Name,5(Eastwood)')
		rightclick('Table', '10 - 35|Loc Name,5')
		select_menu('Edit Record')
##		select('Table1', 'cell:10 - 35|Loc Name,5(Eastwood)')
		select('Table', 'cell:Data,4(Marayong Offsite Reserve)')
		assert_p('Table', 'Text', 'Marayong Offsite Reserve', 'Data,4')
		select('Table', 'cell:Data,4(Marayong Offsite Reserve)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5052, 5052], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastwood, Eastwood], [Loc Addr Ln1, 45, 40, Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc Addr Ln2, 85, 40, 11 Melissa Place, 11 Melissa Place], [Loc Addr Ln3, 125, 35, Marayong, Marayong], [Loc Postcode, 160, 10, 2148, 2148], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
	close()
