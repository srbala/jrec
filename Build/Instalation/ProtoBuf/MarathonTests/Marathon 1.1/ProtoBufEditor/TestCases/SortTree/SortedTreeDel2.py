useFixture(default)

### Problems !!!


def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'protoSales.bin')
		click('Edit1')
		select_menu('View>>Sorted Field Tree')
		##select('List', 'sale')
		select('Table', 'store', 'Field,0')
		select('Table', 'department', 'Field,1')
		select('Table', 'cell:Field,1(department)')
		click('Build Tree')
		select('JTreeTable', 'cell:keycode,2(null)')
		rightclick('JTreeTable', 'store,2')
		select_menu('Delete Record#{s#}')
		#select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Tree,8(null)')
		rightclick('JTreeTable', 'Tree,8')
		select_menu('Expand Tree')
		select('JTreeTable', 'rows:[7,8,9],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[7,8,9],columns:[Tree]')
		select('LinesTbl', 'cell:1|keycode,0(64614401)')
		assert_p('LinesTbl', 'Text', '59', '2|store,1')
		select('LinesTbl', 'cell:1|keycode,3(64624770)')
##		assert_p('LinesTbl', 'Content', '[[64614401, 59, 957, 40118, 1, 1990], [64614401, 59, 957, 40118, 1, 1990], [62684217, 59, 957, 40118, 1, 9990], [64624770, 59, 957, 40118, 1, 2590], [60664048, 184, 60, 40118, -1, -4800], [60614866, 184, 60, 40118, -1, -4800], [60664048, 184, 60, 40118, -1, -4800], [60664048, 184, 60, 40118,-1, -4800], [60614866, 184, 60, 40118, -1, -4800], [67644821, 184, 60, 40118, -1, -14990], [67644118, 184, 60, 40118, 1, 16990], [69654459, 184, 60, 40118, 1, 5080], [60664779, 184, 60, 40118,1, 5080], [68644941, 184, 60, 40118, -1, -10390], [68644941, 184, 60, 40118, -1, -10390], [68644941, 184, 60, 40118, -1, -10390], [68644941, 184, 60, 40118, -1, -10390], [68644934, 184, 60, 40118,1, 10390], [69654638, 184, 60, 40118,1, 6000], [67634923, 184, 60, 40118,1, 17590]]')
		assert_p('LinesTbl', 'Content', '[[64614401, 59, 957, 40118, 1, 1990], [64614401, 59, 957, 40118, 1, 1990], [62684217, 59, 957, 40118, 1, 9990], [64624770, 59, 957, 40118, 1, 2590], [60664048, 184, 60, 40118, -1, -4800], [60614866, 184, 60, 40118, -1, -4800], [60664048, 184, 60, 40118, -1, -4800], [60664048, 184, 60, 40118, -1, -4800], [60614866, 184, 60, 40118, -1, -4800], [67644821, 184, 60, 40118, -1, -14990], [67644118, 184, 60, 40118, 1, 16990], [69654459, 184, 60, 40118, 1, 5080], [60664779, 184, 60, 40118, 1, 5080], [68644941, 184, 60, 40118, -1, -10390], [68644941, 184, 60, 40118, -1, -10390], [68644941, 184, 60, 40118, -1, -10390], [68644941, 184, 60, 40118, -1, -10390], [68644934, 184, 60, 40118, 1, 10390], [69654638, 184, 60, 40118, 1, 6000], [67634923, 184, 60, 40118, 1, 17590]]')
		select('LinesTbl', 'cell:1|keycode,15(68644941)')
		assert_p('LinesTbl', 'Text', '68644934', '1|keycode,17')
		select('LinesTbl', 'cell:1|keycode,4(60664048)')
		assert_p('LinesTbl', 'Text', '60664048', '1|keycode,4')
		select('LinesTbl', 'cell:1|keycode,3(64624770)')
		assert_p('LinesTbl', 'Text', '60664048', '1|keycode,4')
		select('LinesTbl', 'cell:1|keycode,3(64624770)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoSales.bin>>Table:')
		select('LinesTbl', 'cell:1|keycode,7(62684671)')
		assert_p('LinesTbl', 'RowCount', '233')
		select('LinesTbl', 'cell:1|keycode,7(62684671)')
		select_menu('Window>>protoSales.bin>>Tree View')
##		select('Table', 'cell:1|keycode,7(62684671)')
		select('JTreeTable', 'cell:Tree,8(null)')
		rightclick('JTreeTable', 'Tree,8')
		select('JTreeTable', 'cell:Tree,4(null)')
		rightclick('JTreeTable', 'Tree,4')
		select_menu('Delete Record#{s#}')
		select('JTreeTable', 'rows:[3,4],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
##		select('JTreeTable', 'rows:[3,4],columns:[Tree]')
		select('LinesTbl', 'cell:1|keycode,0(68634752)')
		assert_p('LinesTbl', 'Content', '[[68634752, 59, 410, 40118, 1, 8990], [60614487, 59, 878, 40118, 1, 5950], [63644339, 59, 878, 40118, 1, 12650]]')
		select('LinesTbl', 'cell:3|department,1(878)')
		assert_p('LinesTbl', 'Text', 'cell:3|department,1(878)')
		select('LinesTbl', 'cell:4|saleDate,2(40118)')
		assert_p('LinesTbl', 'RowCount', '3')
		select('LinesTbl', 'cell:4|saleDate,2(40118)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoSales.bin>>Table:')
		select('LinesTbl', 'cell:1|keycode,5(69694158)')
		assert_p('LinesTbl', 'RowCount', '231')
		select('LinesTbl', 'cell:1|keycode,5(69694158)')
		select_menu('Window>>protoSales.bin>>Tree View')
		select('LinesTbl', 'cell:1|keycode,5(69694158)')
		select('JTreeTable', 'cell:Tree,0(null)')
		click('Delete1')
		select('JTreeTable', 'cell:keycode,0(null)')
		rightclick('JTreeTable', 'keycode,0')
		select_menu('Expand Tree')
		select('JTreeTable', 'rows:[1,2],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[1,2],columns:[Tree]')
		select('LinesTbl', 'cell:1|keycode,0(61664713)')
		assert_p('LinesTbl', 'Content', '[[61664713, 59, 335, 40118, 1, 17990], [61664713, 59, 335, 40118, -1, -17990], [61684613, 59, 335, 40118, 1, 12990], [68634752, 59, 410, 40118, 1, 8990]]')
		select('LinesTbl', 'cell:1|keycode,3(68634752)')
		assert_p('LinesTbl', 'Text', '68634752', '1|keycode,3')
		select('LinesTbl', 'cell:3|department,0(335)')
		assert_p('LinesTbl', 'Text', '335', '3|department,0')
		select('LinesTbl', 'cell:3|department,0(335)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('LinesTbl', 'cell:1|keycode,0(64614401)')
		assert_p('LinesTbl', 'Text', '64614401', '1|keycode,1')
		select('LinesTbl', 'cell:1|keycode,3(61664713)')
		assert_p('LinesTbl', 'RowCount', '218')
		select('LinesTbl', 'cell:1|keycode,3(61664713)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'protoSales.bin'):
			click('No')
		close()
	close()
