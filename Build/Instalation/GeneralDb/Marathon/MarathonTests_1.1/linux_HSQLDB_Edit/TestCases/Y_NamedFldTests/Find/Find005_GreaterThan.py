useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'csv2DTAR020_tst1.bin.csv')
		select('System_Txt', 'CSV')
		click('Edit1')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4.87], [69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [69624033, 166, 40118, 80, 1, 18.19], [60604100, 166, 40118, 80, 1, 13.30], [68674560, 166, 40118, 170, 1, 5.99]]')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		rightclick('LineList.FileDisplay_JTbl', '1|KEYCODE-NO,0')
##		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select_menu('Edit Record')
#		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
#		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		click('Find1')
##		click('WindowsInternalFrameTitlePane', 153, 18)
		select('Find.Search For_Txt', '58')
		select('Find.Operator_Txt', '>')
		select('Find.Field_Txt', 'STORE-NO')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=7, 1, 0')
		select_menu('Window>>csv2DTAR020_tst1.bin.csv>>Record: ')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 61664713, 61664713], [STORE-NO, 2, , 59, 59], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 335, 335], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 17.99, 17.99]]')
		assert_p('LineFrame.Record_Txt', 'Text', '7')
		select_menu('Window>>csv2DTAR020_tst1.bin.csv>>Find')
		select('Find.Operator_Txt', '>')
		select('Find.Field_Txt', 'STORE-NO')
		
		click('Find1')
		
##		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=8, 1, 0')

		select_menu('Window>>csv2DTAR020_tst1.bin.csv>>Record: ')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 61664713, 61664713], [STORE-NO, 2, , 59, 59], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 335, 335], [QTY-SOLD, 5, , -1, -1], [SALE-PRICE, 6, , -17.99, -17.99]]')
		assert_p('LineFrame.Record_Txt', 'Text', '8')
		select_menu('Window>>csv2DTAR020_tst1.bin.csv>>Find')
		select('Find.Operator_Txt', '>')
		select('Find.Field_Txt', 'STORE-NO')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=9, 1, 0')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=10, 1, 0')
		select_menu('Window>>csv2DTAR020_tst1.bin.csv>>Record: ')
		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, 1, , 68634752, 68634752], [STORE-NO, 2, , 59, 59], [DATE, 3, , 40118, 40118], [DEPT-NO, 4, , 410, 410], [QTY-SOLD, 5, , 1, 1], [SALE-PRICE, 6, , 8.99, 8.99]]')
		assert_p('LineFrame.Record_Txt', 'Text', '10')
	close()