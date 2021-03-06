useFixture(RecordEditor)

def test():
	from Modules import commonBits

	java_recorded_version = '1.6.0_03'

	if window('Record Editor'):
		click(commonBits.fl('Choose File'))

		if window('Open'):
			select(commonBits.selectPane(), 'Ams_LocDownload_20041228.txt')
			click('Open')
		close()

		commonBits.setRecordLayout(select, 'ams Store')

		click(commonBits.fl('Edit') + '1')
##		select('Table', 'rows:[0,1,2,3,4,5],columns:[4 - 4|Loc Nbr,8 - 2|Loc Type]')
		select('Table', 'rows:[0,1,2,3,4,5],columns:[8 - 2|Loc Type]')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Column View #{Selected Records#}'))
##		select('Table2', 'rows:[0,1,2,3,4,5],columns:[4 - 4|Loc Nbr,8 - 2|Loc Type]')
		select('Table', 'cell:Row 1,0(TAR)')
		assert_p('Table1', 'Text', '3', commonBits.fl('Len') + ',0')
		select('Table', 'cell:Row 1,1(5839)')
		assert_p('Table', 'Content', '[[TAR, TAR, TAR, TAR, TAR, TAR], [5839, 5850, 5853, 5866, 5015, 5019], [DC, DC, DC, DC, ST, ST], [DC - Taras Ave, VIC West Ad Support, NSW North Sydney Ad Support, WA Ad Support, Bankstown, Penrith], [, , , , Bankstown, Penrith], [30-68 Taras Ave, Lot 2 Little Boundary Rd, , , Unit 2, 39-41 Allingham Street, 58 Leland Street], [Altona North, Laverton, , , Condell Park, Penrith], [3025, 3028, , , 2200, 2750], [VIC, VIC, , , NSW, NSW], [A, A, A, A, A, A]]')
		select('Table', 'cell:Row 1,1(5839)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'rows:[0,1,2,3,4,5],columns:[4 - 4|Loc Nbr,8 - 2|Loc Type]')
		select('Table', 'rows:[8,11,15],columns:[4 - 4|Loc Nbr,8 - 2|Loc Type]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
