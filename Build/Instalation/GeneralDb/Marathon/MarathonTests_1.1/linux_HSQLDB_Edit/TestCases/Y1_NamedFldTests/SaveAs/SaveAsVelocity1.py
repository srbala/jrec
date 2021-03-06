useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'DTAR020_tst1.bin')
		click(commonBits.fl('Edit') + '1')
		select('LineList.FileDisplay_JTbl', 'rows:[3,4,5,6,7,8,9,10,11,12,13],columns:[9 - 2|STORE-NO]')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Table View #{Selected Records#}'))
##		select('LineList.FileDisplay_JTbl1', 'rows:[3,4,5,6,7,8,9,10,11,12,13],columns:[9 - 2|STORE-NO]')
		select('LineList.FileDisplay_JTbl', 'rows:[2,3,4,5,6],columns:[9 - 2|STORE-NO]')
		select_menu(commonBits.fl('File') + '>>' + commonBits.fl('Export via Velociy Skelton') + '>>toCsv_Comma.vm')
##		select('LineList.FileDisplay_JTbl', 'rows:[2,3,4,5,6],columns:[9 - 2|STORE-NO]')
		select('Edit Output File_Chk', 'true')
		select('Keep screen open_Chk', 'true')
		click(commonBits.fl('Save File'))

		if window(''):
			assert_p('Table', 'Content', '[[69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
			assert_p('Parser_Txt', 'Text', commonBits.fl('Basic Parser')
)
			assert_p('DelimiterCombo', 'Text', ',')
			click(commonBits.fl('Go'))
##			assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08]]')
		close()

##		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08]]')
		select('LineList.Layouts_Txt', commonBits.fl('Full Line'))
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69694158,20,40118,280,1,5.01,], [62684671,20,40118,685,1,69.99,], [62684671,20,40118,685,-1,-69.99,], [61664713,59,40118,335,1,17.99,], [61664713,59,40118,335,-1,-17.99,], [61684613,59,40118,335,1,12.99,], [68634752,59,40118,410,1,8.99,], [60694698,59,40118,620,1,3.99,], [60664659,59,40118,620,1,3.99,], [60614487,59,40118,878,1,5.95,], [68654655,166,40118,60,1,5.08,]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('What to Save_Txt', commonBits.fl('File'))
		click(commonBits.fl('Save File'))

		if window(''):
##			assert_p('Table', 'Content', '[[69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
			assert_p('Table', 'Content', '[[63604808, 20, 40118, 170, 1, 4.87], [69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [69624033, 166, 40118, 80, 1, 18.19], [60604100, 166, 40118, 80, 1, 13.30], [68674560, 166, 40118, 170, 1, 5.99], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')

			assert_p('DelimiterCombo', 'Text', ',')
			click(commonBits.fl('Go'))
##			assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08]]')
		close()

##		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08]]')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4.87], [69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [60694698, 59, 40118, 620, 1, 3.99], [60664659, 59, 40118, 620, 1, 3.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [69624033, 166, 40118, 80, 1, 18.19], [60604100, 166, 40118, 80, 1, 13.30], [68674560, 166, 40118, 170, 1, 5.99]]')




		select('LineList.Layouts_Txt', commonBits.fl('Full Line'))
##		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69694158,20,40118,280,1,5.01,], [62684671,20,40118,685,1,69.99,], [62684671,20,40118,685,-1,-69.99,], [61664713,59,40118,335,1,17.99,], [61664713,59,40118,335,-1,-17.99,], [61684613,59,40118,335,1,12.99,], [68634752,59,40118,410,1,8.99,], [60694698,59,40118,620,1,3.99,], [60664659,59,40118,620,1,3.99,], [60614487,59,40118,878,1,5.95,], [68654655,166,40118,60,1,5.08,]]')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808,20,40118,170,1,4.87,], [69684558,20,40118,280,1,19.00,], [69684558,20,40118,280,-1,-19.00,], [69694158,20,40118,280,1,5.01,], [62684671,20,40118,685,1,69.99,], [62684671,20,40118,685,-1,-69.99,], [61664713,59,40118,335,1,17.99,], [61664713,59,40118,335,-1,-17.99,], [61684613,59,40118,335,1,12.99,], [68634752,59,40118,410,1,8.99,], [60694698,59,40118,620,1,3.99,], [60664659,59,40118,620,1,3.99,], [60614487,59,40118,878,1,5.95,], [68654655,166,40118,60,1,5.08,], [69624033,166,40118,80,1,18.19,], [60604100,166,40118,80,1,13.30,], [68674560,166,40118,170,1,5.99,]]')



		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('What to Save_Txt', commonBits.fl('Selected Records'))
		click(commonBits.fl('Save File'))

		if window(''):
			assert_p('Table', 'Content', '[[KEYCODE-NO, STORE-NO, DATE, DEPT-NO, QTY-SOLD, SALE-PRICE], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
			assert_p('DelimiterCombo', 'Text', ',')
			click(commonBits.fl('Go'))
##			assert_p('LineList.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, STORE-NO, DATE, DEPT-NO, QTY-SOLD, SALE-PRICE], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99]]')
		close()

		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO, STORE-NO, DATE, DEPT-NO, QTY-SOLD, SALE-PRICE], [62684671, 20, 40118, 685, -1, -69.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [61684613, 59, 40118, 335, 1, 12.99], [68634752, 59, 40118, 410, 1, 8.99]]')
		select('LineList.Layouts_Txt', commonBits.fl('Full Line'))
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[KEYCODE-NO,STORE-NO,DATE,DEPT-NO,QTY-SOLD,SALE-PRICE,], [62684671,20,40118,685,-1,-69.99,], [61664713,59,40118,335,1,17.99,], [61664713,59,40118,335,-1,-17.99,], [61684613,59,40118,335,1,12.99,], [68634752,59,40118,410,1,8.99,]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
