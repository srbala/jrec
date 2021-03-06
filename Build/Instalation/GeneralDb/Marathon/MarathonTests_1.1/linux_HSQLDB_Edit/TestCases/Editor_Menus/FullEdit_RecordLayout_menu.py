useFixture(default)

def test():
	from Modules import commonBits

	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select_menu('Record Layouts>>Edit Layout')
		select('Table', 'cell:Record Name,0(ams PO Download)')
		select('TextField', 'ams PO D%')
		select('TextField1', '%')

		#select('TabbedPane', 'Extras')
		#select('TabbedPane', 'Child Records')
		select('Table', 'cell:Record Name,0(ams PO Download)')
		select('ChildRecordsJTbl', 'cell:Child Name,1(0)')
		assert_p('ChildRecordsJTbl', 'Text', '', 'Child Name,1')
		select('ChildRecordsJTbl', 'cell:Child Name,2(0)')
		if commonBits.isVersion82():
##			assert_p('ChildRecordsJTbl', 'Content', '[[, ams PO Download: Detail, 0, Record Type, D1, , ], [, ams PO Download: Header, 0, Record Type, H1, , ], [, ams PO Download: Allocation, 0, Record Type, S1, , ]]')
			assert_p('ChildRecordsJTbl', 'Content', '[[, ams PO Download: Detail, , Record Type, D1, , ], [, ams PO Download: Header, , Record Type, H1, , ], [, ams PO Download: Allocation, , Record Type, S1, , ]]')
			assert_p('ChildRecordsJTbl', 'Content', '[[, ams PO Download: Detail, , Record Type, D1, , ], [, ams PO Download: Header, , Record Type, H1, , ], [, ams PO Download: Allocation, , Record Type, S1, , ]]')
		elif commonBits.isVersion80():
			assert_p('ChildRecordsJTbl', 'Content', '[[, 353, 0, Record Type, D1, , -1], [, 356, 0, Record Type, H1, , -1], [, 357, 0, Record Type, S1, , -1]]')
			assert_p('ChildRecordsJTbl', 'Content', '[[, 353, 0, Record Type, D1, , -1], [, 356, 0, Record Type, H1, , -1], [, 357, 0, Record Type, S1, , -1]]')
		else:
			assert_p('ChildRecordsJTbl', 'Content', '[[, 353, 0, Record Type, D1, -1], [, 356, 0, Record Type, H1, -1], [, 357, 0, Record Type, S1, -1]]')
		select('ChildRecordsJTbl', 'cell:Child Name,0(0)')
		assert_p('ChildRecordsJTbl', 'Text', 'cell:Child Name,0()')
		select('TextField', 'ams PO Download: Detail%')
		select('TextField1', '%')

		#select('TabbedPane', 'Extras')
		#select('TabbedPane', 'Fields')
		#select('Table', '')
		select('RecordFieldsJTbl', 'cell:Description,2()')
		assert_p('RecordFieldsJTbl', 'Text', '', 'Description,2')
		select('RecordFieldsJTbl', 'cell:Description,3()')
		if commonBits.version() == 'MsAccess':
			assert_p('RecordFieldsJTbl', 'Content', '[[1, 2, Record Type, , 0, 0, 15, Ams PO Download, , ], [3, 9, Pack Qty, , 8, 4, 0, , , ], [12, 13, Pack Cost, , 8, 4, 0, , , ], [25, 13, APN, , 7, 0, 0, , , ], [38, 1, Filler, , 0, 0, 0, , , ], [39, 8, Product, , 7, 0, 0, , , ], [72, 15, pmg dtl tech key, , 0, 0, 0, , , ], [87, 15, Case Pack id, , 0, 0, 0, , , ], [101, 50, Product Name, , 0, 0, 0, , , ]]')
		else:
			assert_p('RecordFieldsJTbl', 'Content', '[[1, 2, Record Type, , 0, 0, 0, , , ], [3, 9, Pack Qty, , 8, 4, 0, , , ], [12, 13, Pack Cost, , 8, 4, 0, , , ], [25, 13, APN, , 7, 0, 0, , , ], [38, 1, Filler, , 0, 0, 0, , , ], [39, 8, Product, , 7, 0, 0, , , ], [72, 15, pmg dtl tech key, , 0, 0, 0, , , ], [87, 15, Case Pack id, , 0, 0, 0, , , ], [101, 50, Product Name, , 0, 0, 0, , , ]]')
		#select('TabbedPane', 'Extras')
		#select('TabbedPane', 'Fields')
		#select('Table', '')
		select('TextField', 'ams PO Download: Header%')
		select('TextField1', '%')
		select('RecordFieldsJTbl', 'cell:Description,4(Format YYMMDD)')
		assert_p('RecordFieldsJTbl', 'Text', 'Format YYMMDD', 'Description,4')
		select('RecordFieldsJTbl', 'cell:Description,9(Format YYMMDD)')
		if commonBits.version() == 'MsAccess':
			assert_p('RecordFieldsJTbl', 'Content', '[[1, 2, Record Type, , 0, 0, 15, Ams PO Download, , ], [3, 5, Sequence Number, , 8, 3, 0, , , ], [8, 10, Vendor, , 7, 0, 0, , , ], [18, 12, PO, , 8, 0, 0, , , ], [30, 6, Entry Date, Format YYMMDD, 0, 0, 0, , , ], [36, 8, Filler, , 0, 0, 0, , , ], [44, 2, beg01 code, , 0, 0, 0, , , ], [46, 2, beg02 code, , 0, 0, 0, , , ], [48, 4, Department, , 0, 0, 0, , , ], [52, 6, Expected Reciept Date, Format YYMMDD, 0, 0, 0, , , ], [58, 6, Cancel by date, Format YYMMDD, 0, 0, 0, , , ], [68, 1, EDI Type, , 0, 0, 0, , , ], [69, 6, Add Date, Format YYMMDD, 0, 0, 0, , , ], [75, 1, Filler, , 0, 0, 0, , , ], [76, 10, Department Name, , 0, 0, 0, , , ], [86, 1, Prcoess Type, C/N Conveyable/Non-Conveyable, 0, 0, 0, , , ], [87, 2, Order Type, , 0, 0, 0, , , ]]')
		else:
			assert_p('RecordFieldsJTbl', 'Content', '[[1, 2, Record Type, , 0, 0, 0, , , ], [3, 5, Sequence Number, , 8, 3, 0, , , ], [8, 10, Vendor, , 7, 0, 0, , , ], [18, 12, PO, , 8, 0, 0, , , ], [30, 6, Entry Date, Format YYMMDD, 0, 0, 0, , , ], [36, 8, Filler, , 0, 0, 0, , , ], [44, 2, beg01 code, , 0, 0, 0, , , ], [46, 2, beg02 code, , 0, 0, 0, , , ], [48, 4, Department, , 0, 0, 0, , , ], [52, 6, Expected Reciept Date, Format YYMMDD, 0, 0, 0, , , ], [58, 6, Cancel by date, Format YYMMDD, 0, 0, 0, , , ], [68, 1, EDI Type, , 0, 0, 0, , , ], [69, 6, Add Date, Format YYMMDD, 0, 0, 0, , , ], [75, 1, Filler, , 0, 0, 0, , , ], [76, 10, Department Name, , 0, 0, 0, , , ], [86, 1, Prcoess Type, C/N Conveyable/Non-Conveyable, 0, 0, 0, , , ], [87, 2, Order Type, , 0, 0, 0, , , ]]')
		select('RecordFieldsJTbl', 'cell:Description,9(Format YYMMDD)')
		click('ScrollPane$ScrollBar3', 570, 10)
		click('ScrollPane$ScrollBar3', 523, 10)
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Record Layouts>>Create Layout')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Record Layouts>>Layout Wizard')
		commonBits.doSleep()
		##commonBits.doSleep()
		##assert_p('Label9', 'Text', 'Data Base')
		##assert_p('Label9', 'Text', 'System')
		assert_p('BmKeyedComboBox', 'Text', 'Default')
		assert_p('Label3', 'Text', 'Record Type')
		assert_p('Label4', 'Text', 'Font Name')
	

		
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Record Layouts>>Load Cobol Copybook')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Record Layouts>>Edit System Table')
		select('TableListJTbl', 'cell:Details,1(EDI)')
		assert_p('TableListJTbl', 'Text', 'EDI', 'Details,1')
		select('TableListJTbl', 'cell:Details,5(Mainframe)')
		assert_p('TableListJTbl', 'Text', 'Mainframe', 'Details,5')
		select('TableListJTbl', 'cell:Details,5(Mainframe)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
