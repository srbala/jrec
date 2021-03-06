useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Layout Definitions'):
		click('*')
		commonBits.new1(click)

		select('RecordDef.Record Name_Txt', 'zx3xzFLD1')
		select('RecordDef.Description_Txt', 'fld tst 3')
		select('RecordDef.Lines to Insert_Txt', '3')
		click(commonBits.fl('Insert'))


		select('RecordDef.Lines to Insert_Txt', '')
		assert_p('RecordFieldsJTbl', 'Content', '[[0, 0, , , 0, 0, 0, , , ], [0, 0, , , 0, 0, 0, , , ], [0, 0, , , 0, 0, 0, , , ]]')
		select('RecordFieldsJTbl', '1', commonBits.fl('Position') + ',0')
		select('RecordFieldsJTbl', '1', commonBits.fl('Length') + ',0')
		select('RecordFieldsJTbl', 'fld 11', commonBits.fl('FieldName') + ',0')
		select('RecordFieldsJTbl', '2', commonBits.fl('Position') + ',1')
		select('RecordFieldsJTbl', '5', commonBits.fl('Length') + ',1')
		select('RecordFieldsJTbl', 'fld 12', commonBits.fl('FieldName') + ',1')
		select('RecordFieldsJTbl', '7', commonBits.fl('Position') + ',2')
		select('RecordFieldsJTbl', '9', commonBits.fl('Length') + ',2')
		select('RecordFieldsJTbl', 'fld 13', commonBits.fl('FieldName') + ',2')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',1()')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 11, , 0, 0, 0, , , ], [2, 5, fld 12, , 0, 0, 0, , , ], [7, 9, fld 13, , 0, 0, 0, , , ]]')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',1()')
		assert_p('RecordDef.Description_Txt', 'Text', 'fld tst 3')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',1()')
		assert_p('RecordDef.Record Name_Txt', 'Text', 'zx3xzFLD1')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',1()')
		click(commonBits.fl('Save As'))



		if window('Input'):
			assert_p('OptionPane.textField', 'Text', 'zx3xzFLD1')
			select('OptionPane.textField', 'zx3xzFLD2')
			click('OK')
		close()


		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 11, , 0, 0, 0, , , ], [2, 5, fld 12, , 0, 0, 0, , , ], [7, 9, fld 13, , 0, 0, 0, , , ]]')
		assert_p('RecordDef.Description_Txt', 'Text', 'fld tst 3')
		assert_p('RecordDef.Record Name_Txt', 'Text', 'zx3xzFLD2')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',2()')
		click(commonBits.fl('Insert'))


		select('RecordFieldsJTbl', '18', commonBits.fl('Position') + ',3')
		select('RecordFieldsJTbl', '10', commonBits.fl('Length') + ',3')
		select('RecordFieldsJTbl', 'fld 24', commonBits.fl('FieldName') + ',3')
		select('RecordFieldsJTbl', 'fld 23', commonBits.fl('FieldName') + ',2')
		select('RecordFieldsJTbl', 'fld 22', commonBits.fl('FieldName') + ',1')
		select('RecordFieldsJTbl', 'fld 21', commonBits.fl('FieldName') + ',0')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',1(fld 22)')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 21, , 0, 0, 0, , , ], [2, 5, fld 22, , 0, 0, 0, , , ], [7, 9, fld 23, , 0, 0, 0, , , ], [18, 10, fld 24, , 0, 0, 0, , , ]]')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('FieldName') + ',1(fld 22)')
		click(commonBits.fl('Save As'))



		if window('Input'):
			assert_p('OptionPane.textField', 'Text', 'zx3xzFLD2')
			select('OptionPane.textField', 'zx3xzFLD3')
			click('OK')
		close()

		##select('TabbedPane', 'Extras')
		##select('TabbedPane', 'Extras')
		##select('TabbedPane', 'Fields')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 21, , 0, 0, 0, , , ], [2, 5, fld 22, , 0, 0, 0, , , ], [7, 9, fld 23, , 0, 0, 0, , , ], [18, 10, fld 24, , 0, 0, 0, , , ]]')
		select('RecordFieldsJTbl', 'fld 34', commonBits.fl('FieldName') + ',3')
		select('RecordFieldsJTbl', 'fld 33', commonBits.fl('FieldName') + ',2')
		select('RecordFieldsJTbl', 'fld 32', commonBits.fl('FieldName') + ',1')
		select('RecordFieldsJTbl', 'fld 31', commonBits.fl('FieldName') + ',0')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',3()')
		click(commonBits.fl('Insert'))


		select('RecordFieldsJTbl', '28', commonBits.fl('Position') + ',4')
		select('RecordFieldsJTbl', '12', commonBits.fl('Length') + ',4')
		select('RecordFieldsJTbl', 'fld 35', commonBits.fl('FieldName') + ',4')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',3()')
		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 31, , 0, 0, 0, , , ], [2, 5, fld 32, , 0, 0, 0, , , ], [7, 9, fld 33, , 0, 0, 0, , , ], [18, 10, fld 34, , 0, 0, 0, , , ], [28, 12, fld 35, , 0, 0, 0, , , ]]')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',3()')
		assert_p('RecordDef.Record Name_Txt', 'Text', 'zx3xzFLD3')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',3()')
		assert_p('RecordDef.Description_Txt', 'Text', 'fld tst 3')
		select('RecordFieldsJTbl', 'cell:' + commonBits.fl('Description') + ',3()')
		select('RecordList.Record Name_Txt', 'zx3xzFLD1')

		select('RecordList.Description_Txt', '%')

		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 11, , 0, 0, 0, , , ], [2, 5, fld 12, , 0, 0, 0, , , ], [7, 9, fld 13, , 0, 0, 0, , , ]]')
		assert_p('RecordDef.Description_Txt', 'Text', 'fld tst 3')
		assert_p('RecordDef.Record Name_Txt', 'Text', 'zx3xzFLD1')
		select('RecordList.Record Name_Txt', 'zx3xzFLD2')

		select('RecordList.Description_Txt', '%%')

		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 21, , 0, 0, 0, , , ], [2, 5, fld 22, , 0, 0, 0, , , ], [7, 9, fld 23, , 0, 0, 0, , , ], [18, 10, fld 24, , 0, 0, 0, , , ]]')
		assert_p('RecordDef.Record Name_Txt', 'Text', 'zx3xzFLD2')
		assert_p('RecordDef.Description_Txt', 'Text', 'fld tst 3')
		select('RecordList.Record Name_Txt', 'zx3xzFLD3')

		select('RecordList.Description_Txt', '%')

		assert_p('RecordFieldsJTbl', 'Content', '[[1, 1, fld 31, , 0, 0, 0, , , ], [2, 5, fld 32, , 0, 0, 0, , , ], [7, 9, fld 33, , 0, 0, 0, , , ], [18, 10, fld 34, , 0, 0, 0, , , ], [28, 12, fld 35, , 0, 0, 0, , , ]]')
		assert_p('RecordDef.Record Name_Txt', 'Text', 'zx3xzFLD3')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
