useFixture(reCsvEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('reCsv Editor'):
		select('FilePane$3', 'XfdDTAR020.csv.csv')
		doubleclick('FilePane$3', '6')
		click(commonBits.fl('Edit') + '1')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Show / Hide Fields'))
		select('Table', 'cell:' + commonBits.fl('Show') + ',0(true)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',5(true)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',2(true)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, false], [STORE-NO, true], [DATE, false], [DEPT-NO, true], [QTY-SOLD, true], [SALE-PRICE, false]]')
		click(commonBits.fl('Go'))
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[20, 280, 1], [20, 280, 1], [20, 280, -1], [20, 280, 1], [20, 170, 1], [20, 685, 1], [20, 685, -1], [20, 957, 1], [20, 957, 1], [20, 957, 10], [20, 929, 1], [59, 957, 1], [59, 957, 1], [59, 335, 1], [59, 335, -1], [59, 410, 1], [59, 878, 1], [59, 878, 1], [59, 620, 1], [59, 620, 1], [59, 957, 1], [59, 929, 1]]')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		rightclick('LineList.FileDisplay_JTbl', '2|STORE-NO,8')
##		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select_menu(commonBits.fl('Show Column') + '>>KEYCODE-NO')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69684558, 20, 280, 1], [69694158, 20, 280, 1], [69694158, 20, 280, -1], [69694158, 20, 280, 1], [63604808, 20, 170, 1], [62684671, 20, 685, 1], [62684671, 20, 685, -1], [64634429, 20, 957, 1], [66624458, 20, 957, 1], [63674861, 20, 957, 10], [65674532, 20, 929, 1], [64614401, 59, 957, 1], [64614401, 59, 957, 1], [61664713, 59, 335, 1], [61664713, 59, 335, -1], [68634752, 59, 410, 1], [60614487, 59, 878, 1], [63644339, 59, 878, 1], [60694698, 59, 620, 1], [60664659, 59, 620, 1], [62684217, 59, 957, 1], [67674686, 59, 929, 1]]')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Show / Hide Fields'))
##		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',5(false)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, true], [STORE-NO, true], [DATE, false], [DEPT-NO, true], [QTY-SOLD, true], [SALE-PRICE, true]]')
		click(commonBits.fl('Go'))
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69684558, 20, 280, 1, 5.01], [69694158, 20, 280, 1, 19.00], [69694158, 20, 280, -1, -19.00], [69694158, 20, 280, 1, 5.01], [63604808, 20, 170, 1, 4.87], [62684671, 20, 685, 1, 69.99], [62684671, 20, 685, -1, -69.99], [64634429, 20, 957, 1, 3.99], [66624458, 20, 957, 1, 0.89], [63674861, 20, 957, 10, 2.70], [65674532, 20, 929, 1, 3.59], [64614401, 59, 957, 1, 1.99], [64614401, 59, 957, 1, 1.99], [61664713, 59, 335, 1, 17.99], [61664713, 59, 335, -1, -17.99], [68634752, 59, 410, 1, 8.99], [60614487, 59, 878, 1, 5.95], [63644339, 59, 878, 1, 12.65], [60694698, 59, 620, 1, 3.99], [60664659, 59, 620, 1, 3.99], [62684217, 59, 957, 1, 9.99], [67674686, 59, 929, 1, 3.99]]')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Show / Hide Fields'))
##		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',2(false)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',4(true)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',5(true)')
		click(commonBits.fl('Go'))
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69684558, 20, 40118, 280], [69694158, 20, 40118, 280], [69694158, 20, 40118, 280], [69694158, 20, 40118, 280], [63604808, 20, 40118, 170], [62684671, 20, 40118, 685], [62684671, 20, 40118, 685], [64634429, 20, 40118, 957], [66624458, 20, 40118, 957], [63674861, 20, 40118, 957], [65674532, 20, 40118, 929], [64614401, 59, 40118, 957], [64614401, 59, 40118, 957], [61664713, 59, 40118, 335], [61664713, 59, 40118, 335], [68634752, 59, 40118, 410], [60614487, 59, 40118, 878], [63644339, 59, 40118, 878], [60694698, 59, 40118, 620], [60664659, 59, 40118, 620], [62684217, 59, 40118, 957], [67674686, 59, 40118, 929]]')
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Show / Hide Fields'))
##		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		select('Table', 'cell:' + commonBits.fl('Show') + ',5(false)')
		assert_p('Table', 'Content', '[[KEYCODE-NO, true], [STORE-NO, true], [DATE, true], [DEPT-NO, true], [QTY-SOLD, false], [SALE-PRICE, true]]')
		click(commonBits.fl('Go'))
		select('LineList.FileDisplay_JTbl', 'cell:2|STORE-NO,0(20)')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[69684558, 20, 40118, 280, 5.01], [69694158, 20, 40118, 280, 19.00], [69694158, 20, 40118, 280, -19.00], [69694158, 20, 40118, 280, 5.01], [63604808, 20, 40118, 170, 4.87], [62684671, 20, 40118, 685, 69.99], [62684671, 20, 40118, 685, -69.99], [64634429, 20, 40118, 957, 3.99], [66624458, 20, 40118, 957, 0.89], [63674861, 20, 40118, 957, 2.70], [65674532, 20, 40118, 929, 3.59], [64614401, 59, 40118, 957, 1.99], [64614401, 59, 40118, 957, 1.99], [61664713, 59, 40118, 335, 17.99], [61664713, 59, 40118, 335, -17.99], [68634752, 59, 40118, 410, 8.99], [60614487, 59, 40118, 878, 5.95], [63644339, 59, 40118, 878, 12.65], [60694698, 59, 40118, 620, 3.99], [60664659, 59, 40118, 620, 3.99], [62684217, 59, 40118, 957, 9.99], [67674686, 59, 40118, 929, 3.99]]')
	close()
