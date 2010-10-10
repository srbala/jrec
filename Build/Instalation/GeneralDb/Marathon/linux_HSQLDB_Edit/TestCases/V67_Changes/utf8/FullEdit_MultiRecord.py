useFixture(default)

def test():
	from Modules import commonBits

	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		click('Choose File')

		if window('Open'):
			select(commonBits.selectPane(), 'utf8a_Ams_PODownload_20041231.txt')
			click('Open')
		close()

		commonBits.setRecordLayout(select, 'utf8_ams PO Download')
		click('Edit1')
		select('Table', 'cell:3 - 4|DC Number 1,0(4534)')
		rightclick('Table', '3 - 4|DC Number 1,0')
		select_menu('Edit Record')
##		select('Table1', 'cell:3 - 4|DC Number 1,0(4534)')
		select('Table', 'cell:Data,2(6060)')
		assert_p('Table', 'Text', '6060', 'Data,2')
		select('Table', 'cell:Data,3(286225)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, H1, H1], [Sequence Number, 3, 5, 45.349, 45349], [Vendor, 8, 10, 6060, 0000006060], [PO, 18, 12, 286225, 286225], [Entry Date, 30, 6, 040909, 040909], [Filler, 36, 8, , ], [beg01 code, 44, 2, 00, 00], [beg02 code, 46, 2, , ], [Department, 48, 4, 200, 200], [Expected Reciept Date, 52, 6, 050102, 050102], [Cancel by date, 58, 6, 050107, 050107], [EDI Type, 68, 1, , ], [Add Date, 69, 6, , ], [Filler, 75, 1, , ], [Department Name, 76, 10, LADIES KNI, LADIES KNI], [Prcoess Type, 86, 1, C, C], [Order Type, 87, 2, FT, FT]]')
		select('Table', 'cell:Data,3(286225)')
		assert_p('Table', 'RowCount', '17')
		select('Table', 'cell:Data,3(286225)')
		click('Right')
		select('Table', 'cell:Field,3(APN)')
		assert_p('Table', 'Text', 'APN', 'Field,3')
		select('Table', 'cell:Field,3(APN)')
		select('Table', 'cell:Field,5(Product)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, D1, D1], [Pack Qty, 3, 9, 7.0000, 000070000], [Pack Cost, 12, 13, 0.0002, 0000000000002], [APN, 25, 13, 2222500000000, 2222500000000], [Filler, 38, 1, , ], [Product, 39, 8, 43314531, 43314531], [pmg dtl tech key, 72, 15, 2075359, 2075359], [Case Pack id, 87, 15, 45614531, 45614531], [Product Name, 101, 50,  DONKEY 24-006607 SHWL WRAP CARD,  DONKEY 24-006607 SHWL WRAP CARD]]')
		select('Table', 'cell:Field,8(Product Name)')
		assert_p('Table', 'RowCount', '9')
		select('Table', 'cell:Field,8(Product Name)')
		click('Right')
		select('Table', 'cell:Data,0(S1)')
		assert_p('Table', 'RowCount', '19')
		select('Table', 'cell:Data,0(S1)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, S1, S1], [DC Number 1, 3, 4, 5043, 5043], [Pack Quantity 1, 7, 8, 1, 00000001], [DC Number 2, 15, 4, 5045, 5045], [Pack Quantity 2, 19, 8, 1, 00000001], [DC Number 4, 39, 4, 5076, 5076], [Pack Quantity 4, 43, 8, 1, 00000001], [DC Number 5, 51, 4, 5079, 5079], [Pack Quantity 5, 55, 8, 1, 00000001], [DC Number 6, 63, 4, 5151, 5151], [Pack Quantity 6, 67, 8, 1, 00000001], [DC Number 7, 75, 4, 5072, 5072], [Pack Quantity 7, 79, 8, 1, 00000001], [DC Number 8, 87, 4, , ], [Pack Quantity 8, 91, 8, 0, 00000000], [DC Number 9, 99, 4, , ], [Pack Quantity 9, 103, 8, 0, 00000000], [DC Number 10, 111, 4, , ], [Pack Quantity 10, 115, 8, 0, 00000000]]')
		select('Table', 'cell:Data,11(5072)')
		assert_p('Table', 'Text', '5072', 'Data,11')
		select('Table', 'cell:Data,11(5072)')
		click('Right')
		select('Table', 'cell:Data,8( MILK 24-006607 SHWL WRAP CARD)')
		assert_p('Table', 'Text', ' MILK 24-006607 SHWL WRAP CARD', 'Data,8')
		select('Table', 'cell:Data,8( MILK 24-006607 SHWL WRAP CARD)')
		select('Table', 'cell:Data,7(5614944)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, D1, D1], [Pack Qty, 3, 9, 4.0000, 000040000], [Pack Cost, 12, 13, 148.3200, 0000001483200], [APN, 25, 13, 0, 0000000000000], [Filler, 38, 1, , ], [Product, 39, 8, 5614944, 05614944], [pmg dtl tech key, 72, 15, 2075360, 2075360], [Case Pack id, 87, 15, 5614944, 5614944], [Product Name, 101, 50,  MILK 24-006607 SHWL WRAP CARD,  MILK 24-006607 SHWL WRAP CARD]]')
		select('Table', 'cell:Data,6(2075360)')
		assert_p('Table', 'RowCount', '9')
		select('Table', 'cell:Data,6(2075360)')
		click('Right')
		select('Table', 'cell:Data,6(49440001)')
		assert_p('Table', 'Text', '49440001', 'Data,6')
		select('Table', 'cell:Data,1(5045)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, S1, S1], [DC Number 1, 3, 4, 5045, 5045], [Pack Quantity 1, 7, 8, 1, 00000001], [DC Number 2, 15, 4, 5076, 5076], [Pack Quantity 2, 19, 8, 1, 00000001], [DC Number 4, 39, 4, 3331, 3331], [Pack Quantity 4, 43, 8, 49440001, 49440001], [DC Number 5, 51, 4, , ], [Pack Quantity 5, 55, 8, 0, 00000000], [DC Number 6, 63, 4, , ], [Pack Quantity 6, 67, 8, 0, 00000000], [DC Number 7, 75, 4, , ], [Pack Quantity 7, 79, 8, 0, 00000000], [DC Number 8, 87, 4, , ], [Pack Quantity 8, 91, 8, 0, 00000000], [DC Number 9, 99, 4, , ], [Pack Quantity 9, 103, 8, 0, 00000000], [DC Number 10, 111, 4, , ], [Pack Quantity 10, 115, 8, 0, 00000000]]')
		select('Table', 'cell:Data,1(5045)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Filter')
		select('Table', 'false', 'Include,1')
		select('Table', 'false', 'Include,2')
		click('Filter')
		select('Table', 'cell:12 - 13|Pack Cost,1(148.3200)')
		assert_p('Table', 'Text', '148.3200', '12 - 13|Pack Cost,1')
		select('Table', 'cell:12 - 13|Pack Cost,1(148.3200)')
##		assert_p('Table', 'Content', '[[D1, 7.0000, 0.0002, 2222500000000, , 43314531, 2075359, 45614531,  DONKEY 24-006607 SHWL WRAP CARD], [D1, 4.0000, 148.3200, 0, , 5614944, 2075360, 5614944,  MILK 24-006607 SHWL WRAP CARD], [D1, 48.0000, 148.3200, 0, , 55615071, 2075361, 55615071,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 4.0000, 148.3200, 0, , 55615156, 2075362, 55615156,  AQUA 24-006607 SHWL WRAP CARD], [D1, 16.0000, 62281483200, 2222, , 2224531, 2075348, 5614531,  DONKEY 24-006607 SHWL WRAP CARD], [D1, 8.0000, 148.3200, 0, , 62224944, 2075349, 65614944,  MILK 24-006607 SHWL WRAP CARD], [D1, 108.0000, 148.3200, 0, , 62225071, 2075350, 65615071,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 8.0000, 148.3200, 0, , 52225156, 2075351, 55615156,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 6.0000, 148.3200, 0, , 45614531, 2075352, 45614531,  DONKEY 24-006607 SHWL WRAP CARD], [D1, 3.0000, 148.3200, 0, , 45614944, 2075353, 45614944,  MILK 24-006607 SHWL WRAP CARD], [D1, 44.0000, 148.3200, 0, , 45615071, 2075354, 45615071,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 3.0000, 148.3200, 0, , 45615156, 2075355, 35615156,  AQUA 24-006607 SHWL WRAP CARD], [D1, 30.0000, 292.6800, 0, , 45846680, 2120736, 45615156,  CONCERTO BLACK LEATHER ANKLE BOOT], [D1, 29.0000, 198.3600, 0, , 45846772, 2121104, 5846772,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 29.0000, 198.3600, 0, , 45847489, 2121627, 45847489,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 25.0000, 465.4800, 0, , 45848707, 2179843, 45848707A,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 8.0000, 82.1600, 0, , 46164790, 2203070, 46164790B8,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 24.0000, 112.9700, 0, , 46164790, 2203056, 46164790,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 7.0000, 82.1600, 0, , 46165360, 2203075, 46165360B8,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 23.0000, 112.9700, 0, , 46165360, 2203072, 46165360,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 8.0000, 83.8400, 0, , 45928553, 2203222, 45928553B8,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 22.0000, 125.7600, 0, , 45928553, 2203219, 45928553,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 22.0000, 125.7600, 0, , 15935759, 2203223, 05935759,  JAZZ DUSTY PINK HEELED PEEP TOE], [D1, 7.0000, 83.8400, 0, , 45935759, 2203224, 45935759B8,  JAZZ DUSTY PINK HEELED PEEP TOE]]')
		assert_p('Table', 'Content', '[[D1, 7.0000, 0.0002, 2222500000000, , 43314531, 2075359, 45614531,  DONKEY 24-006607 SHWL WRAP CARD], [D1, 4.0000, 148.3200, 0, , 5614944, 2075360, 5614944,  MILK 24-006607 SHWL WRAP CARD], [D1, 48.0000, 148.3200, 0, , 55615071, 2075361, 55615071,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 4.0000, 148.3200, 0, , 55615156, 2075362, 55615156,  AQUA 24-006607 SHWL WRAP CARD], [D1, 16.0000, 6228148.3200, 2222, , 2224531, 2075348, 5614531,  DONKEY 24-006607 SHWL WRAP CARD], [D1, 8.0000, 148.3200, 0, , 62224944, 2075349, 65614944,  MILK 24-006607 SHWL WRAP CARD], [D1, 108.0000, 148.3200, 0, , 62225071, 2075350, 65615071,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 8.0000, 148.3200, 0, , 52225156, 2075351, 55615156,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 6.0000, 148.3200, 0, , 45614531, 2075352, 45614531,  DONKEY 24-006607 SHWL WRAP CARD], [D1, 3.0000, 148.3200, 0, , 45614944, 2075353, 45614944,  MILK 24-006607 SHWL WRAP CARD], [D1, 44.0000, 148.3200, 0, , 45615071, 2075354, 45615071,  M.ROSE 24-006607 SHWL WRAP CARD], [D1, 3.0000, 148.3200, 0, , 45615156, 2075355, 35615156,  AQUA 24-006607 SHWL WRAP CARD], [D1, 30.0000, 292.6800, 0, , 45846680, 2120736, 45615156,  CONCERTO BLACK LEATHER ANKLE BOOT], [D1, 29.0000, 198.3600, 0, , 45846772, 2121104, 5846772,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 29.0000, 198.3600, 0, , 45847489, 2121627, 45847489,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 25.0000, 465.4800, 0, , 45848707, 2179843, 45848707A,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 8.0000, 82.1600, 0, , 46164790, 2203070, 46164790B8,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 24.0000, 112.9700, 0, , 46164790, 2203056, 46164790,  ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT], [D1, 7.0000, 82.1600, 0, , 46165360, 2203075, 46165360B8,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 23.0000, 112.9700, 0, , 46165360, 2203072, 46165360,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 8.0000, 83.8400, 0, , 45928553, 2203222, 45928553B8,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 22.0000, 125.7600, 0, , 45928553, 2203219, 45928553,  CABERETCARAMEL MICRO SUEDE PEEP TOE], [D1, 22.0000, 125.7600, 0, , 15935759, 2203223, 05935759,  JAZZ DUSTY PINK HEELED PEEP TOE], [D1, 7.0000, 83.8400, 0, , 45935759, 2203224, 45935759B8,  JAZZ DUSTY PINK HEELED PEEP TOE]]')
		select('Table', 'cell:12 - 13|Pack Cost,1(148.3200)')
		select('Table', 'cell:12 - 13|Pack Cost,4(62281483200)')
		assert_p('Table', 'RowCount', '24')
		select('Table', 'cell:12 - 13|Pack Cost,5(148.3200)')
		assert_p('Table', 'ColumnCount', '9')
		select('Table', 'cell:12 - 13|Pack Cost,5(148.3200)')
		select('LayoutCombo', 'Full Line')
		select('Table', 'cell:Full Line,3(D100004000000000014832000000000000000 55615156000000054540000004       2075362        55615156       AQUA 24-006607 SHWL WRAP CARD                     )')
		assert_p('Table', 'Text', 'D100048000000000014832000000000000000 55615071000000054540000048       2075361        55615071       M.ROSE 24-006607 SHWL WRAP CARD                   ', 'Full Line,2')
		select('Table', 'cell:Full Line,4(D100016000000622814832000000000002222 02224531000000054540000016       2075348        5614531        DONKEY 24-006607 SHWL WRAP CARD                   )')
		assert_p('Table', 'ColumnCount', '1')
		select('Table', 'cell:Full Line,0(D100007000000000000000022222500000000 43314531000000054540000007       2075359        45614531       DONKEY 24-006607 SHWL WRAP CARD                   )')
		assert_p('Table', 'Text', 'cell:Full Line,0(D100007000000000000000022222500000000 43314531000000054540000007       2075359        45614531       DONKEY 24-006607 SHWL WRAP CARD                   )')
		select('Table', 'cell:Full Line,1(D100004000000000014832000000000000000 05614944000000054540000004       2075360        5614944        MILK 24-006607 SHWL WRAP CARD                     )')
		assert_p('Table', 'Text', 'cell:Full Line,1(D100004000000000014832000000000000000 05614944000000054540000004       2075360        5614944        MILK 24-006607 SHWL WRAP CARD                     )')
		select('Table', 'cell:Full Line,3(D100004000000000014832000000000000000 55615156000000054540000004       2075362        55615156       AQUA 24-006607 SHWL WRAP CARD                     )')
		assert_p('Table', 'Text', 'cell:Full Line,3(D100004000000000014832000000000000000 55615156000000054540000004       2075362        55615156       AQUA 24-006607 SHWL WRAP CARD                     )')
		select('LayoutCombo', 'ams PO Download: Detail')
		rightclick('Table', '3 - 9|Pack Qty,0')
		select_menu('Edit Record')
		select('Table', 'cell:Data,8( DONKEY 24-006607 SHWL WRAP CARD)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, D1, D1], [Pack Qty, 3, 9, 7.0000, 000070000], [Pack Cost, 12, 13, 0.0002, 0000000000002], [APN, 25, 13, 2222500000000, 2222500000000], [Filler, 38, 1, , ], [Product, 39, 8, 43314531, 43314531], [pmg dtl tech key, 72, 15, 2075359, 2075359], [Case Pack id, 87, 15, 45614531, 45614531], [Product Name, 101, 50,  DONKEY 24-006607 SHWL WRAP CARD,  DONKEY 24-006607 SHWL WRAP CARD]]')
		select('Table', 'cell:Data,8( DONKEY 24-006607 SHWL WRAP CARD)')
		click('Right')
		select('Table', 'cell:Data,8( MILK 24-006607 SHWL WRAP CARD)')
		assert_p('Table', 'Text', ' MILK 24-006607 SHWL WRAP CARD', 'Data,8')
		select('Table', 'cell:Data,8( MILK 24-006607 SHWL WRAP CARD)')
		click('Right')
		select('Table', 'cell:Data,8( M.ROSE 24-006607 SHWL WRAP CARD)')
		assert_p('Table', 'Text', 'cell:Data,8( M.ROSE 24-006607 SHWL WRAP CARD)')
		select('Table', 'cell:Data,8( M.ROSE 24-006607 SHWL WRAP CARD)')
		click('Right')
		select('Table', 'cell:Data,7(55615156)')
		assert_p('Table', 'Text', 'cell:Data,7(55615156)')
		select('Table', 'cell:Data,7(55615156)')
		click('RightM')
		select('Table', 'cell:Data,8( JAZZ DUSTY PINK HEELED PEEP TOE)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, D1, D1], [Pack Qty, 3, 9, 7.0000, 000070000], [Pack Cost, 12, 13, 83.8400, 0000000838400], [APN, 25, 13, 0, 0000000000000], [Filler, 38, 1, , ], [Product, 39, 8, 45935759, 45935759], [pmg dtl tech key, 72, 15, 2203224, 2203224], [Case Pack id, 87, 15, 45935759B8, 45935759B8], [Product Name, 101, 50,  JAZZ DUSTY PINK HEELED PEEP TOE,  JAZZ DUSTY PINK HEELED PEEP TOE]]')
		select('Table', 'cell:Data,8( JAZZ DUSTY PINK HEELED PEEP TOE)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
