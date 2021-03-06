useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'zzzCsvTest5.csv')
		commonBits.setRecordLayout(select, 'zzzCsvTest5')

		click('Edit1')
		select('Table', 'cell:2|Array 1 (; and colon),0(22)')
		rightclick('Table', '1|Field 1,0')
		select_menu('Edit Record')
		select('Table', '111|11', 'Data,0')
		select('Table', 'cell:Text,0(111|11)')
		assert_p('Table', 'Text', '111|11', 'Text,0')
		select('Table', 'cell:Text,1(22)')
		assert_p('Table', 'Content', '[[Field 1, 1, , 111|11, 111|11], [Array 1 (; and colon), 2, , 22, 22], [Field 3, 3, , 33, 33], [Array 2 (;), 4, , 44, 44], [Field 5, 5, , 55, 55], [Array 3 (colon), 6, , 66, 66], [Field 7, 7, , 77, 77]]')
		select('Table', '111|', 'Data,0')
		select('Table', '111|', 'Data,0')
		select('Table', 'cell:Text,0(111|)')
		assert_p('Table', 'Text', '111|', 'Text,0')
		select('Table', '111\' 22', 'Data,0')
		select('Table', '111\' 22', 'Data,0')
		select('Table', 'cell:Text,0(111\' 22)')
		assert_p('Table', 'Text', 'cell:Text,0(111\' 22)')
		select('Table', '33|', 'Data,2')
		select('Table', '33|', 'Data,2')
		select('Table', 'cell:Text,2(33|)')
		assert_p('Table', 'Text', '33|', 'Text,2')
		select('Table', 'cell:Text,3(44)')
		assert_p('Table', 'Content', '[[Field 1, 1, , 111\' 22, 111\' 22], [Array 1 (; and colon), 2, , 22, 22], [Field 3, 3, , 33|, 33|], [Array 2 (;), 4, , 44, 44], [Field 5, 5, , 55, 55], [Array 3 (colon), 6, , 66, 66], [Field 7, 7, , 77, 77]]')
		select('Table', 'cell:Text,3(44)')
		click('TextArea')
		assert_p('TextArea', 'Text', '111\' 22|22|\'33|\'|44|55|66|77')
		select('Table', '55|66|', 'Data,4')
		select('Table', 'cell:Text,4(55|66|)')
		assert_p('Table', 'Text', '55|66|', 'Text,4')
		select('Table', 'cell:Text,4(55|66|)')
		click('TextArea')
		assert_p('TextArea', 'Text', '111\' 22|22|\'33|\'|44|\'55|66|\'|66|77')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('LayoutCombo', 'Full Line')
		select('Table', 'cell:Full Line,0(111\' 22|22|\'33|\'|44|\'55|66|\'|66|77)')
		assert_p('Table', 'Text', '111\' 22|22|\'33|\'|44|\'55|66|\'|66|77', 'Full Line,0')
		select('Table', 'cell:Full Line,1(1|2;3;4:1;2;3;4:4;5;6|333|2;3;4;5;6|555|1:2:3|777)')
		assert_p('Table', 'Content', '[[111\' 22|22|\'33|\'|44|\'55|66|\'|66|77], [1|2;3;4:1;2;3;4:4;5;6|333|2;3;4;5;6|555|1:2:3|777], [111|22|33|44|55|66|77], [1|2;3;4:1;2;3;4:4;5;6|333|2;3;4;5;6|555|1:2:3|777]]')
		select('Table', 'cell:Full Line,1(1|2;3;4:1;2;3;4:4;5;6|333|2;3;4;5;6|555|1:2:3|777)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'zzzCsvTest5.csv'):
			click('No')
		close()
	close()
