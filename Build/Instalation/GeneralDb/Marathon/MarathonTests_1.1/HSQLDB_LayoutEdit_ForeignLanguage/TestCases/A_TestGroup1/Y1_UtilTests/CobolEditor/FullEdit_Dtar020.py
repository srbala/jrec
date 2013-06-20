useFixture(editFileLayout)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'DTAR020.bin')
		##select('FileChooser', '/C:/Program Files/RecordEdit/MSaccess/SampleFiles/DTAR020.bin')
		click(commonBits.fl('Choose File'))

		if window('Open'):
			click('Open')
		close()
		commonBits.setRecordLayoutX(select, 'DTAR020')
		##select('ComboBox2', 'DTAR020')

		click(commonBits.fl('Edit') + '1')
		select('Table', 'cell:1 - 8|KEYCODE-NO,0(69684558)')
		assert_p('Table', 'Text', '69684558', '1 - 8|KEYCODE-NO,0')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(69684558)')
		assert_p('Table', 'Text', '69684558', '1 - 8|KEYCODE-NO,1')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(69684558)')
		rightclick('Table1',  commonBits.fl('Line') + ',1')
		select_menu(commonBits.fl('Edit Record')
)
##		select('Table1', 'cell:1 - 8|KEYCODE-NO,1(69684558)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-19.00)')
		assert_p('Table', 'Text', '-19.00', commonBits.fl('Data') + ',5')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-19.00)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(280)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(280)')
		assert_p('Table', 'RowCount', '6')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(5.01)')
		assert_p('Table', 'Text', '5.01', commonBits.fl('Data') + ',5')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(5.01)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',0(69694158)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		assert_p('Table', 'Text', '40118', commonBits.fl('Data') + ',2')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		click('RightM')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, 8, 69664668, 69664668, f6f9f6f6f4f6f6f8], [STORE-NO, 9, 2, 184, <, 184c], [DATE, 11, 4, 40118,' 
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(8.95)')
		assert_p('Table', 'Text', 'cell:' + commonBits.fl('Data') + ',5(8.95)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(8.95)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:1 - 8|KEYCODE-NO,1(69684558)')
		rightclick('Table', '1 - 8|KEYCODE-NO,1')
		select_menu(commonBits.fl('Sort')
)

		##select('List', 'DTAR020')
		select('Table', 'SALE-PRICE', commonBits.fl('Field') + ',0')
		select('Table', 'cell:' + commonBits.fl('Field') + ',0(SALE-PRICE)')
		##click(commonBits.fl('Sort') + '1')

		
		if commonBits.isTstLanguage():
			click(commonBits.fl('Sort'))
		else:
			click('Sort1')


		select('Table', 'cell:1 - 8|KEYCODE-NO,0(68684135)')
		rightclick('Table', '1 - 8|KEYCODE-NO,0')
		select_menu(commonBits.fl('Edit Record')
)
	##	select('Table1', 'cell:1 - 8|KEYCODE-NO,0(68684135)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-269.00)')
		assert_p('Table', 'Text', '-269.00', commonBits.fl('Data') + ',5')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-269.00)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(878)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(878)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-249.00)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-249.00)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-69.99)')
		assert_p('Table', 'Text', '-69.99', commonBits.fl('Data') + ',5')
		select('Table', 'cell:' + commonBits.fl('Data') + ',0(62684671)')
		assert_p('Table', 'Text', '62684671', commonBits.fl('Data') + ',0')
		select('Table', 'cell:' + commonBits.fl('Data') + ',0(62684671)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, 8, 64604930, 64604930, f6f4f6f0f4f9f3f0], [STORE-NO, 9, 2, 184, <, 184c], [DATE, 11, 4, 40118, 		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:1 - 8|KEYCODE-NO,0(68684135)')
		rightclick('Table', '1 - 8|KEYCODE-NO,0')
		select_menu('Sort')
		##select('List', 'DTAR020')
		select('Table', 'KEYCODE-NO', commonBits.fl('Field') + ',0')
		select('Table', 'cell:' + commonBits.fl('Field') + ',0(KEYCODE-NO)')
		
		if commonBits.isTstLanguage():
			click(commonBits.fl('Sort'))
		else:
			click('Sort1')

		select('Table', 'cell:1 - 8|KEYCODE-NO,0(60604100)')
		assert_p('Table', 'Text', '60604100', '1 - 8|KEYCODE-NO,0')
		select('Table', 'cell:1 - 8|KEYCODE-NO,0(60604100)')
		rightclick('Table', '1 - 8|KEYCODE-NO,0')
		select_menu(commonBits.fl('Edit Record')
)
##		select('Table1', 'cell:1 - 8|KEYCODE-NO,0(60604100)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(13.30)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(13.30)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(9.00)')
		assert_p('Table', 'Content', '''[[KEYCODE-NO, 1, 8, 60604880, 60604880, f6f0f6f0f4f8f8f0], [STORE-NO, 9, 2, 184, <, 184c], [DATE, 11, 4, 40118, , 250c], [QTY-SOLD, 17, 5, 1, 		select('Table', 'cell:Data,2(40118)')

		assert_p('Table', 'Text', '250', commonBits.fl('Data') + ',3')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-14.25)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-14.25)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:1 - 8|KEYCODE-NO,0(60604100)')
		rightclick('Table', '9 - 2|STORE-NO,0')
		select_menu('Sort')
		##select('List', 'DTAR020')
		select('Table', 'STORE-NO', commonBits.fl('Field') + ',0')
		select('Table', 'cell:' + commonBits.fl('Field') + ',0(STORE-NO)')
		##click('Sort1')

		
		if commonBits.isTstLanguage():
			click(commonBits.fl('Sort'))
		else:
			click('Sort1')


		select('Table', 'cell:9 - 2|STORE-NO,0(20)')
		assert_p('Table', 'Text', 'cell:9 - 2|STORE-NO,0(20)')
		select('Table', 'cell:9 - 2|STORE-NO,0(20)')
		rightclick('Table', '9 - 2|STORE-NO,0')
		select_menu(commonBits.fl('Edit Record')
)
	##	select('Table1', 'cell:9 - 2|STORE-NO,0(20)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-69.99)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(-69.99)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(69.99)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(69.99)')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(4.87)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(4.87)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window(commonBits.fl(r'Save Changes to file: ' + commonBits.sampleDir() + 'DTAR020.bin')):
			click('No')
		close()
	close()
