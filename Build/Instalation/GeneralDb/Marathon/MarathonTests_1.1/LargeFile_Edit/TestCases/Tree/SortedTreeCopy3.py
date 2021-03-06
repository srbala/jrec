useFixture(default)

###
###  Problem Nimbus ???
###
def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'DTAR020.bin')
		click('Edit1')
		select_menu('View>>Sorted Field Tree')
#		select('List', 'DTAR020')
		select('Table', 'STORE-NO', 'Field,0')
		select('Table', 'DEPT-NO', 'Field,1')
		select('Table', 'cell:Field,1(DEPT-NO)')
		click('Build Tree')
		#select('JTreeTable', '')
		rightclick('JTreeTable', 'KEYCODE-NO,1')
		select('JTreeTable', 'cell:KEYCODE-NO,1(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,1')
		select_menu('Copy Record#{s#}')
		select('JTreeTable', 'cell:KEYCODE-NO,3(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,3')
		select_menu('Paste Record#{s#}')
		select('JTreeTable', 'cell:STORE-NO,3(null)')
		assert_p('JTreeTable', 'RowCount', '5')
		select('JTreeTable', 'cell:KEYCODE-NO,4(null)')
		rightclick('JTreeTable', 'STORE-NO,4')
		select('JTreeTable', 'cell:KEYCODE-NO,4(null)')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'cell:KEYCODE-NO,4(null)')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(61664713)')
		assert_p('Table', 'Text', '61684613', '1 - 8|KEYCODE-NO,2')
		select('Table', 'cell:1 - 8|KEYCODE-NO,4(60694698)')
		assert_p('Table', 'Content', '[[61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [63644339, 59, 40118, 878, 1, 12.65], [67674686, 59, 40118, 929, 1, 3.99], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [62684217, 59, 40118, 957, 1, 9.99], [64624770, 59, 40118, 957, 1, 2.59]]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,8(67674686)')
		assert_p('Table', 'RowCount', '13')
		select('Table', 'cell:1 - 8|KEYCODE-NO,8(67674686)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('JTreeTable', 'cell:KEYCODE-NO,1(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Tree,4(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,4')
		select_menu('Copy Record#{s#}')
		select('JTreeTable', 'cell:KEYCODE-NO,7(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,7')
		select_menu('Paste Record#{s#}')
		select('JTreeTable', 'cell:KEYCODE-NO,1(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:KEYCODE-NO,5(null)')
		assert_p('JTreeTable', 'RowCount', '12')
		select('JTreeTable', 'cell:KEYCODE-NO,8(null)')
		assert_p('JTreeTable', 'RowCount', '12')
		select('JTreeTable', 'cell:KEYCODE-NO,8(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,8')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:KEYCODE-NO,9(60694698)')
		assert_p('JTreeTable', 'Text', 'cell:KEYCODE-NO,9(60694698)')
		select('JTreeTable', 'cell:KEYCODE-NO,10(60664659)')
		assert_p('JTreeTable', 'Text', '60664659', 'KEYCODE-NO,10')
		select('JTreeTable', 'cell:KEYCODE-NO,9(60694698)')
		assert_p('JTreeTable', 'RowCount', '14')
		select('JTreeTable', 'rows:[9,10],columns:[KEYCODE-NO]')
		rightclick('JTreeTable', 'KEYCODE-NO,9')
		select('JTreeTable', 'rows:[9,10],columns:[KEYCODE-NO]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[9,10],columns:[KEYCODE-NO]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,0(60694698)')
		assert_p('Table', 'Content', '[[60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99]]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,0(60694698)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('JTreeTable', 'cell:Tree,4(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,4')
		select_menu('Copy Record#{s#}')
		select('JTreeTable', 'cell:KEYCODE-NO,2(null)')
		rightclick('JTreeTable', 'KEYCODE-NO,2')
		select_menu('Paste Record#{s#} Prior')
		select('JTreeTable', 'cell:Tree,1(null)')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'rows:[2,3],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[2,3],columns:[Tree]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(60664659)')
		assert_p('Table', 'Text', '59', '9 - 2|STORE-NO,1')
		select('Table', 'cell:1 - 8|KEYCODE-NO,2(61664713)')
		assert_p('Table', 'Content', '[[60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99]]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,3(61664713)')
		assert_p('Table', 'RowCount', '5')
		select('Table', 'cell:1 - 8|KEYCODE-NO,3(61664713)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('JTreeTable', 'cell:Tree,12(null)')
		rightclick('JTreeTable', 'Tree,12')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>DTAR020.bin>>Table:')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')


		if window('Save Changes to file: ' + commonBits.sampleDir() + 'DTAR020.bin'):
			click('No')
		close()
	close()
