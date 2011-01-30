useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_10'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20050101.txt')
		select('ComboBox2', 'ams PO Download')
		commonBits.doEdit(click)
		select_menu('View>>Record Based Tree')
##		select('Table', '1', 'Parent Record,0')
##		select('Table', '0', 'Parent Record,2')

		select('Table', 'ams PO Download: Header', 'Parent Record,0')
		select('Table', 'ams PO Download: Detail', 'Parent Record,2')


		select('Table', 'cell:Parent Record,2(0)')
		click('Build')
		select_menu('File>>Save Tree as XML')

		if window('Open'):
			select('File Name', 'xmlSaveAms_PODownload_20050101.xml')
			click('Open')
		close()

		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>Ams_PODownload_20050101.txt>>Table: ')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('File>>File Copy Menu')
		click('*1')
		select('FileChooser', commonBits.sampleDir() + 'xmlSaveAms_PODownload_20050101.xml')
		click('Right')
		select('TabbedPane', '')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PO_fromXmlSave.txt')


		commonBits.setRecordLayout2(select, 'ams PO Download')

		if commonBits.isJRecord():
			click('Right')
		click('Right')

		select('TabbedPane', '')
		select('Table', 'cell:Equivalent Record,2(-1)')
		select('Table', 'cell:Equivalent Record,2(1)')
		select('Table', 'ams PO Download: Header', 'Equivalent Record,2')
#		select('Table', 'cell:Equivalent Record,2(1)')
		select('Table1', 'cell:Field,4(Sequence_Number)')
		assert_p('Table1', 'Content', '[[Xml~Name, ], [Xml~Prefix, ], [Xml~Namespace, ], [Record_Type, Record Type], [Sequence_Number, Sequence Number], [Vendor, Vendor], [PO, PO], [Entry_Date, Entry Date], [beg01_code, beg01 code], [Department, Department], [Expected_Reciept_Date, Expected Reciept Date], [Cancel_by_date, Cancel by date], [Department_Name, Department Name], [Prcoess_Type, Prcoess Type], [Order_Type, Order Type], [Xml~End, ], [Following~Text, ]]')
		select('Table1', 'cell:Field,4(Sequence_Number)')
		select('Table', 'cell:Equivalent Record,3(0)')
		select('Table', 'ams PO Download: Detail', 'Equivalent Record,3')
#		select('Table', 'cell:Equivalent Record,3(0)')
		select('Table1', 'cell:Field,4(Pack_Qty)')
		assert_p('Table1', 'Content', '[[Xml~Name, ], [Xml~Prefix, ], [Xml~Namespace, ], [Record_Type, Record Type], [Pack_Qty, Pack Qty], [Pack_Cost, Pack Cost], [APN, APN], [Product, Product], [pmg_dtl_tech_key, pmg dtl tech key], [Case_Pack_id, Case Pack id], [Product_Name, Product Name], [Xml~End, ], [Following~Text, ]]')
		select('Table1', 'cell:Field,4(Pack_Qty)')
		select('Table', 'ams PO Download: Allocation', 'Equivalent Record,4')
		select('Table', 'cell:Equivalent Record,4(2)')
		select('Table1', 'cell:Field,4(DC_Number_1)')
		assert_p('Table1', 'Content', '[[Xml~Name, ], [Xml~Prefix, ], [Xml~Namespace, ], [Record_Type, Record Type], [DC_Number_1, DC Number 1], [Pack_Quantity_1, Pack Quantity 1], [DC_Number_2, DC Number 2], [Pack_Quantity_2, Pack Quantity 2], [DC_Number_4, DC Number 4], [Pack_Quantity_4, Pack Quantity 4], [DC_Number_5, DC Number 5], [Pack_Quantity_5, Pack Quantity 5], [DC_Number_6, DC Number 6], [Pack_Quantity_6, Pack Quantity 6], [DC_Number_7, DC Number 7], [Pack_Quantity_7, Pack Quantity 7], [DC_Number_8, DC Number 8], [Pack_Quantity_8, Pack Quantity 8], [DC_Number_9, DC Number 9], [Pack_Quantity_9, Pack Quantity 9], [DC_Number_10, DC Number 10], [Pack_Quantity_10, Pack Quantity 10], [Xml~End, ], [Following~Text, ]]')
##		select('Table1', '')
		select('Table', 'cell:Record,3(ams_PO_Download__Detail)')
		assert_p('Table', 'Content', '[[XML Start_Document,  ], [ams_PO_Download,  ], [ams_PO_Download__Header, ams PO Download: Header], [ams_PO_Download__Detail, ams PO Download: Detail], [ams_PO_Download__Allocation, ams PO Download: Allocation], [/ams_PO_Download__Detail,  ], [/ams_PO_Download__Header,  ], [/ams_PO_Download,  ]]')
		select('Table', 'cell:Record,3(ams_PO_Download__Detail)')
		click('ReFrame', 787, 576)
		click('Right')
		select('TabbedPane', '')
		click('Copy2')
		assert_p('TextField1', 'Text', 'Copy Done !!! ')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('File>>Compare Menu')
		click('*2')
		select('FileChooser', commonBits.sampleDir() + 'xmlSaveAms_PODownload_20050101.xml')
		click('Right')
		select('TabbedPane', '')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20050101.txt')
		click('Right')
		select('TabbedPane', '')
		select('Table', 'cell:Equivalent Record,2(-1)')
		select('Table', 'ams PO Download: Header', 'Equivalent Record,2')
#		select('Table', 'cell:Equivalent Record,2(1)')
		select('Table1', 'cell:Field,3(Record_Type)')
		assert_p('Table1', 'Content', '[[Xml~Name, ], [Xml~Prefix, ], [Xml~Namespace, ], [Record_Type, Record Type], [Sequence_Number, Sequence Number], [Vendor, Vendor], [PO, PO], [Entry_Date, Entry Date], [beg01_code, beg01 code], [Department, Department], [Expected_Reciept_Date, Expected Reciept Date], [Cancel_by_date, Cancel by date], [Department_Name, Department Name], [Prcoess_Type, Prcoess Type], [Order_Type, Order Type], [Xml~End, ], [Following~Text, ]]')
		select('Table1', 'cell:Field,3(Record_Type)')
		select('Table', 'ams PO Download: Detail', 'Equivalent Record,3')
		select('Table', 'cell:Equivalent Record,3(0)')
		select('Table1', 'cell:Field,4(Pack_Qty)')
		assert_p('Table1', 'Content', '[[Xml~Name, ], [Xml~Prefix, ], [Xml~Namespace, ], [Record_Type, Record Type], [Pack_Qty, Pack Qty], [Pack_Cost, Pack Cost], [APN, APN], [Product, Product], [pmg_dtl_tech_key, pmg dtl tech key], [Case_Pack_id, Case Pack id], [Product_Name, Product Name], [Xml~End, ], [Following~Text, ]]')
		select('Table1', 'cell:Field,4(Pack_Qty)')
		select('Table', 'cell:Equivalent Record,4(2)')
		select('Table', 'ams PO Download: Allocation', 'Equivalent Record,4')
##		select('Table', 'cell:Equivalent Record,4(2)')
		select('Table1', 'cell:Field,3(Record_Type)')
		assert_p('Table1', 'Content', '[[Xml~Name, ], [Xml~Prefix, ], [Xml~Namespace, ], [Record_Type, Record Type], [DC_Number_1, DC Number 1], [Pack_Quantity_1, Pack Quantity 1], [DC_Number_2, DC Number 2], [Pack_Quantity_2, Pack Quantity 2], [DC_Number_4, DC Number 4], [Pack_Quantity_4, Pack Quantity 4], [DC_Number_5, DC Number 5], [Pack_Quantity_5, Pack Quantity 5], [DC_Number_6, DC Number 6], [Pack_Quantity_6, Pack Quantity 6], [DC_Number_7, DC Number 7], [Pack_Quantity_7, Pack Quantity 7], [DC_Number_8, DC Number 8], [Pack_Quantity_8, Pack Quantity 8], [DC_Number_9, DC Number 9], [Pack_Quantity_9, Pack Quantity 9], [DC_Number_10, DC Number 10], [Pack_Quantity_10, Pack Quantity 10], [Xml~End, ], [Following~Text, ]]')
##		select('Table1', '')
		select('Table', 'cell:Record,2(ams_PO_Download__Header)')
##		assert_p('Table', 'Content', '[[XML Start_Document, -1], [ams_PO_Download, -1], [ams_PO_Download__Header, 1], [ams_PO_Download__Detail, 0], [ams_PO_Download__Allocation, 2], [/ams_PO_Download__Detail, -1], [/ams_PO_Download__Header, -1], [/ams_PO_Download, -1]]')
		assert_p('Table', 'Content', '[[XML Start_Document,  ], [ams_PO_Download,  ], [ams_PO_Download__Header, ams PO Download: Header], [ams_PO_Download__Detail, ams PO Download: Detail], [ams_PO_Download__Allocation, ams PO Download: Allocation], [/ams_PO_Download__Detail,  ], [/ams_PO_Download__Header,  ], [/ams_PO_Download,  ]]')

		select('Table', 'cell:Record,2(ams_PO_Download__Header)')
		click('ReFrame', 782, 600)
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>Two Layout Compare')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Open')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PO_fromXmlSave.txt')
		commonBits.doEdit(click)
		select('Table', 'cell:3 - 4|DC Number 1,3(5078)')
		select('Table', 'cell:3 - 4|DC Number 1,4(5303)')
		rightclick('Table', '3 - 4|DC Number 1,4')
		select_menu('Edit Record')
###		select('Table1', 'cell:3 - 4|DC Number 1,4(5303)')
		select('Table', 'cell:Data,7(5177)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, S1, S1], [DC Number 1, 3, 4, 5303, 5303], [Pack Quantity 1, 7, 8, 1, 00000001], [DC Number 2, 15, 4, 5169, 5169], [Pack Quantity 2, 19, 8, 1, 00000001], [DC Number 4, 39, 4, 5171, 5171], [Pack Quantity 4, 43, 8, 1, 00000001], [DC Number 5, 51, 4, 5177, 5177], [Pack Quantity 5, 55, 8, 1, 00000001], [DC Number 6, 63, 4, 5016, 5016], [Pack Quantity 6, 67, 8, 1, 00000001], [DC Number 7, 75, 4, 5089, 5089], [Pack Quantity 7, 79, 8, 2, 00000002], [DC Number 8, 87, 4, 5136, 5136], [Pack Quantity 8, 91, 8, 1, 00000001], [DC Number 9, 99, 4, 5011, 5011], [Pack Quantity 9, 103, 8, 1, 00000001], [DC Number 10, 111, 4, 5046, 5046], [Pack Quantity 10, 115, 8, 1, 00000001]]')
		select('Table', 'cell:Data,7(5177)')
		click('TextArea')
		assert_p('TextArea', 'Text', 'S1530300000001516900000001            517100000001517700000001501600000001508900000002513600000001501100000001504600000001')
		click('Right')
		click('TextArea')
		assert_p('TextArea', 'Text', 'S1514500000001509600000002            516200000001516300000001516400000001519200000001515000000001517500000001000000000000')
		click('Right')
		select('Table', 'cell:Data,4(040929)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, H1, H1], [Sequence Number, 3, 5, 45.358, 45358], [Vendor, 8, 10, 4338, 0000004338], [PO, 18, 12, 233872, 000000233872], [Entry Date, 30, 6, 040929, 040929], [Filler, 36, 8, , ], [beg01 code, 44, 2, 00, 00], [beg02 code, 46, 2, , ], [Department, 48, 4, 290, 290], [Expected Reciept Date, 52, 6, 050103, 050103], [Cancel by date, 58, 6, 050107, 050107], [EDI Type, 68, 1, , ], [Add Date, 69, 6, , ], [Filler, 75, 1, , ], [Department Name, 76, 10, OPTIONS PL, OPTIONS PL], [Prcoess Type, 86, 1, C, C], [Order Type, 87, 2, FT, FT]]')
		select('Table', 'cell:Data,4(040929)')
		click('TextArea')
		assert_p('TextArea', 'Text', 'H1453580000004338000000233872040929        00  290 050103050107            OPTIONS PLCFT')
		click('Right')
		select('Table', 'cell:Data,5(43372078)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, D1, D1], [Pack Qty, 3, 9, 14.0000, 000140000], [Pack Cost, 12, 13, 119.8400, 0000001198400], [APN, 25, 13, 0, 0000000000000], [Filler, 38, 1, , ], [Product, 39, 8, 43372078, 43372078], [pmg dtl tech key, 72, 15, 2117152, 2117152], [Case Pack id, 87, 15, 45872078, 45872078], [Product Name, 101, 50,  MTH5033H DUSTY PINK L/S FANCY CREW C\'MERE CARDIGA,  MTH5033H DUSTY PINK L/S FANCY CREW C\'MERE CARDIGA]]')
		select('Table', 'cell:Data,5(43372078)')
		click('TextArea')
		assert_p('TextArea', 'Text', 'D100014000000000011984000000000000000 43372078                         2117152        45872078       MTH5033H DUSTY PINK L/S FANCY CREW C\'MERE CARDIGA')
		click('Right')
		select('Table', 'cell:Data,5(5057)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, S1, S1], [DC Number 1, 3, 4, 5036, 5036], [Pack Quantity 1, 7, 8, 1, 00000001], [DC Number 2, 15, 4, 5043, 5043], [Pack Quantity 2, 19, 8, 1, 00000001], [DC Number 4, 39, 4, 5057, 5057], [Pack Quantity 4, 43, 8, 1, 00000001], [DC Number 5, 51, 4, 5065, 5065], [Pack Quantity 5, 55, 8, 1, 00000001], [DC Number 6, 63, 4, 5069, 5069], [Pack Quantity 6, 67, 8, 1, 00000001], [DC Number 7, 75, 4, 5076, 5076], [Pack Quantity 7, 79, 8, 1, 00000001], [DC Number 8, 87, 4, 5079, 5079], [Pack Quantity 8, 91, 8, 1, 00000001], [DC Number 9, 99, 4, 5094, 5094], [Pack Quantity 9, 103, 8, 1, 00000001], [DC Number 10, 111, 4, 5128, 5128], [Pack Quantity 10, 115, 8, 1, 00000001]]')
		select('Table', 'cell:Data,5(5057)')
		click('TextArea')
		click('TextArea')
		assert_p('TextArea', 'Text', 'S1503600000001504300000001            505700000001506500000001506900000001507600000001507900000001509400000001512800000001')
		click('Right')
		click('TextArea')
		assert_p('TextArea', 'Text', 'S1515100000001518000000001            517300000001000000000000000000000000000000000000000000000000000000000000000000000000')
		click('Right')
		click('TextArea')
		assert_p('TextArea', 'Text', 'H1453590000004468000000255906040929        00  290 050103050107            OPTIONS PLCFT')
		select('Table', 'cell:Data,9(050103)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, H1, H1], [Sequence Number, 3, 5, 45.359, 45359], [Vendor, 8, 10, 4468, 0000004468], [PO, 18, 12, 255906, 000000255906], [Entry Date, 30, 6, 040929, 040929], [Filler, 36, 8, , ], [beg01 code, 44, 2, 00, 00], [beg02 code, 46, 2, , ], [Department, 48, 4, 290, 290], [Expected Reciept Date, 52, 6, 050103, 050103], [Cancel by date, 58, 6, 050107, 050107], [EDI Type, 68, 1, , ], [Add Date, 69, 6, , ], [Filler, 75, 1, , ], [Department Name, 76, 10, OPTIONS PL, OPTIONS PL], [Prcoess Type, 86, 1, C, C], [Order Type, 87, 2, FT, FT]]')
		select('Table', 'cell:Data,9(050103)')
		click('Right')
		select('Table', 'cell:Data,7(45872078)')
		select('Table', 'cell:Data,2(101.2000)')
		assert_p('Table', 'Content', '[[Record Type, 1, 2, D1, D1], [Pack Qty, 3, 9, 29.0000, 000290000], [Pack Cost, 12, 13, 101.2000, 0000001012000], [APN, 25, 13, 0, 0000000000000], [Filler, 38, 1, , ], [Product, 39, 8, 45874751, 45874751], [pmg dtl tech key, 72, 15, 2117337, 2117337], [Case Pack id, 87, 15, 45872078, 45872078], [Product Name, 101, 50,  MTH5030H BLK L/S VLVT RIBBON SCOOP C\'MERE W/BROOC,  MTH5030H BLK L/S VLVT RIBBON SCOOP C\'MERE W/BROOC]]')
		select('Table', 'cell:Data,2(101.2000)')
		click('TextArea')
		assert_p('TextArea', 'Text', 'D100029000000000010120000000000000000 45874751                         2117337        45872078       MTH5030H BLK L/S VLVT RIBBON SCOOP C\'MERE W/BROOC')
		#click('MetalInternalFrameTitlePane', 503, 14)
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:3 - 4|DC Number 1,4(5303)')
		select('Table', 'cell:3 - 4|DC Number 1,4(5303)')
		select_menu('Window>>Ams_PO_fromXmlSave.txt>>Table: ')
		select('Table', 'cell:3 - 4|DC Number 1,4(5303)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
