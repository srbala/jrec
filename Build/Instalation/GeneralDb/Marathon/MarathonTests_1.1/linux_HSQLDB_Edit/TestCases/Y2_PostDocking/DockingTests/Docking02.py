useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'csv3DTAR020_tst1.bin.csv')
		if commonBits.version() == 'MsAccess':
			select('Record Layout_Txt', 'Comma Delimited, names on the first line')
		else:
			select('System_Txt', 'CSV')
		click(commonBits.fl('Edit') + '1')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		rightclick('LineList.FileDisplay_JTbl', '1|KEYCODE-NO,4')
##		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select_menu(commonBits.fl('Edit Record'))
		select('TabbedPane', 'Record:')
		select('LineFrame.FileDisplay_JTbl', 'cell:' + commonBits.fl('Type') + ',2(Char)')
#		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , Char, 62684671, 62684671], [STORE-NO, 2, , Char, 20, 20], [DATE, 3, , Char, 40118, 40118], [DEPT-NO, 4, , Char, 685, 685], [QTY-SOLD, 5, , Char, 1, 1], [SALE-PRICE, 6, , Char, 69.99, 69.99]]')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , ' + commonBits.fl('Char') + ', 62684671, 62684671], [STORE-NO, 2, , ' + commonBits.fl('Char') + ', 20, 20], [DATE, 3, , ' + commonBits.fl('Char') + ', 40118, 40118], [DEPT-NO, 4, , ' + commonBits.fl('Char') + ', 685, 685], [QTY-SOLD, 5, , ' + commonBits.fl('Char') + ', 1, 1], [SALE-PRICE, 6, , ' + commonBits.fl('Char') + ', 69.99, 69.99]]')
		select('LineFrame.FileDisplay_JTbl', 'cell:' + commonBits.fl('Type') + ',2(Char)')
		assert_p('LineFrame.Record_Txt', 'Text', '5')
		select('LineFrame.FileDisplay_JTbl', 'cell:' + commonBits.fl('Type') + ',2(Char)')
		click(commonBits.fl('Table:'))
		select('TabbedPane', 'Table:')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Sorted Field Tree'))
		select('fields_JTbl', 'STORE-NO', commonBits.fl('Field') + ',0')
		select('fields_JTbl', 'cell:' + commonBits.fl('Field') + ',0(STORE-NO)')
		select('fieldSummary_JTbl', 'cell:' + commonBits.fl('Function') + ',1()')
		select('fields_JTbl', 'cell:' + commonBits.fl('Field') + ',0(STORE-NO)')
		select('fieldSummary_JTbl', commonBits.fl('Maximum'), commonBits.fl('Function') + ',1')
		select('fieldSummary_JTbl', commonBits.fl('Sum'), commonBits.fl('Function') + ',4')
		select('fieldSummary_JTbl', commonBits.fl('Sum'), commonBits.fl('Function') + ',5')
		select('fieldSummary_JTbl', 'cell:' + commonBits.fl('Function') + ',5(' + commonBits.fl('Sum') + ')')
		click(commonBits.fl('Build Tree'))
		select('TabbedPane', 'Tree View')
		assert_p('LineTree.FileDisplay_JTbl', 'Content', '[[, , , 166, , , 4, 42.56], [, , 68654655, 166, 40118, 60, 1, 5.08], [, , 69624033, 166, 40118, 80, 1, 18.19], [, , 60604100, 166, 40118, 80, 1, 13.30], [, , 68674560, 166, 40118, 170, 1, 5.99], [, , , 20, , , 2, 9.88], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , 69684558, 20, 40118, 280, 1, 19.00], [, , 69684558, 20, 40118, 280, -1, -19.00], [, , 69694158, 20, 40118, 280, 1, 5.01], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , 59, , , 5, 35.91], [, , 61664713, 59, 40118, 335, 1, 17.99], [, , 61664713, 59, 40118, 335, -1, -17.99], [, , 61684613, 59, 40118, 335, 1, 12.99], [, , 68634752, 59, 40118, 410, 1, 8.99], [, , 60694698, 59, 40118, 620, 1, 3.99], [, , 60664659, 59, 40118, 620, 1, 3.99], [, , 60614487, 59, 40118, 878, 1, 5.95]]')
		select_menu(commonBits.fl('Window') + '>>' + commonBits.fl('Undock all Tabs'))
##		select('TabbedPane', 'Record:')
##		select('TabbedPane', 'Table:')
		assert_p('LineTree.FileDisplay_JTbl', 'Content', '[[, , , 166, , , 4, 42.56], [, , 68654655, 166, 40118, 60, 1, 5.08], [, , 69624033, 166, 40118, 80, 1, 18.19], [, , 60604100, 166, 40118, 80, 1, 13.30], [, , 68674560, 166, 40118, 170, 1, 5.99], [, , , 20, , , 2, 9.88], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , 69684558, 20, 40118, 280, 1, 19.00], [, , 69684558, 20, 40118, 280, -1, -19.00], [, , 69694158, 20, 40118, 280, 1, 5.01], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , 59, , , 5, 35.91], [, , 61664713, 59, 40118, 335, 1, 17.99], [, , 61664713, 59, 40118, 335, -1, -17.99], [, , 61684613, 59, 40118, 335, 1, 12.99], [, , 68634752, 59, 40118, 410, 1, 8.99], [, , 60694698, 59, 40118, 620, 1, 3.99], [, , 60664659, 59, 40118, 620, 1, 3.99], [, , 60614487, 59, 40118, 878, 1, 5.95]]')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4.87], [69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [69624033, 166, 40118, 80, 1, 18.19], [60604100, 166, 40118, 80, 1, 13.30], [68674560, 166, 40118, 170, 1, 5.99]]')
	close()
