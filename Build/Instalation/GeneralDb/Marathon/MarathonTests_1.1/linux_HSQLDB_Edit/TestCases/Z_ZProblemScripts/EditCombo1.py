useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_Receipt.txt')
		click('Edit1')
		select('Table', 'cell:3 - 3|Brand Id Rs,0(STD)')
		rightclick('Table', '3 - 3|Brand Id Rs,0')
		select_menu('Edit Record')
		select('Table', 'cell:Data,0(FH)')
		assert_p('Table', 'Text', 'File Header (FH)', 'Data,0')
		select('Table', 'cell:Text,0(FH)')
		assert_p('Table', 'Text', 'cell:Text,0(FH)')
		select('Table', 'cell:Text,1(STD)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, FH, FH], [Brand Id Rs, 3, 3, STD, STD], [Order No, 6, 12, REC01TAR05/0, REC01TAR05/0], [Receipt Location, 18, 4, 3/20, 3/20], [Prod No, 31, 14, 9, 9], [Keycode, 45, 8, , ], [Sequence No, 53, 5, , ], [Store No, 58, 4, , ], [Receive Alc Qty, 62, 9, , ], [Outstanding Ord Qty, 71, 9, , ], [C Usr Updt, 80, 8, , ], [Ts Updt, 88, 26, , ], [Act Recv Qty, 114, 9, , ], [Filler, 123, 228, , ]]')
		select('Table', 'cell:Data,0(FH)')
		assert_p('Table', 'Text', 'cell:Data,0(FH)')
		click('Right')
		select('Table', 'cell:Data,0(RH)')
		assert_p('Table', 'Text', 'Receipt Header (RH)', 'Data,0')
		select('Table', 'cell:Text,0(RH)')
		assert_p('Table', 'Text', 'cell:Text,0(RH)')
		select('Table', 'cell:Text,1(TAR)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, RH, RH], [Brand Id Rs Rh, 3, 3, TAR, TAR], [Order No Rh, 6, 12, 297853, 297853], [Receipt Locn Rh, 18, 4, 9601, 9601], [Sup Id Rh, 31, 8, 1122, 00001122], [Receipt Date Rh, 39, 10, 04.03.2005, 04.03.2005], [Receipt Time Rh, 49, 8, 20.28.10, 20.28.10], [Brand Xref Rh, 57, 5, 0, 00000], [Brand Dc No Rh, 62, 4, 5965, 5965], [Rcpt Final Stat Rh, 66, 1, I, I], [Processed Ind Rh, 67, 1, N, N], [Asn Rh, 68, 30, , ], [Asn Seq No Rh, 98, 9, 0, 000000000], [Smpl Chck Ctn Rh, 107, 7, 0, 0000000], [Smpl Chck U Rh, 114, 11, 0.00, 00000000000], [Invoice No Rh, 125, 20, , ], [Tot Rcpt Amt Rh, 145, 9, 1377.60, 000137760], [Tot Recv Qty Rh, 154, 9, 28, 000000028], [Tot Outers Rh, 163, 11, 28.00, 00000002800], [Carrier Connote Rh, 174, 20, , ], [Ers Status Rh, 194, 1, N, N], [Chk Result Adjd Rh, 195, 1, N, N], [Brand Stk Upd Rh, 196, 1, Y, Y], [Orginl Scm Cnt Rh, 197, 7, 28, 0000028], [Pick Pack Ind Rh, 204, 1, , ], [C Usr Updt Rh, 205, 8, L9601008, L9601008], [Ts Updt Rh, 213, 26, 2005-03-04-20.34.46.709398, 2005-03-04-20.34.46.709398], [Rh Num Rd, 239, 9, 1, 000000001], [Rh Num As, 248, 9, 0, 000000000], [Rh Filler, 257, 94, , ]]')
		select('Table', 'cell:Data,0(RH)')
		assert_p('Table', 'Text', 'cell:Data,0(RH)')
		click('Right')
		select('Table', 'cell:Data,0(RD)')
		assert_p('Table', 'Text', 'Receipt DC Record (RD)', 'Data,0')
		select('Table', 'cell:Text,0(RD)')
		assert_p('Table', 'Text', 'RD', 'Text,0')
		select('Table', 'cell:Text,1(TAR)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, RD, RD], [Brand Id Rs Rd, 3, 3, TAR, TAR], [Order No Rd, 6, 12, 211853, 211853], [Receipt Locn Rd, 18, 4, 9601, 9601], [Prod No Rd, 31, 14, 2201324, 00000002201324], [Keycode Rd, 45, 8, 0, 00000000], [Seq No Rd, 53, 5, 1, 00001], [Prod Qualifier Rd, 58, 2, EN, EN], [Rcvd Qty Rd, 60, 9, 28, 000000028], [Itms Per Ctn Qtyrd, 69, 6, 1, 000001], [Unit Cost Rd, 75, 14, 49.200, 00000000049200], [C Usr Updt Rd, 89, 8, EQBD180, EQBD180], [Ts Updt Rd, 97, 26, 2005-03-04-20.30.05.644995, 2005-03-04-20.30.05.644995], [Rd Num Rs, 123, 9, 14, 000000014], [Rd Filler, 132, 219,              000131760                                                                                                                                                                                                     ,              000131760                                                                                                                                                                                                     ]]')
		select('Table', 'cell:Data,0(RD)')
		assert_p('Table', 'Text', 'cell:Data,0(RD)')
		click('Right')
		select('Table', 'cell:Data,0(RS)')
		assert_p('Table', 'Text', 'Receipt Store (RS)', 'Data,0')
		select('Table', 'cell:Text,0(RS)')
		assert_p('Table', 'Text', 'RS', 'Text,0')
		select('Table', 'cell:Text,1(TAR)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, RS, RS], [Brand Id Rs, 3, 3, TAR, TAR], [Order No, 6, 12, 297853, 297853], [Receipt Location, 18, 4, 9111, 9111], [Prod No, 31, 14, 2201324, 00000002201324], [Keycode, 45, 8, 0, 00000000], [Sequence No, 53, 5, 1, 00001], [Store No, 58, 4, 5036, 5036], [Receive Alc Qty, 62, 9, 1, 000000001], [Outstanding Ord Qty, 71, 9, 1, 000000001], [C Usr Updt, 80, 8, EQBD180, EQBD180], [Ts Updt, 88, 26, 2005-03-04-20.30.05.580496, 2005-03-04-20.30.05.580496], [Act Recv Qty, 114, 9, 1, 000000001], [Filler, 123, 228, , ]]')
		select('Table', 'cell:Data,0(RS)')
		assert_p('Table', 'Text', 'cell:Data,0(RS)')
		click('RightM')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
