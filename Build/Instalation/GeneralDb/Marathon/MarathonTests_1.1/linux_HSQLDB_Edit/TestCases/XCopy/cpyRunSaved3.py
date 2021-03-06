useFixture(RecordEditor)

def test():
	from Modules import commonBits
	import time

	java_recorded_version = '1.6.0_10'

	if window('Record Editor'):
		commonBits.selectOldFilemenu(select_menu, 'Utilities', 'File Copy Menu')
		click('*3')
		select('FileChooser', commonBits.sampleDir() + 'DTAR020.bin')
		select('FileChooser1', commonBits.sampleDir() + 'barDTAR020.csv')
		commonBits.setRecordLayout2(select, 'DTAR020')
		select('DelimiterCombo', '|')
		click('Right')
		select('TabbedPane', '')
		select('Table1', 'cell:' + commonBits.fl('Field') + ',1(STORE-NO)')
		assert_p('Table1', 'Content', '[[KEYCODE-NO, true], [STORE-NO, true], [DATE, true], [DEPT-NO, true], [QTY-SOLD, true], [SALE-PRICE, true]]')
##		select('Table1', '')
		select('Table', 'cell:' + commonBits.fl('Record') + ',0(DTAR020)')
		doubleclick('Table', commonBits.fl('Record') + ',0')
		assert_p('Table', 'Content', '[[DTAR020, true]]')
		select('Table', 'cell:' + commonBits.fl('Record') + ',0(DTAR020)')
		click('Right')
		select('TabbedPane', '')
#		click(commonBits.fl('Choose File'))

#		if window('Open'):
#			click('Cancel')
#		close()

#		click(commonBits.fl('Choose File'))

#		if window('Open'):
#			click('Cancel')
#		close()

		select('FileChooser', commonBits.userDir() + 'CpyDTAR020barCsv.xml')
		commonBits.save1(click)
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('*')
		select('FileChooser', commonBits.userDir() + 'CpyDTAR020barCsv.xml')
		click(commonBits.fl('Run Copy Dialog'))
		assert_p('FileChooser', 'Text', commonBits.sampleDir() + 'DTAR020.bin')
		assert_p('FileChooser1', 'Text', commonBits.sampleDir() + 'barDTAR020.csv')

		if commonBits.isRecordEditor():
			assert_p('ComboBox2', 'Text', 'DTAR020')

		assert_p('DelimiterCombo', 'Text', '|')
		click('Right')
		select('TabbedPane', '')
		select('Table', 'cell:' + commonBits.fl('Record') + ',0(DTAR020)')
		select('Table', 'cell:' + commonBits.fl('Record') + ',0(DTAR020)')
		doubleclick('Table', commonBits.fl('Record') + ',0')
		assert_p('Table', 'Text', 'DTAR020', commonBits.fl('Record') + ',0')
		select('Table', 'cell:' + commonBits.fl('Record') + ',0(DTAR020)')
		select('Table1', 'cell:' + commonBits.fl('Field') + ',0(KEYCODE-NO)')
		assert_p('Table1', 'Content', '[[KEYCODE-NO, true], [STORE-NO, true], [DATE, true], [DEPT-NO, true], [QTY-SOLD, true], [SALE-PRICE, true]]')
		select('Table1', 'cell:' + commonBits.fl('Field') + ',0(KEYCODE-NO)')
		click('Right')
		select('TabbedPane', '')
		##click('Copy2')

		commonBits.copy(click)

		assert_p('TextField1', 'Text', commonBits.fl('Copy Done !!!'))
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Open')
		select('FileChooser', commonBits.sampleDir() + 'barDTAR020.csv')
		select('ComboBox2', 'Generic CSV - enter details')
		commonBits.doEdit(click)


		if window(''):
			select('CheckBox', 'true')
			assert_p('DelimiterCombo', 'Text', '|')
			select('Table', 'cell:DATE,3(40118)')
			assert_p('Table', 'Content', '[[69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69684558, 20, 40118, 280, 1, 5.01], [69694158, 20, 40118, 280, 1, 19.00], [69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [63604808, 20, 40118, 170, 1, 4.87], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [64634429, 20, 40118, 957, 1, 3.99], [66624458, 20, 40118, 957, 1, 0.89], [63674861, 20, 40118, 957, 10, 2.70], [65674532, 20, 40118, 929, 1, 3.59], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95], [63644339, 59, 40118, 878, 1, 12.65], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [62684217, 59, 40118, 957, 1, 9.99], [67674686, 59, 40118, 929, 1, 3.99], [61684613, 59, 40118, 335, 1, 12.99], [64624770, 59, 40118, 957, 1, 2.59], [69694814, 166, 40118, 360, 1, 2.50], [69694814, 166, 40118, 360, 1, 2.50], [69644164, 166, 40118, 193, 1, 21.59]]')
			select('Table', 'cell:DATE,3(40118)')
			commonBits.doSleep()

			click(commonBits.fl('Go'))
		close()

		commonBits.doSleep()
		select('Table', 'cell:4|DEPT-NO,0(280)')
		assert_p('Table', 'Text', 'cell:4|DEPT-NO,0(280)')
		select('Table', 'cell:1|KEYCODE-NO,1(69684558)')
		rightclick('Table', '1|KEYCODE-NO,1')
		select_menu( commonBits.fl('Edit Record'))
##		select('Table1', 'cell:1|KEYCODE-NO,1(69684558)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',0(69684558)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , -1, -1], [SALE-PRICE, 6, , -19.00, -19.00]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',0(69684558)')
		click('TextArea')
		assert_p('TextArea', 'Text', '69684558|20|40118|280|-1|-19.00')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 5.01, 5.01]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		click('TextArea')
		assert_p('TextArea', 'Text', '69684558|20|40118|280|1|5.01')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69694158, 69694158], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 19.00, 19.00]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		click('TextArea')
		click('TextArea')
		assert_p('TextArea', 'Text', '69694158|20|40118|280|1|19.00')
		click('Right')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, 1, , 69694158, 69694158], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 5.01, 5.01]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(40118)')
		click('TextArea')
		click('TextArea')
		assert_p('TextArea', 'Text', '69694158|20|40118|280|1|5.01')
	close()
