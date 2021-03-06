useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click(commonBits.fl('Edit') + '1')
		select('Table', 'rows:[0,1,2,3,4,5,6,7,8,9,10,11,12],columns:[7 - 8|Pack Quantity 1]')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Table View #{Selected Records#}'))
##		select('Table2', 'rows:[0,1,2,3,4,5,6,7,8,9,10,11,12],columns:[7 - 8|Pack Quantity 1]')
		click('BaseDisplay$HeaderToolTips', '19 - 8|Pack Quantity 2')
		assert_p('BaseDisplay$HeaderToolTips', 'Text', '19 - 8|Pack Quantity 2', '19 - 8|Pack Quantity 2')
		click('BaseDisplay$HeaderToolTips', '1 - 2|Record Type')
		assert_p('BaseDisplay$HeaderToolTips', 'Text', '1 - 2|Record Type', '1 - 2|Record Type')
		click('BaseDisplay$HeaderToolTips', '3 - 4|DC Number 1')
		click('BaseDisplay$HeaderToolTips', '3 - 4|DC Number 1')
		assert_p('BaseDisplay$HeaderToolTips', 'Text', '3 - 4|DC Number 1', '3 - 4|DC Number 1')
		assert_p('Table', 'Content', '[[H1, 4534, 90000006, 602, 86225, , 200, 50, 10205010, 7596, 5, LAD, IES KNIC, FT, , , , , ], [D1, 0, 70000000, 0, 222, 4331, 45310000, 5, 45400000, 7, 207, 5359, , 4561, 4531, D, ONKEY 24, -6, 607 SHWL], [S1, 5043, 1, 5045, 1, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [D1, 0, 40000000, 1, 48320000, 0561, 49440000, 5, 45400000, 4, 207, 5360, , 5614, 944, M, ILK 24-0, 660, 7 SHWL W], [S1, 5045, 1, 5076, 1, 3331, 49440001, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 4, 80000000, 1, 48320000, 5561, 50710000, 5, 45400000, 48, 207, 5361, , 5561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5036, 3, 5043, 5, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [S1, 5151, 4, 5180, 3, 5173, 2, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 0, 40000000, 1, 48320000, 5561, 51560000, 5, 45400000, 4, 207, 5362, , 5561, 5156, A, QUA 24-0, 660, 7 SHWL W], [S1, 5043, 1, 5045, 1, 3331, 51560001, , 0, , 0, , 0, , 0, , 0, , 0], [H1, 4535, 6, 2280, 222, , 200, 50, 10205010, 7596, 6, LAD, IES KNIC, FT, , , , , ], [D1, 1, 60000006, 2281, 48320000, 0222, 45310000, 5, 45400000, 16, 207, 5348, , 5614, 531, D, ONKEY 24, -6, 607 SHWL], [S1, 5019, 1, 5037, 1, 5078, 1, 5085, 1, 5091, 1, 5093, 1, 5095, 1, 51 D, ONKEY 24, -6, 607 SHWL]]')
##		select('Table', '')
		rightclick('Table', '3 - 4|DC Number 1,4')
		click('PopupMenu', 23, 0)
		select('Table', 'cell:3 - 4|DC Number 1,4(5045)')
		assert_p('Table', 'Content', '[[H1, 4534, 90000006, 602, 86225, , 200, 50, 10205010, 7596, 5, LAD, IES KNIC, FT, , , , , ], [D1, 0, 70000000, 0, 222, 4331, 45310000, 5, 45400000, 7, 207, 5359, , 4561, 4531, D, ONKEY 24, -6, 607 SHWL], [S1, 5043, 1, 5045, 1, 5076, 1, 5079, 1, 5151, 1, 5072, 1, , 0, , 0, , 0], [D1, 0, 40000000, 1, 48320000, 0561, 49440000, 5, 45400000, 4, 207, 5360, , 5614, 944, M, ILK 24-0, 660, 7 SHWL W], [S1, 5045, 1, 5076, 1, 3331, 49440001, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 4, 80000000, 1, 48320000, 5561, 50710000, 5, 45400000, 48, 207, 5361, , 5561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5036, 3, 5043, 5, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [S1, 5151, 4, 5180, 3, 5173, 2, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 0, 40000000, 1, 48320000, 5561, 51560000, 5, 45400000, 4, 207, 5362, , 5561, 5156, A, QUA 24-0, 660, 7 SHWL W], [S1, 5043, 1, 5045, 1, 3331, 51560001, , 0, , 0, , 0, , 0, , 0, , 0], [H1, 4535, 6, 2280, 222, , 200, 50, 10205010, 7596, 6, LAD, IES KNIC, FT, , , , , ], [D1, 1, 60000006, 2281, 48320000, 0222, 45310000, 5, 45400000, 16, 207, 5348, , 5614, 531, D, ONKEY 24, -6, 607 SHWL], [S1, 5019, 1, 5037, 1, 5078, 1, 5085, 1, 5091, 1, 5093, 1, 5095, 1, 51 D, ONKEY 24, -6, 607 SHWL]]')
	close()
