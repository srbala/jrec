useFixture(default)

def test():
	from Modules import commonBits
	if window('Record Layout Definitions'):
		click('*6')
		select('FileChooser', commonBits.cobolDir() + 'AmsLocation.cbl')
		click('Go')
		assert_p('TextArea', 'Text', '''

-->> ''' + commonBits.cobolDir() + '''AmsLocation.cbl processed

      Copybook: AmsLocation''')
		select_menu('Record Layouts>>Edit Layout')
		select('TextField', 'AmsLo%')
		select('TabbedPane', 'Extras')
		select('TextField1', '%')
		#select('TabbedPane', 'Fields')
		#select('TabbedPane', 'Extras')
		#select('TabbedPane', 'Fields')
		#assert_p('TextField2', 'Text', 'AmsLocation')
		select('RecordFieldsJTbl', 'cell:FieldName,0(Brand)')
		assert_p('RecordFieldsJTbl', 'Text', 'cell:FieldName,0(Brand)')
		select('RecordFieldsJTbl', 'cell:FieldName,1(Location-Number)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [85, 40, Address-2, , 0, 0, 0, , , Address-2], [125, 35, Address-3, , 0, 0, 0, , , Address-3], [160, 10, Postcode, , 25, 0, 0, , , Postcode], [170, 3, State, , 0, 0, 0, , , State], [173, 1, Location-Active, , 0, 0, 0, , , Location-Active]]')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Location-Type)')
		assert_p('RecordFieldsJTbl', 'RowCount', '10')
		select('RecordFieldsJTbl', 'rows:[2,3,4],columns:[FieldName]')
		rightclick('RecordFieldsJTbl', 'FieldName,3')
		select_menu('Copy Record#{s#}')
		select('RecordFieldsJTbl', 'cell:FieldName,9(Location-Active)')
		rightclick('RecordFieldsJTbl', 'FieldName,9')
		select_menu('Paste Record#{s#}')
		#click('WindowsScrollBarUI$WindowsArrowButton4')
		select('RecordFieldsJTbl', 'cell:FieldName,12(Address-1)')
		assert_p('RecordFieldsJTbl', 'RowCount', '13')
		select('RecordFieldsJTbl', 'cell:FieldName,10(Location-Type)')
		assert_p('RecordFieldsJTbl', 'Text', 'cell:FieldName,10(Location-Type)')
		select('RecordFieldsJTbl', 'cell:FieldName,9(Location-Active)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [85, 40, Address-2, , 0, 0, 0, , , Address-2], [125, 35, Address-3, , 0, 0, 0, , , Address-3], [160, 10, Postcode, , 25, 0, 0, , , Postcode], [170, 3, State, , 0, 0, 0, , , State], [173, 1, Location-Active, , 0, 0, 0, , , Location-Active], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'rows:[9,10,11],columns:[FieldName]')
		rightclick('RecordFieldsJTbl', 'FieldName,10')
		select_menu('Delete Record#{s#}')
		select('RecordFieldsJTbl', 'cell:FieldName,9(Address-1)')
		assert_p('RecordFieldsJTbl', 'RowCount', '10')
		select('RecordFieldsJTbl', 'cell:FieldName,6(Address-3)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [85, 40, Address-2, , 0, 0, 0, , , Address-2], [125, 35, Address-3, , 0, 0, 0, , , Address-3], [160, 10, Postcode, , 25, 0, 0, , , Postcode], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'rows:[1,2,3],columns:[FieldName]')
		rightclick('RecordFieldsJTbl', 'FieldName,2')
		select_menu('Cut Record#{s#}')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Address-2)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [85, 40, Address-2, , 0, 0, 0, , , Address-2], [125, 35, Address-3, , 0, 0, 0, , , Address-3], [160, 10, Postcode, , 25, 0, 0, , , Postcode], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,3(Address-3)')
		assert_p('RecordFieldsJTbl', 'RowCount', '7')
		select('RecordFieldsJTbl', 'cell:FieldName,5(State)')
		rightclick('RecordFieldsJTbl', 'FieldName,5')
		select_menu('Paste Record#{s#} Prior')
		select('RecordFieldsJTbl', 'cell:FieldName,4(Postcode)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [85, 40, Address-2, , 0, 0, 0, , , Address-2], [125, 35, Address-3, , 0, 0, 0, , , Address-3], [160, 10, Postcode, , 25, 0, 0, , , Postcode], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,5(Location-Number)')
		assert_p('RecordFieldsJTbl', 'Text', 'Location-Number', 'FieldName,5')
		select('RecordFieldsJTbl', 'cell:FieldName,6(Location-Type)')
		assert_p('RecordFieldsJTbl', 'RowCount', '10')
		select('RecordFieldsJTbl', 'rows:[2,3,4],columns:[FieldName]')
		click('Delete2')
		select('RecordFieldsJTbl', 'cell:FieldName,1(Address-1)')
		assert_p('RecordFieldsJTbl', 'RowCount', '7')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Location-Number)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Location-Number)')
		click('Insert')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Location-Number)')
		#keystroke('RecordFieldsJTbl', 'Ctrl+F9', 'FieldName,2')
		#click('BasicInternalFrameTitlePane$NoFocusButton9')
		select('RecordFieldsJTbl', 'cell:FieldName,4(Location-Type)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [0, 0, , , 0, 0, 0, , , ], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,5(Location-Name)')
		assert_p('RecordFieldsJTbl', 'RowCount', '8')
		select('RecordFieldsJTbl', 'cell:FieldName,3()')
		click('Delete2')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Location-Number)')
		assert_p('RecordFieldsJTbl', 'RowCount', '7')
		select('RecordFieldsJTbl', 'cell:FieldName,3(Location-Type)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'rows:[1,2,3],columns:[FieldName]')
		click('Cut2')
		select('RecordFieldsJTbl', 'cell:Length,2(3)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,1(Location-Name)')
		assert_p('RecordFieldsJTbl', 'RowCount', '4')
		select('RecordFieldsJTbl', 'cell:FieldName,2(State)')
		click('Paste2')
		select('RecordFieldsJTbl', 'cell:FieldName,2(State)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,4(Location-Number)')
		assert_p('RecordFieldsJTbl', 'RowCount', '7')
		select('RecordFieldsJTbl', 'rows:[3,4,5],columns:[FieldName]')
		click('Cut2')
		select('RecordFieldsJTbl', 'cell:FieldName,2(State)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 3, Brand, , 0, 0, 0, , , Brand], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,0(Brand)')
		click('Paste Prior')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Location-Type)')
		assert_p('RecordFieldsJTbl', 'Content', '[[45, 40, Address-1, , 0, 0, 0, , , Address-1], [4, 4, Location-Number, , 25, 0, 0, , , Location-Number], [8, 2, Location-Type, , 0, 0, 0, , , Location-Type], [1, 3, Brand, , 0, 0, 0, , , Brand], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,3(Brand)')
		assert_p('RecordFieldsJTbl', 'RowCount', '7')
		select('RecordFieldsJTbl', 'rows:[1,2,3],columns:[FieldName]')
		click('Delete2')
		select('RecordFieldsJTbl', 'cell:FieldName,0(Address-1)')
		click('Copy2')
		select('RecordFieldsJTbl', 'cell:FieldName,2(State)')
		click('Paste Prior')
		select('RecordFieldsJTbl', 'cell:FieldName,3(State)')
		assert_p('RecordFieldsJTbl', 'Content', '[[45, 40, Address-1, , 0, 0, 0, , , Address-1], [10, 35, Location-Name, , 0, 0, 0, , , Location-Name], [45, 40, Address-1, , 0, 0, 0, , , Address-1], [170, 3, State, , 0, 0, 0, , , State], [45, 40, Address-1, , 0, 0, 0, , , Address-1]]')
		select('RecordFieldsJTbl', 'cell:FieldName,2(Address-1)')
		assert_p('RecordFieldsJTbl', 'RowCount', '5')
		select('RecordFieldsJTbl', 'cell:FieldName,3(State)')
		click('Delete3')

		if window('Delete: AmsLocation'):
			click('Yes')
		close()

		#select('TabbedPane', 'Extras')
		#select('TabbedPane', 'Child Records')
		#select('TabbedPane', 'Extras')
		#select('TabbedPane', 'Child Records')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Close')

##		select_menu('File>>Exit')
	close()
