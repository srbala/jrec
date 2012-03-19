useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_10'
	if window('Record Editor'):
		select_menu('File>>File Copy Menu')
		click('*3')
		select('FileChooser', commonBits.sampleDir() + 'DTAR020.bin')
		select('FileChooser1', commonBits.sampleDir() + 'CpyCsvDtar020.Txt')
		commonBits.setRecordLayout2(select, 'DTAR020')
		select('ComboBox3', '<Tab>')
		click('Right')
		select('TabbedPane', '')
		select('Table1', 'cell:Include,3(true)')
		click('Right')
		select('TabbedPane', '')
		select('FileChooser', commonBits.userDir() + 'cpy2csvDTAR020.xml')
		click('Save1')
		click('Copy2')
		assert_p('TextField1', 'Text', 'Copy Done !!! ')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>Menu>>Copy Menu')
		select_menu('Window>>Open File')
		select('FileChooser', commonBits.sampleDir() + 'CpyCsvDtar020.Txt')
		##select('ComboBox2', 'Tab Delimited, names on the first line')
		commonBits.setRecordLayout(select, 'Tab Delimited, names on the first line')

		click('Edit1')
		select('Table', 'cell:2|STORE-NO,0(20)')
		rightclick('Table', '1|KEYCODE-NO,0')
##		select('Table', 'cell:2|STORE-NO,0(20)')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|STORE-NO,0(20)')
		select('Table', 'cell:Data,0(69684558)')
		assert_p('JTableHeader', 'Text', 'Data', 'Data')
		select('Table', 'cell:Data,2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [QTY-SOLD, 4, , 1, 1], [SALE-PRICE, 5, , 19.00, 19.00]]')
		select('Table', 'cell:Data,2(40118)')
		click('Right')
		select('Table', 'cell:Data,4(-19.00)')
		assert_p('Table', 'Text', '-19.00', 'Data,4')
		select('Table', 'cell:Data,2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [QTY-SOLD, 4, , -1, -1], [SALE-PRICE, 5, , -19.00, -19.00]]')
		select('Table', 'cell:Data,2(40118)')
		click('Right')
		select('Table', 'cell:Data,4(5.01)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [QTY-SOLD, 4, , 1, 1], [SALE-PRICE, 5, , 5.01, 5.01]]')
		select('Table', 'cell:Data,2(40118)')
		click('Right')
		select('Table', 'cell:Data,2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69694158, 69694158], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [QTY-SOLD, 4, , 1, 1], [SALE-PRICE, 5, , 19.00, 19.00]]')
		select('Table', 'cell:Data,2(40118)')
		click('Right')
		select('Table', 'cell:Data,4(-19.00)')
		assert_p('Table', 'Text', '-19.00', 'Data,4')
		select('Table', 'cell:Data,2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69694158, 69694158], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [QTY-SOLD, 4, , -1, -1], [SALE-PRICE, 5, , -19.00, -19.00]]')
	close()