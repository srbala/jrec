useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_10'

	if window('Record Layout Definitions'):
		click('*7')
		select('FileChooser', commonBits.xmlCopybookDir() + 'yyAms PO Download.Xml')
		#select('BmKeyedComboBox1', '9')
		select('BmKeyedComboBox1', 'Other')

		click(commonBits.fl('Go'))

		assert_p('TextArea', 'Text', commonBits.checkCopybookLoad(commonBits.xmlCopybookDir() + 'yyAms PO Download.Xml', 'yyAms PO Download'))

		
##		assert_p('TextArea', 'Text', '''
##
##-->> ''' + commonBits.xmlCopybookDir() + '''yyAms PO Download.Xml processed
##
##      Copybook: yyAms PO Download''')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('*')
		select('TextField', 'yy%')
		select('TextField1', '%')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Child Records')
		assert_p('TextField2', 'Text', 'yyAms PO Download')
		assert_p('BmKeyedComboBox2', 'Text', commonBits.fl('Group of Records'))
		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',0(416)')
		assert_p('ChildRecordsJTbl', 'Text', 'yyAms PO Download: Detail', '' + commonBits.fl('Child Record') + ',0')
#		select('ChildRecordsJTbl', '416', commonBits.fl('Child Record') + ',0')
#		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',1(417)')
#		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',1(417)')
		assert_p('ChildRecordsJTbl', 'Text', 'yyAms PO Download: Header', '' + commonBits.fl('Child Record') + ',1')
#		select('ChildRecordsJTbl', '417', commonBits.fl('Child Record') + ',1')
#		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',2(418)')
#		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',2(418)')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Child Records')
		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',0(416)')
		keystroke('ChildRecordsJTbl', 'Ctrl+C', '' + commonBits.fl('Child Record') + ',0')
		select('ChildRecordsJTbl', 'cell:' + commonBits.fl('Child Record') + ',0(416)')
		select('TextField', 'yyAms PO Download: D%')
		select('TextField1', '%')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Fields')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Fields')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',0(Record Type)')
		assert_p('RecordFieldsJTbl', 'Text', 'Record Type', '' + commonBits.fl('FieldName') + ',0')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',1(Pack Qty)')
		assert_p('RecordFieldsJTbl', 'Text', '', commonBits.fl('Description') + ',0')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',2(Pack Cost)')
		assert_p('RecordFieldsJTbl', 'Text', 'Pack Cost', '' + commonBits.fl('FieldName') + ',2')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',1(8)')
##		assert_p('RecordFieldsJTbl', 'Text', '8', '' + commonBits.fl('FieldType') + ',1')
##		assert_p('RecordFieldsJTbl', 'Text', commonBits.fl('Num Assumed Decimal (Zero padded)'), '' + commonBits.fl('FieldType') + ',1')

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',1(7)')
		assert_p('TextField8', 'Text', commonBits.fl('Num Assumed Decimal (Zero padded)'))




		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',0(0)')
##		assert_p('RecordFieldsJTbl', 'Text', '0', '' + commonBits.fl('FieldType') + ',4')
##		assert_p('RecordFieldsJTbl', 'Text', commonBits.fl('Char'), '' + commonBits.fl('FieldType') + ',4')

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',4(7)')
		assert_p('TextField8', 'Text', commonBits.fl('Char'))

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',3(7)')
##		assert_p('RecordFieldsJTbl', 'Text', '0', '' + commonBits.fl('FieldType') + ',4')
##		assert_p('RecordFieldsJTbl', 'Text', commonBits.fl('Char'), '' + commonBits.fl('FieldType') + ',4')

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',4(7)')
		assert_p('TextField8', 'Text', commonBits.fl('Char'))


		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',8(Product Name)')
		assert_p('RecordFieldsJTbl', 'Text', 'Product Name', '' + commonBits.fl('FieldName') + ',8')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',8(Product Name)')
##		assert_p('BmKeyedComboBox3', 'Text', '0')
		assert_p('BmKeyedComboBox3', 'Text', 'Unkown')
		assert_p('BmKeyedComboBox2', 'Text', commonBits.fl('Record Layout')
)
		select('TextField', 'yyAms PO Download: H%')
		select('TextField1', '%')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Fields')
		assert_p('TextField2', 'Text', 'yyAms PO Download: Header')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',0(Record Type)')
		assert_p('RecordFieldsJTbl', 'Text', 'Record Type', '' + commonBits.fl('FieldName') + ',0')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',2(Vendor)')
		assert_p('RecordFieldsJTbl', 'Text', 'Vendor', '' + commonBits.fl('FieldName') + ',2')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',3(PO)')
		assert_p('RecordFieldsJTbl', 'Text', 'Entry Date', '' + commonBits.fl('FieldName') + ',4')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',4(Entry Date)')
		assert_p('RecordFieldsJTbl', 'Text', 'Entry Date', '' + commonBits.fl('FieldName') + ',4')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',6(beg01 code)')
		assert_p('RecordFieldsJTbl', 'Text', 'beg01 code', '' + commonBits.fl('FieldName') + ',6')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',8(Department)')
		assert_p('RecordFieldsJTbl', 'Text', 'Department', '' + commonBits.fl('FieldName') + ',8')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',1(8)')
##		assert_p('RecordFieldsJTbl', 'Text', '8', '' + commonBits.fl('FieldType') + ',1')
##		assert_p('RecordFieldsJTbl', 'Text', commonBits.fl('Num Assumed Decimal (Zero padded)'), commonBits.fl('FieldType') + ',3')

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',3(7)')
		assert_p('TextField8', 'Text', commonBits.fl('Num Assumed Decimal (Zero padded)'))


		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',3(8)')
##		assert_p('RecordFieldsJTbl', 'Text', '8', '' + commonBits.fl('FieldType') + ',3')
##		assert_p('RecordFieldsJTbl', 'Text', commonBits.fl('Num Assumed Decimal (Zero padded)'), '' + commonBits.fl('FieldType') + ',3')

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',3(7)')
		assert_p('TextField8', 'Text', commonBits.fl('Num Assumed Decimal (Zero padded)'))


		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',3(8)')
		select('TextField', 'yyAms PO Download: A%')
		select('TextField1', '%')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Extras')
##		select('TabbedPane', 'Fields')
		assert_p('CheckBox', 'Text', 'false')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',1(DC Number 1)')
		assert_p('RecordFieldsJTbl', 'Text', 'DC Number 1', '' + commonBits.fl('FieldName') + ',1')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',2(Pack Quantity 1)')
		assert_p('RecordFieldsJTbl', 'Text', 'Pack Quantity 1', '' + commonBits.fl('FieldName') + ',2')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',3(DC Number 2)')
		assert_p('RecordFieldsJTbl', 'Text', 'DC Number 2', '' + commonBits.fl('FieldName') + ',3')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',4(Pack Quantity 2)')
		assert_p('RecordFieldsJTbl', 'RowCount', '19')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',2(7)')
		##assert_p('RecordFieldsJTbl', 'Text', '7', '' + commonBits.fl('FieldType') + ',4')

##		assert_p('RecordFieldsJTbl', 'Text', commonBits.fl('Num (Right Justified zero padded)'), '' + commonBits.fl('FieldType') + ',4')

		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldType') + ',4(7)')
		assert_p('TextField8', 'Text', commonBits.fl('Num (Right Justified zero padded)'))



# 		commonBits.delete3(click)
		select('TextField', 'yyAms PO Download')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Child Records')
		commonBits.delete3(click)

		if window(commonBits.fl('Delete: yyAms PO Download')):
			click('Yes')
		close()

#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
		select('TextField', 'yyAms PO Download%')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
		select('TextField', 'yyAms PO Download: A%')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
		commonBits.delete3(click)

		if window(commonBits.fl('Delete: yyAms PO Download: Allocation')):
			click('Yes')
		close()

#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
		select('TextField', 'yyAms PO Download: H%')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
		commonBits.delete3(click)

		if window(commonBits.fl('Delete: yyAms PO Download: Header')):
			click('Yes')
		close()

		select('TextField', 'yyAms PO Download: %')
		commonBits.delete3(click)

		if window(commonBits.fl('Delete: yyAms PO Download: Detail')):
			click('Yes')
		close()
		click(commonBits.fl('Close')
)


	close()
