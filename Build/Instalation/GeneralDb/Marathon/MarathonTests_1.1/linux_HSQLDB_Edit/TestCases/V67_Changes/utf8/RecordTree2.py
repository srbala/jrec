useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'utf8a_Ams_PODownload_20041231.txt')
		commonBits.setRecordLayout(select, 'utf8_ams PO Download')
		click('Edit1')
		select_menu('View>>Record Based Tree')
		select('Table', '1', 'Parent Record,0')
		select('Table', '0', 'Parent Record,2')
		select('Table', 'cell:Parent Record,2(0)')
		click('Build')
		select('LayoutCombo', 'ams PO Download: Header')
		select('JTreeTable', 'cell:Sequence Number,3(45.352)')
		assert_p('JTreeTable', 'Content', '[[, , H1, 45.349, 6060, 286225, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.350, 6228, 222227, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.351, 6228, 222243, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.352, 5341, 294915, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.353, 5341, 294987, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.354, 5341, 295139, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.355, 5341, 303662, 041110, , 00, , 310, 041231, 050107, P, , , YOUTH SHOE, C, FT], [, , H1, 45.356, 5341, 304100, 041111, , 00, , 310, 041231, 050107, P, , , YOUTH SHOE, C, FT]]')
		select('JTreeTable', 'cell:Sequence Number,3(45.352)')
		rightclick('JTreeTable', 'Sequence Number,3')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Sequence Number,4(0.030)')
		assert_p('JTreeTable', 'Text', '45.353', 'Sequence Number,5')
		select('JTreeTable', 'cell:PO,4(292680000000)')
		assert_p('JTreeTable', 'Content', '[[, , H1, 45.349, 6060, 286225, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.350, 6228, 222227, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.351, 6228, 222243, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.352, 5341, 294915, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , D1, 0.030, 0, 292680000000, 000000, 00 45846, 68, 00, 0000, 007272, 000003, ,    212, 0, 736, , 45], [, , H1, 45.353, 5341, 294987, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.354, 5341, 295139, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.355, 5341, 303662, 041110, , 00, , 310, 041231, 050107, P, , , YOUTH SHOE, C, FT], [, , H1, 45.356, 5341, 304100, 041111, , 00, , 310, 041231, 050107, P, , , YOUTH SHOE, C, FT]]')
		select('JTreeTable', 'cell:PO,4(292680000000)')
		rightclick('JTreeTable', 'Sequence Number,4')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:PO,4(292680000000)')
		assert_p('JTreeTable', 'Text', '292680000000', 'PO,4')
		select('JTreeTable', 'cell:PO,5(300000003504)')
		assert_p('JTreeTable', 'Content', '[[, , H1, 45.349, 6060, 286225, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.350, 6228, 222227, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.351, 6228, 222243, 040909, , 00, , 200, 050102, 050107, , , , LADIES KNI, C, FT], [, , H1, 45.352, 5341, 294915, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , D1, 0.030, 0, 292680000000, 000000, 00 45846, 68, 00, 0000, 007272, 000003, ,    212, 0, 736, , 45], [, , S1, 50.360, 2504, 300000003504, 500000, 00350570, 00, 00, 0015, 065000, 000025, 0, 000002, 5, 0760000000, 3, 50], [, , S1, 51.510, 3518, 2507, 200000, 00151730, 00, 00, 001,    000, 00000, 0, 000000, ,    0000000, 0, ], [, , H1, 45.353, 5341, 294987, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.354, 5341, 295139, 041013, , 00, , 475, 041231, 050107, P, , , WOMENS SHO, C, FT], [, , H1, 45.355, 5341, 303662, 041110, , 00, , 310, 041231, 050107, P, , , YOUTH SHOE, C, FT], [, , H1, 45.356, 5341, 304100, 041111, , 00, , 310, 041231, 050107, P, , , YOUTH SHOE, C, FT]]')
		select('JTreeTable', 'cell:Tree,8(null)')
		rightclick('JTreeTable', 'Tree,8')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Sequence Number,9(0.025)')
		rightclick('JTreeTable', 'Sequence Number,9')
		select_menu('Expand Tree')
		select('LayoutCombo', 'ams PO Download: Allocation')
		select('JTreeTable', 'cell:DC Number 2,10(5043)')
		assert_p('JTreeTable', 'Text', '5180', 'DC Number 2,11')
		select('JTreeTable', 'cell:DC Number 2,11(5180)')
		assert_p('JTreeTable', 'Content', '[[, , H1, 4534, 90000006, 602, 86225, , 200, 50, 10205010, 7596, 5, LAD, IES KNIC, FT, , , , , ], [, , H1, 4535, 6, 2280, 222, , 200, 50, 10205010, 7596, 6, LAD, IES KNIC, FT, , , , , ], [, , H1, 4535, 10000006, 2280, 222, , 200, 50, 10205010, 7596, 8, LAD, IES KNIC, FT, , , , , ], [, , H1, 4535, 20000005, 3412, 94915, , 475, 41, 23105010, 7596, 5P, WOM, ENS SHOC, FT, , , , , ], [, , D1, 3, 0, 2, 92680000, 4584, 66800000, 7, 27200000, 30, 212, 736, , 4561, 5156, C, ONCERTO, BLAC, K LEATHE], [, , S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 3, 5079, 1, 5094, 3, 5128, 3], [, , S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [, , H1, 4535, 30000005, 3412, 94987, , 475, 41, 23105010, 7596, 5P, WOM, ENS SHOC, FT, , , , , ], [, , H1, 4535, 40000005, 3412, 95139, , 475, 41, 23105010, 7596, 5P, WOM, ENS SHOC, FT, , , , , ], [, , D1, 2, 50000000, 4, 65480000, 4584, 87070000, 9, 9000000, 25, 217, 9843, , 4584, 8707A, A, NGEL PIN, K SY, NTHETIC], [, , S1, 5036, 2, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [, , S1, 5151, 2, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [, , H1, 4535, 50000005, 3413, 3662, , 310, 41, 23105010, 7596, 5P, YOU, TH SHOEC, FT, , , , , ], [, , H1, 4535, 60000005, 3413, 4100, , 310, 41, 23105010, 7596, 5P, YOU, TH SHOEC, FT, , , , , ]]')
	close()