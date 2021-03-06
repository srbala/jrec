useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'zzzCsvTest4.csv')
		commonBits.setRecordLayout(select, 'zzzCsvTest4')
		click(commonBits.fl('Edit') + '1')
		select('Table', 'cell:1|Field 1,0(111)')
		assert_p('Table', 'Content', '[[111, 22, 33, 44, 55, 66, 77], [1, 2;3;4|1;2;3;4|4;5;6, 333, 2;3;4;5;6, 555, 1:2:3, 1|33|33|11], [111, 22, 33, 44, 55, 66, 1|2|1], [1, 2;3;4|1;2;3;4|4;5;6, 333, 2;3;4;5;6, 555, 1:2:3, 11|2|11]]')
		select('Table', 'cell:3|Field 3,1(333)')
		assert_p('Table', 'Text', '333', '3|Field 3,1')
		select('Table', 'cell:3|Field 3,1(333)')
		select('LayoutCombo', commonBits.fl('Full Line'))
		#select('Table', 'cell:' + commonBits.fl('Full Line') + ',1(1"2;3;4|1;2;3;4|4;5;6"3332;3;4;5;65551:2:3"1|33|33|11")')
		#assert_p('Table', 'Content', '[[111223344556677], [1"2;3;4|1;2;3;4|4;5;6"3332;3;4;5;65551:2:3"1|33|33|11"], [1112233445566"1|2|1"], [1"2;3;4|1;2;3;4|4;5;6"3332;3;4;5;65551:2:3"11|2|11"]]')
		#select('Table', 'cell:' + commonBits.fl('Full Line') + ',3(1"2;3;4|1;2;3;4|4;5;6"3332;3;4;5;65551:2:3"11|2|11")')
		#assert_p('Table', 'Text', '1"2;3;4|1;2;3;4|4;5;6"3332;3;4;5;65551:2:3"11|2|11"', 'Full Line,3')
		select('Table', 'cell:' + commonBits.fl('Full Line') + ',3(1"2;3;4|1;2;3;4|4;5;6"3332;3;4;5;65551:2:3"11|2|11")')
		select('LayoutCombo', 'zzzCsvTest4')
		#select('Table', '')
		rightclick('Table', '1|Field 1,0')
		select_menu(commonBits.fl('Edit Record'))
		select('Table', 'cell:' + commonBits.fl('Text') + ',0(111)')
		assert_p('Table', 'Text', '111', commonBits.fl('Text') + ',0')
		select('Table', 'cell:' + commonBits.fl('Text') + ',1(22)')
		assert_p('Table', 'Content', '[[Field 1, 1, , 111, 111], [Array 1 (; and |), 2, , 22, 22], [Field 3, 3, , 33, 33], [Array 2 (;), 4, , 44, 44], [Field 5, 5, , 55, 55], [Array 3 (:), 6, , 66, 66], [Array 4 (|), 7, , 77, 77]]')
		select('Table', 'cell:' + commonBits.fl('Text') + ',1(22)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Text') + ',1(2;3;4|1;2;3;4|4;5;6)')
		assert_p('Table', 'Text', '1', commonBits.fl('Text') + ',0')
		select('Table', 'cell:' + commonBits.fl('Text') + ',2(333)')
		assert_p('Table', 'Content', '[[Field 1, 1, , 1, 1], [Array 1 (; and |), 2, , 2;3;4|1;2;3;4|4;5;6, 2;3;4|1;2;3;4|4;5;6], [Field 3, 3, , 333, 333], [Array 2 (;), 4, , 2;3;4;5;6, 2;3;4;5;6], [Field 5, 5, , 555, 555], [Array 3 (:), 6, , 1:2:3, 1:2:3], [Array 4 (|), 7, , 1|33|33|11, 1|33|33|11]]')
		select('Table', 'cell:' + commonBits.fl('Text') + ',2(333)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
