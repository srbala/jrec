useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoStoreSales3.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,2')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,3')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,6')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,7')
		select_menu('Expand Tree')
		select('LayoutCombo', 'Product')
		select('JTreeTable', 'rows:[9,10,11,12,13],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[9,10,11,12,13],columns:[Tree]')
		select('Table', 'cell:2|saleDate,1(40118)')
		assert_p('Table', 'Content', '[[69684558, 40118, -1, -19000], [69684558, 40118, 1, 5010], [69694158, 40118, 1, 19000], [69694158, 40118, -1, -19000], [69694158, 40118, 1, 5010]]')
		select('Table', 'cell:2|saleDate,1(40118)')
		rightclick('Table', '1|keycode,2')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|saleDate,1(40118)')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 69694158, 69694158], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 19000, 19000]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:2|saleDate,1(40118)')
		select('Table', 'cell:2|saleDate,1(40118)')
		select_menu('Window>>protoStoreSales3.bin>>Table:')
		select('Table', 'cell:2|saleDate,1(40118)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales3.bin>>Tree View')
		select('JTreeTable', 'rows:[9,10,11],columns:[Tree]')
		select_menu('View>>Record View #{Selected Records#}')
		select('JTreeTable', 'rows:[9,10,11],columns:[Tree]')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -19000, -19000]]')
		click('Right')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 5010, 5010]]')
		click('Right')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 69694158, 69694158], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 19000, 19000]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('JTreeTable', 'rows:[9,10,11,12],columns:[keycode]')
		select_menu('View>>Column View #{Selected Records#}')
		select('JTreeTable', 'rows:[9,10,11,12],columns:[keycode]')
		select('Table', 'cell:Row 1,1(40118)')
		assert_p('Table', 'Content', '[[69684558, 69684558, 69694158, 69694158], [40118, 40118, 40118, 40118], [-1, 1, 1, -1], [-19000, 5010, 19000, -19000]]')
		select('Table', 'cell:Row 2,1(40118)')
		rightclick('Table', 'Row 2,1')
		select_menu('Edit Record')
##		select('Table1', 'cell:Row 2,1(40118)')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 5010, 5010]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:Row 2,1(40118)')
		select('Table', 'cell:Row 2,1(40118)')
		select_menu('Window>>protoStoreSales3.bin>>Column Table')
		select('Table', 'cell:Row 2,1(40118)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

##		if window('Save Changes to file: ' + commonBits.sampleDir() + 'protoStoreSales3.bin'):
##			click('No')
##		close()
	close()
