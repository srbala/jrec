useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Protocol Buffer Editor'):
		select('File_Txt', commonBits.sampleDir() + 'DTAR020_tst1.bin')
		click('Edit1')
		click('Export')
		select('TabbedPane', 'Velocity')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('File>>Export via Velociy Skelton>>toCsv_Comma.vm')
		select('Edit Output File_Chk', 'true')
		select('Keep screen open_Chk', 'true')
		click('save file')

		if window(''):
			assert_p('Table', 'Content', '[[63604808, 20, 40118, 170, 1, 4870], [69684558, 20, 40118, 280, 1, 19000], [69684558, 20, 40118, 280, -1, -19000], [69694158, 20, 40118, 280, 1, 5010], [62684671, 20, 40118, 685, 1, 69990], [62684671, 20, 40118, 685, -1, -69990], [61664713, 59, 40118, 335, 1, 17990], [61664713, 59, 40118, 335, -1, -17990], [61684613, 59, 40118, 335, 1, 12990], [68634752, 59, 40118, 410, 1, 8990], [60694698, 59, 40118, 620, 1, 3990], [60664659, 59, 40118, 620, 1, 3990], [60614487, 59, 40118, 878, 1, 5950], [68654655, 166, 40118, 60, 1, 5080], [69624033, 166, 40118, 80, 1, 18190], [60604100, 166, 40118, 80, 1, 13300], [68674560, 166, 40118, 170, 1, 5990], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
			assert_p('Parser_Txt', 'Text', 'Basic Parser')
			assert_p('ComboBox', 'Text', ',')
			click('Go')
##			assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4870], [69684558, 20, 40118, 280, 1, 19000], [69684558, 20, 40118, 280, -1, -19000], [69694158, 20, 40118, 280, 1, 5010], [62684671, 20, 40118, 685, 1, 69990], [62684671, 20, 40118, 685, -1, -69990], [61664713, 59, 40118, 335, 1, 17990], [61664713, 59, 40118, 335, -1, -17990], [61684613, 59, 40118, 335, 1, 12990], [68634752, 59, 40118, 410, 1, 8990], [60694698, 59, 40118, 620, 1, 3990], [60664659, 59, 40118, 620, 1, 3990], [60614487, 59, 40118, 878, 1, 5950], [68654655, 166, 40118, 60, 1, 5080], [69624033, 166, 40118, 80, 1, 18190], [60604100, 166, 40118, 80, 1, 13300], [68674560, 166, 40118, 170, 1, 5990]]')
		close()

		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4870], [69684558, 20, 40118, 280, 1, 19000], [69684558, 20, 40118, 280, -1, -19000], [69694158, 20, 40118, 280, 1, 5010], [62684671, 20, 40118, 685, 1, 69990], [62684671, 20, 40118, 685, -1, -69990], [61664713, 59, 40118, 335, 1, 17990], [61664713, 59, 40118, 335, -1, -17990], [61684613, 59, 40118, 335, 1, 12990], [68634752, 59, 40118, 410, 1, 8990], [60694698, 59, 40118, 620, 1, 3990], [60664659, 59, 40118, 620, 1, 3990], [60614487, 59, 40118, 878, 1, 5950], [68654655, 166, 40118, 60, 1, 5080], [69624033, 166, 40118, 80, 1, 18190], [60604100, 166, 40118, 80, 1, 13300], [68674560, 166, 40118, 170, 1, 5990]]')
		select('LineList.Layouts_Txt', 'Full Line')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808,20,40118,170,1,4870,], [69684558,20,40118,280,1,19000,], [69684558,20,40118,280,-1,-19000,], [69694158,20,40118,280,1,5010,], [62684671,20,40118,685,1,69990,], [62684671,20,40118,685,-1,-69990,], [61664713,59,40118,335,1,17990,], [61664713,59,40118,335,-1,-17990,], [61684613,59,40118,335,1,12990,], [68634752,59,40118,410,1,8990,], [60694698,59,40118,620,1,3990,], [60664659,59,40118,620,1,3990,], [60614487,59,40118,878,1,5950,], [68654655,166,40118,60,1,5080,], [69624033,166,40118,80,1,18190,], [60604100,166,40118,80,1,13300,], [68674560,166,40118,170,1,5990,]]')
	close()