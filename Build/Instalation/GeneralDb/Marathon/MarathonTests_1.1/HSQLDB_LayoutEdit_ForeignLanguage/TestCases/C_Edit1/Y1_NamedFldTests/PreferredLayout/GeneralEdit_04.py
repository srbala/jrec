useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'csv1DTAR020_tst1.bin.csv')
		select('System_Txt', 'CSV')
		click(commonBits.fl('Edit') + '1')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Update Csv Columns'))
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',1')
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',3')
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',4')
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',5')
		select('FieldChange_JTbl', 'cell:' + commonBits.fl('Type') + ',5(Number)')
		click(commonBits.fl('Apply'))
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Sorted Field Tree'))
		select('fields_JTbl', 'STORE-NO', commonBits.fl('Field') + ',0')
		select('fields_JTbl', 'DEPT-NO', commonBits.fl('Field') + ',1')
		select('fields_JTbl', 'cell:' + commonBits.fl('Field') + ',1(DEPT-NO)')
		select('fieldSummary_JTbl', 'cell:' + commonBits.fl('Function') + ',1()')
		select('fields_JTbl', 'cell:' + commonBits.fl('Field') + ',1(DEPT-NO)')
		select('fieldSummary_JTbl', commonBits.fl('Minimum'), commonBits.fl('Function') + ',1')
		select('fieldSummary_JTbl', commonBits.fl('Minimum'), commonBits.fl('Function') + ',3')
		select('fieldSummary_JTbl', commonBits.fl('Sum'), commonBits.fl('Function') + ',4')
		select('fieldSummary_JTbl', commonBits.fl('Sum'), commonBits.fl('Function') + ',5')
		select('fieldSummary_JTbl', 'cell:' + commonBits.fl('Function') + ',5(Sum)')
		click(commonBits.fl('Build Tree'))
		select('LineTree.FileDisplay_JTbl', 'cell:DATE,9(40118)')

###
###   Not sure which is correct:
###
##		assert_p('LineTree.FileDisplay_JTbl', 'Content', '[[, , , 20, , 170, 2, 9.88], [, , , 20, , 170, 1, 4.87], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , 20, , 280, 1, 5.01], [, , 69684558, 20, 40118, 280, 1, 19.00], [, , 69684558, 20, 40118, 280, -1, -19.00], [, , 69694158, 20, 40118, 280, 1, 5.01], [, , , 20, , 685, 0, 0.00], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , 59, , 335, 5, 35.91], [, , , 59, , 335, 1, 12.99], [, , 61664713, 59, 40118, 335, 1, 17.99], [, , 61664713, 59, 40118, 335, -1, -17.99], [, , 61684613, 59, 40118, 335, 1, 12.99], [, , , 59, , 410, 1, 8.99], [, , 68634752, 59, 40118, 410, 1, 8.99], [, , , 59, , 620, 2, 7.98], [, , 60694698, 59, 40118, 620, 1, 3.99], [, , 60664659, 59, 40118, 620, 1, 3.99], [, , , 59, , 878, 1, 5.95], [, , 60614487, 59, 40118, 878, 1, 5.95], [, , , 166, , 170, 4, 42.56], [, , , 166, , 60, 1, 5.08], [, , 68654655, 166, 40118, 60, 1, 5.08], [, , , 166, , 80, 2, 31.49], [, , 69624033, 166, 40118, 80, 1, 18.19], [, , 60604100, 166, 40118, 80, 1, 13.30], [, , , 166, , 170, 1, 5.99], [, , 68674560, 166, 40118, 170, 1, 5.99]]')
##		assert_p('LineTree.FileDisplay_JTbl', 'Content', '[[, , , 20, , 170, 2, 9.88], [, , , 20, , 170, 1, 4.87], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , 20, , 280, 1, 5.01], [, , 69684558, 20, 40118, 280, 1, 19.00], [, , 69684558, 20, 40118, 280, -1, -19.00], [, , 69694158, 20, 40118, 280, 1, 5.01], [, , , 20, , 685, 0, 0.00], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , 59, , 335, 5, 35.91], [, , , 59, , 335, 1, 12.99], [, , 61664713, 59, 40118, 335, 1, 17.99], [, , 61664713, 59, 40118, 335, -1, -17.99], [, , 61684613, 59, 40118, 335, 1, 12.99], [, , , 59, , 410, 1, 8.99], [, , 68634752, 59, 40118, 410, 1, 8.99], [, , , 59, , 620, 2, 7.98], [, , 60694698, 59, 40118, 620, 1, 3.99], [, , 60664659, 59, 40118, 620, 1, 3.99], [, , , 59, , 878, 1, 5.95], [, , 60614487, 59, 40118, 878, 1, 5.95], [, , , 166, , 170, 4, 42.56], [, , , 166, , 60, 1, 5.08], [, , 68654655, 166, 40118, 60, 1, 5.08], [, , , 166, , 80, 2, 31.49], [, , 69624033, 166, 40118, 80, 1, 18.19], [, , 60604100, 166, 40118, 80, 1, 13.30], [, , , 166, , 170, 1, 5.99], [, , 68674560, 166, 40118, 170, 1, 5.99]]')
###  or this
		assert_p('LineTree.FileDisplay_JTbl', 'Content', '[[, , , 20, , 170, 2, 9.88], [, , , 20, , 170, 1, 4.87], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , 20, , 280, 1, 5.01], [, , 69684558, 20, 40118, 280, 1, 19.00], [, , 69684558, 20, 40118, 280, -1, -19.00], [, , 69694158, 20, 40118, 280, 1, 5.01], [, , , 20, , 685, 0, 0.00], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , 59, , 335, 5, 35.91], [, , , 59, , 335, 1, 12.99], [, , 61664713, 59, 40118, 335, 1, 17.99], [, , 61664713, 59, 40118, 335, -1, -17.99], [, , 61684613, 59, 40118, 335, 1, 12.99], [, , , 59, , 410, 1, 8.99], [, , 68634752, 59, 40118, 410, 1, 8.99], [, , , 59, , 620, 2, 7.98], [, , 60694698, 59, 40118, 620, 1, 3.99], [, , 60664659, 59, 40118, 620, 1, 3.99], [, , , 59, , 878, 1, 5.95], [, , 60614487, 59, 40118, 878, 1, 5.95], [, , , 166, , 60, 4, 42.56], [, , , 166, , 60, 1, 5.08], [, , 68654655, 166, 40118, 60, 1, 5.08], [, , , 166, , 80, 2, 31.49], [, , 69624033, 166, 40118, 80, 1, 18.19], [, , 60604100, 166, 40118, 80, 1, 13.30], [, , , 166, , 170, 1, 5.99], [, , 68674560, 166, 40118, 170, 1, 5.99]]')
		assert_p('LineTree.FileDisplay_JTbl', 'Content', '[[, , , 20, , 170, 2, 9.88], [, , , 20, , 170, 1, 4.87], [, , 63604808, 20, 40118, 170, 1, 4.87], [, , , 20, , 280, 1, 5.01], [, , 69684558, 20, 40118, 280, 1, 19.00], [, , 69684558, 20, 40118, 280, -1, -19.00], [, , 69694158, 20, 40118, 280, 1, 5.01], [, , , 20, , 685, 0, 0.00], [, , 62684671, 20, 40118, 685, 1, 69.99], [, , 62684671, 20, 40118, 685, -1, -69.99], [, , , 59, , 335, 5, 35.91], [, , , 59, , 335, 1, 12.99], [, , 61664713, 59, 40118, 335, 1, 17.99], [, , 61664713, 59, 40118, 335, -1, -17.99], [, , 61684613, 59, 40118, 335, 1, 12.99], [, , , 59, , 410, 1, 8.99], [, , 68634752, 59, 40118, 410, 1, 8.99], [, , , 59, , 620, 2, 7.98], [, , 60694698, 59, 40118, 620, 1, 3.99], [, , 60664659, 59, 40118, 620, 1, 3.99], [, , , 59, , 878, 1, 5.95], [, , 60614487, 59, 40118, 878, 1, 5.95], [, , , 166, , 60, 4, 42.56], [, , , 166, , 60, 1, 5.08], [, , 68654655, 166, 40118, 60, 1, 5.08], [, , , 166, , 80, 2, 31.49], [, , 69624033, 166, 40118, 80, 1, 18.19], [, , 60604100, 166, 40118, 80, 1, 13.30], [, , , 166, , 170, 1, 5.99], [, , 68674560, 166, 40118, 170, 1, 5.99]]')

		select('LineTree.FileDisplay_JTbl', 'cell:STORE-NO,2(20)')
		rightclick('LineTree.FileDisplay_JTbl', 'STORE-NO,2')
		select_menu(commonBits.fl('Edit Record'))
#		select('LineTree.FileDisplay_JTbl', 'cell:STORE-NO,2(20)')
#	#	assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 63604808, 63604808], [STORE-NO, 2, , 20, 20], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 170, 170], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 4.87, 4.87]]')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Show / Hide Fields'))
#		select('LineTree.FileDisplay_JTbl', 'cell:STORE-NO,9(20)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, true], [STORE-NO, true], [DATE, true], [DEPT-NO, true], [QTY-SOLD, true], [SALE-PRICE, true]]')
		select('Table', 'cell:' + commonBits.fl('Show') + ',2(true)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',5(true)')
		
		click(commonBits.fl('Go'))
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 63604808, 63604808], [STORE-NO, 2, , 20, 20], [DEPT-NO, 4, , 170, 170], [QTY-SOLD, 5, , 1, 1]]')
		click('Right')
		keystroke('Right', 'Context Menu')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , 1, 1]]')
		click('Right')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , -1, -1]]')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Show / Hide Fields'))
		select('Table', 'cell:' + commonBits.fl('Show') + ',5(false)')
		click(commonBits.fl('Go'))
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 69684558, 69684558], [STORE-NO, 2, , 20, 20], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , -1, -1], [SALE-PRICE, 6, , -19.00, -19.00]]')
		click('Right')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 69694158, 69694158], [STORE-NO, 2, , 20, 20], [DEPT-NO, 4, , 280, 280], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 5.01, 5.01]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
