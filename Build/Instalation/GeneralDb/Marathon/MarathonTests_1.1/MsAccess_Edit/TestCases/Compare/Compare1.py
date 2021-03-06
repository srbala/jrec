useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		commonBits.selectOldFilemenu(select_menu, 'Utilities', 'Compare Menu')
		click('*1')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20041231_Compare.txt')
		select('FileChooser1', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click('Right')
		select('TabbedPane', '')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('Table', 'Content', '[[, Old, 2, D1, 17.0000, 0.0102, 2222500000000, , 43314531, 2075359, 45614531,  DONKEY 24-006607 SHWL WRAP CARD, , , , , , , , , , ], [, New, 2, , 7.0000, 0.0002, , , , , , , , , , , , , , , , ], [, Old, 3, S1, 5043, 10, 9045, 2, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [, New, 3, , , 1, 5045, 1, , , , , , , , , , , , , , ], [, Old, 4, D1, 14.0000, 148.3200, 0, , 5614944, 2075360, 5614944,  MILK 24-006607 SHWL WRAP CARD, , , , , , , , , , ], [, New, 4, , 4.0000, , , , , , , , , , , , , , , , , ], [, Old, 5, S1, 5045, 11, 5076, 1, 3331, 49440001, , 0, , 0, , 0, , 0, , 0, , 0], [, New, 5, , , 1, , , , , , , , , , , , , , , , ], [, Old, 6, D1, 8.0000, 48.3200, 0, , 55615071, 2075361, 55615071,  M.ROSE 24-006607 SHWL WRAP CARD, , , , , , , , , , ], [, New, 6, , 48.0000, 148.3200, , , , , , , , , , , , , , , , ], [, Old, 7, S1, 5036, 6, 5043, 51, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [, New, 7, , , 3, , 5, , , , , , , , , , , , , , ]]')
	
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Left')
		select('TabbedPane', '')
		select('Table', 'false', 'Include,0')
#		select('Table', 'cell:Include,0(false)')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('Table', 'Content', '[[, Old, 2, S1, 5043, 10, 9045, 2, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [, New, 2, , , 1, 5045, 1, , , , , , , , , , , , , , ], [, Old, 3, S1, 5045, 11, 5076, 1, 3331, 49440001, , 0, , 0, , 0, , 0, , 0, , 0], [, New, 3, , , 1, , , , , , , , , , , , , , , , ], [, Old, 4, S1, 5036, 6, 5043, 51, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [, New, 4, , , 3, , 5, , , , , , , , , , , , , , ]]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Left')
		select('TabbedPane', '')
		select('Table', 'cell:Include,0(false)')
		select('Table1', 'cell:Include,1(true)')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('Table', 'Content', '[[, Old, 2, D1, 0.0102, 2222500000000, , 43314531, 2075359, 45614531,  DONKEY 24-006607 SHWL WRAP CARD, , , , , , , , , , , ], [, New, 2, , 0.0002, , , , , , , , , , , , , , , , , ], [, Old, 3, S1, 5043, 10, 9045, 2, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [, New, 3, , , 1, 5045, 1, , , , , , , , , , , , , , ], [, Old, 5, S1, 5045, 11, 5076, 1, 3331, 49440001, , 0, , 0, , 0, , 0, , 0, , 0], [, New, 5, , , 1, , , , , , , , , , , , , , , , ], [, Old, 6, D1, 48.3200, 0, , 55615071, 2075361, 55615071,  M.ROSE 24-006607 SHWL WRAP CARD, , , , , , , , , , , ], [, New, 6, , 148.3200, , , , , , , , , , , , , , , , , ], [, Old, 7, S1, 5036, 6, 5043, 51, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [, New, 7, , , 3, , 5, , , , , , , , , , , , , , ]]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Left')
		select('TabbedPane', '')
		select('Table1', 'cell:Include,2(true)')
		select('Table', 'cell:Record,2(ams PO Download: Allocation)')
		select('Table1', 'cell:Include,1(true)')
		select('Table', 'cell:Record,2(ams PO Download: Allocation)')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('Table', 'Content', '[[, Old, 3, S1, 10, 9045, 2, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [, New, 3, , 1, 5045, 1, , , , , , , , , , , , , , ], [, Old, 5, S1, 11, 5076, 1, 3331, 49440001, , 0, , 0, , 0, , 0, , 0, , 0], [, New, 5, , 1, , , , , , , , , , , , , , , , ], [, Old, 7, S1, 6, 5043, 51, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [, New, 7, , 3, , 5, , , , , , , , , , , , , , ]]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Left')
		select('TabbedPane', '')
		select('Table1', 'cell:Include,2(true)')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('Table', 'Content', '[[, Old, 3, S1, 9045, 2, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [, New, 3, , 5045, 1, , , , , , , , , , , , , , ], [, Old, 7, S1, 5043, 51, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [, New, 7, , , 5, , , , , , , , , , , , , , ]]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()

