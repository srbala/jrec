useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'DTAR020.bin')
		commonBits.doEdit(click)

		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Sorted Field Tree'))
#		select('List', 'DTAR020')
		select('Table', 'STORE-NO', commonBits.fl('Field') + ',0')
		select('Table', 'DEPT-NO', commonBits.fl('Field') + ',1')
		select('Table', 'cell:' + commonBits.fl('Field') + ',1(DEPT-NO)')
		click(commonBits.fl('Build Tree'))
		select('JTreeTable', 'cell:KEYCODE-NO,0(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,0')
		select_menu(commonBits.fl('Copy Record#{s#}'))
		select('JTreeTable', 'cell:KEYCODE-NO,2(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,2')
		select_menu(commonBits.fl('Paste Record#{s#} Prior'))
		select('JTreeTable', 'cell:KEYCODE-NO,2(null)')
		assert_p('JTreeTable', 'RowCount', '5')
		select('JTreeTable', 'cell:KEYCODE-NO,2(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,2')
		select_menu(commonBits.fl('Expand Tree'))
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',5(null)')
		assert_p('JTreeTable', 'RowCount', '10')
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',3(null)')
		rightclick('JTreeTable', commonBits.fl('Tree') + ',3')
		select_menu(commonBits.fl('Expand Tree'))
		select('JTreeTable', 'cell:KEYCODE-NO,4(63604808)')
		assert_p('JTreeTable', 'Text', '63604808', 'KEYCODE-NO,4')
		select('JTreeTable', 'cell:STORE-NO,4(20)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',8(null)')
		rightclick('JTreeTable', commonBits.fl('Tree') + ',8')
		select_menu(commonBits.fl('Expand Tree'))
		select('JTreeTable', 'cell:KEYCODE-NO,10(66624458)')
		assert_p('JTreeTable', 'Text', '66624458', 'KEYCODE-NO,10')
		select('JTreeTable', 'cell:KEYCODE-NO,11(63674861)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 64634429, 20, 40118, 957, 1, 3.99], [, , 66624458, 20, 40118, 957, 1, 0.89], [, , 63674861, 20, 40118, 957, 10, 2.70], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',6(null)')
		rightclick('JTreeTable', commonBits.fl('Tree') + ',6')
		select_menu(commonBits.fl('Expand Tree'))
		select('JTreeTable', 'cell:KEYCODE-NO,7(62684671)')
		assert_p('JTreeTable', 'Text', '62684671', 'KEYCODE-NO,7')
		select('JTreeTable', 'cell:KEYCODE-NO,8(62684671)')
		rightclick('JTreeTable', 'KEYCODE-NO,8')
		select('JTreeTable', 'cell:KEYCODE-NO,8(62684671)')
		assert_p('JTreeTable', 'RowCount', '16')
		select('JTreeTable', 'cell:DATE,7(40118)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , , , , , ], [, , , , , , , ], [, , 64634429, 20, 40118, 957, 1, 3.99], [, , 66624458, 20, 40118, 957, 1, 0.89], [, , 63674861, 20, 40118, 957, 10, 2.70], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',1(null)')
		rightclick('JTreeTable', commonBits.fl('Tree') + ',1')
		select_menu(commonBits.fl('Expand Tree'))
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',6(null)')
		assert_p('JTreeTable', 'RowCount', '22')
		select('JTreeTable', 'rows:[7,8,9,10,11,12,13,14,15],columns:[' + commonBits.fl('Tree') + ']')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Table View #{Selected Records#}'))
		select('JTreeTable', 'rows:[7,8,9,10,11,12,13,14,15],columns:[' + commonBits.fl('Tree') + ']')
		select('Table', 'cell:1 - 8|KEYCODE-NO,4(63604808)')
		assert_p('Table', 'Content', '[[64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [62684217, 59, 40118, 957, 1, 9.99], [64624770, 59, 40118, 957, 1, 2.59], [63604808, 20, 40118, 170, 1, 4.87], [69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69684558, 20, 40118, 280, 1, 5.01], [69694158, 20, 40118, 280, 1, 19.00], [69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [65674532, 20, 40118, 929, 1, 3.59]]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,7(69684558)')
		assert_p('Table', 'Text', '69684558', '1 - 8|KEYCODE-NO,7')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(64614401)')
		assert_p('Table', 'Text', '62684217', '1 - 8|KEYCODE-NO,2')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(64614401)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window(commonBits.fl('Save Changes to file: ' + commonBits.sampleDir() + 'DTAR020.bin')):
			click('No')
		close()
	close()
