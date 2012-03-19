useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click('Edit1')
		select_menu('View>>Record Based Tree')
		select('Table', '1', 'Parent Record,0')
		select('Table', '0', 'Parent Record,2')
		select('Table', 'cell:Parent Record,2(0)')
		click('Build')
		select('JTreeTable', 'cell:Record Type,0(H1)')
		click('Delete1')
		select_menu('View>>Table View #{Selected Records#}')
		select_menu('Window>>Ams_PODownload_20041231.txt>>Table: ')
		select('Table', 'cell:15 - 4|DC Number 2,0(2280)')
		select('LayoutCombo', 'ams PO Download: Header')
		select('Table', 'cell:18 - 12|PO,0(222227)')
		assert_p('Table', 'Text', '222227', '18 - 12|PO,0')
		select('Table', 'cell:8 - 10|Vendor,1(6228)')
		assert_p('Table', 'RowCount', '60')
		select('Table', 'cell:8 - 10|Vendor,1(6228)')
		select_menu('Window>>Ams_PODownload_20041231.txt>>Tree View')
		select('Table', 'cell:8 - 10|Vendor,1(6228)')
		#select('JTreeTable', '')
		rightclick('JTreeTable', 'Sequence Number,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Sequence Number,2(0.006)')
		rightclick('JTreeTable', 'Sequence Number,2')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Sequence Number,4(0.003)')
		rightclick('JTreeTable', 'Sequence Number,4')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Sequence Number,6(0.044)')
		rightclick('JTreeTable', 'Sequence Number,6')
		select_menu('Expand Tree')
		select('JTreeTable', 'rows:[7,8],columns:[Record Type]')
		click('Delete1')
		select('JTreeTable', 'rows:[3,4,5],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[3,4,5],columns:[Tree]')
		select('Table', 'cell:7 - 8|Pack Quantity 1,0(30000000)')
		assert_p('Table', 'Text', '1', '7 - 8|Pack Quantity 1,1')
		select('Table', 'cell:7 - 8|Pack Quantity 1,2(40000000)')
		#assert_p('Table', 'Text', '40000000', '7 - 8|Pack Quantity 1,2')
		select('Table', 'cell:7 - 8|Pack Quantity 1,3(30000000)')
		#assert_p('Table', 'Content', '[[D1, 0, 30000000, 1, 48320000, 4561, 49440000, 5, 45400000, 3, 207, 5353, , 4561, 4944, M, ILK 24-0, 660, 7 SHWL W], [S1, 5009, 1, 5021, 1, , 0, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 4, 40000000, 1, 48320000, 4561, 50710000, 5, 45400000, 44, 207, 5354, , 4561, 5071, M, .ROSE 24, -6, 607 SHWL], [D1, 0, 30000000, 1, 48320000, 4561, 51560000, 5, 45400000, 3, 207, 5355, , 3561, 5156, A, QUA 24-0, 660, 7 SHWL W], [S1, 5009, 1, 5021, 1, , 0, , 0, , 0, , 0, , 0, , 0, , 0]]')
		select('Table', 'cell:7 - 8|Pack Quantity 1,1(1)')
		#assert_p('Table', 'RowCount', '5')
		select('Table', 'cell:7 - 8|Pack Quantity 1,1(1)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:18 - 12|PO,2(700000001507)')
		assert_p('Table', 'RowCount', '58')
		select('Table', 'cell:18 - 12|PO,2(700000001507)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'Ams_PODownload_20041231.txt'):
			click('No')
		close()
	close()