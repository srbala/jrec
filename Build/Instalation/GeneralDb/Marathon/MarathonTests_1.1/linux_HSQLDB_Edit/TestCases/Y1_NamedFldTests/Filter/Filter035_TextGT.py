useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'csv2DTAR020_tst1.bin.csv')
		click(commonBits.fl('Edit') + '1')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Update Csv Columns'))
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',5')
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',1')
		select('FieldChange_JTbl', 'cell:' + commonBits.fl('Type') + ',1(Number)')
		click(commonBits.fl('Apply'))
		click('Filter1')
		select('Fields.FieldRelationship_JTbl', 'cell:' + commonBits.fl('Field') + ',0(null)')
		select('Fields.FieldRelationship_JTbl', 'SALE-PRICE', commonBits.fl('Field') + ',0')
		select('Fields.FieldRelationship_JTbl', commonBits.fl('> (Text)'), commonBits.fl('Operator') + ',0')
		select('Fields.FieldRelationship_JTbl', '3.99', commonBits.fl('Value') + ',0')
		select('Fields.FieldRelationship_JTbl', 'cell:' + commonBits.fl('Value') + ',1()')
		commonBits.filter(click)
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4.87], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99], [68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95], [68654655, 166, 40118, 60, 1, 5.08], [68674560, 166, 40118, 170, 1, 5.99]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Fields.FieldRelationship_JTbl', 'cell:' + commonBits.fl('Field') + ',1(null)')
		select('Fields.FieldRelationship_JTbl', 'STORE-NO', commonBits.fl('Field') + ',1')
		select('Fields.FieldRelationship_JTbl', '59', commonBits.fl('Value') + ',1')
		select('Fields.FieldRelationship_JTbl', 'cell:' + commonBits.fl('Value') + ',2()')
		commonBits.filter(click)
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Fields.FieldRelationship_JTbl', '20', commonBits.fl('Value') + ',1')
		select('Fields.FieldRelationship_JTbl', 'cell:' + commonBits.fl('Value') + ',2()')
		commonBits.filter(click)
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[63604808, 20, 40118, 170, 1, 4.87], [69694158, 20, 40118, 280, 1, 5.01], [62684671, 20, 40118, 685, 1, 69.99]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Fields.FieldRelationship_JTbl', '166', commonBits.fl('Value') + ',1')
		select('Fields.FieldRelationship_JTbl', 'cell:' + commonBits.fl('Value') + ',2()')
		commonBits.filter(click)
		assert_p('LineList.FileDisplay_JTbl', 'Content', '[[68654655, 166, 40118, 60, 1, 5.08], [68674560, 166, 40118, 170, 1, 5.99]]')
	close()
