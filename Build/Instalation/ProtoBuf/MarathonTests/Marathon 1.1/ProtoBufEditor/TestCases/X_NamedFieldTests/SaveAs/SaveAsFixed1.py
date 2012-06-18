useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Protocol Buffer Editor'):
		select('File_Txt', commonBits.sampleDir() + 'DTAR020_tst1.bin')
		click('Edit1')
		select('LineList.FileDisplay_JTbl', 'rows:[2,3,4,5,6,7,8,9,10,11,12,13],columns:[2|Store_No]')
		click('Export')
		select('TabbedPane', 'Fixed')
		select('names on first line_Chk', 'true')
		select('space between fields_Chk', 'true')
		select('Edit Output File_Chk', 'true')
		select('Keep screen open_Chk', 'true')
		assert_p('FixedColNames_JTbl', 'Content', '[[Keycode_no, true, 10], [Store_No, true, 8], [DATE, true, 5], [Dept_No, true, 7], [Qty_Sold, true, 8], [Sale_Price, true, 10]]')
		click('save file')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no, Store_No,  DATE, Dept_No, Qty_Sold, Sale_Price], [  63604808,       20, 40118,     170,        1,       4870], [  69684558,       20, 40118,     280,        1,      19000], [  69684558,       20, 40118,     280,       -1,     -19000], [  69694158,       20, 40118,     280,        1,       5010], [  62684671,       20, 40118,     685,        1,      69990], [  62684671,       20, 40118,     685,       -1,     -69990], [  61664713,       59, 40118,     335,        1,      17990], [  61664713,       59, 40118,     335,       -1,     -17990], [  61684613,       59, 40118,     335,        1,      12990], [  68634752,       59, 40118,     410,        1,       8990], [  60694698,       59, 40118,     620,        1,       3990], [  60664659,       59, 40118,     620,        1,       3990], [  60614487,       59, 40118,     878,        1,       5950], [  68654655,      166, 40118,      60,        1,       5080], [  69624033,      166, 40118,      80,        1,      18190], [  60604100,      166, 40118,      80,        1,      13300], [  68674560,      166, 40118,     170,        1,       5990]]')
		select('LineList.Layouts_Txt', 'Full Line')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no Store_No  DATE Dept_No Qty_Sold Sale_Price], [  63604808       20 40118     170        1       4870], [  69684558       20 40118     280        1      19000], [  69684558       20 40118     280       -1     -19000], [  69694158       20 40118     280        1       5010], [  62684671       20 40118     685        1      69990], [  62684671       20 40118     685       -1     -69990], [  61664713       59 40118     335        1      17990], [  61664713       59 40118     335       -1     -17990], [  61684613       59 40118     335        1      12990], [  68634752       59 40118     410        1       8990], [  60694698       59 40118     620        1       3990], [  60664659       59 40118     620        1       3990], [  60614487       59 40118     878        1       5950], [  68654655      166 40118      60        1       5080], [  69624033      166 40118      80        1      18190], [  60604100      166 40118      80        1      13300], [  68674560      166 40118     170        1       5990]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('What to Save_Txt', 'Selected Records')
		click('save file')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no, Store_No,  DATE, Dept_No, Qty_Sold, Sale_Price], [  69684558,       20, 40118,     280,       -1,     -19000], [  69694158,       20, 40118,     280,        1,       5010], [  62684671,       20, 40118,     685,        1,      69990], [  62684671,       20, 40118,     685,       -1,     -69990], [  61664713,       59, 40118,     335,        1,      17990], [  61664713,       59, 40118,     335,       -1,     -17990], [  61684613,       59, 40118,     335,        1,      12990], [  68634752,       59, 40118,     410,        1,       8990], [  60694698,       59, 40118,     620,        1,       3990], [  60664659,       59, 40118,     620,        1,       3990], [  60614487,       59, 40118,     878,        1,       5950], [  68654655,      166, 40118,      60,        1,       5080]]')
		select('LineList.Layouts_Txt', 'Full Line')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no Store_No  DATE Dept_No Qty_Sold Sale_Price], [  69684558       20 40118     280       -1     -19000], [  69694158       20 40118     280        1       5010], [  62684671       20 40118     685        1      69990], [  62684671       20 40118     685       -1     -69990], [  61664713       59 40118     335        1      17990], [  61664713       59 40118     335       -1     -17990], [  61684613       59 40118     335        1      12990], [  68634752       59 40118     410        1       8990], [  60694698       59 40118     620        1       3990], [  60664659       59 40118     620        1       3990], [  60614487       59 40118     878        1       5950], [  68654655      166 40118      60        1       5080]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('FixedColNames_JTbl', 'cell:Include,2(true)')
		select('FixedColNames_JTbl', 'cell:Include,3(true)')
		click('save file')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no, Store_No, Qty_Sold, Sale_Price], [  69684558,       20,       -1,     -19000], [  69694158,       20,        1,       5010], [  62684671,       20,        1,      69990], [  62684671,       20,       -1,     -69990], [  61664713,       59,        1,      17990], [  61664713,       59,       -1,     -17990], [  61684613,       59,        1,      12990], [  68634752,       59,        1,       8990], [  60694698,       59,        1,       3990], [  60664659,       59,        1,       3990], [  60614487,       59,        1,       5950], [  68654655,      166,        1,       5080]]')
		select('LineList.Layouts_Txt', 'Full Line')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no Store_No Qty_Sold Sale_Price], [  69684558       20       -1     -19000], [  69694158       20        1       5010], [  62684671       20        1      69990], [  62684671       20       -1     -69990], [  61664713       59        1      17990], [  61664713       59       -1     -17990], [  61684613       59        1      12990], [  68634752       59        1       8990], [  60694698       59        1       3990], [  60664659       59        1       3990], [  60614487       59        1       5950], [  68654655      166        1       5080]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('space between fields_Chk', 'false')
		click('save file')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_no, Store_No, Qty_Sold, Sale_Price], [  69684558,       20,       -1,     -19000], [  69694158,       20,        1,       5010], [  62684671,       20,        1,      69990], [  62684671,       20,       -1,     -69990], [  61664713,       59,        1,      17990], [  61664713,       59,       -1,     -17990], [  61684613,       59,        1,      12990], [  68634752,       59,        1,       8990], [  60694698,       59,        1,       3990], [  60664659,       59,        1,       3990], [  60614487,       59,        1,       5950], [  68654655,      166,        1,       5080]]')
		select('LineList.Layouts_Txt', 'Full Line')
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[Keycode_noStore_NoQty_SoldSale_Price], [  69684558      20      -1    -19000], [  69694158      20       1      5010], [  62684671      20       1     69990], [  62684671      20      -1    -69990], [  61664713      59       1     17990], [  61664713      59      -1    -17990], [  61684613      59       1     12990], [  68634752      59       1      8990], [  60694698      59       1      3990], [  60664659      59       1      3990], [  60614487      59       1      5950], [  68654655     166       1      5080]]')
	close()
