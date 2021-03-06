useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'csv2DTAR020_tst1.bin.csv')
		click(commonBits.fl('Edit') + '1')
		click('Find1')
		select('Find.Search For_Txt', '19')
##		click('ScrollPane$ScrollBar', 12, 37)
		select('Find.Operator_Txt', commonBits.fl('= (Numeric)'))
		commonBits.find(click)
		assert_p('TextField', 'Text',  commonBits.fl('Found (line, field Num, field position)=') + '2, 5, 0')
		commonBits.find(click)

		if window(''):
			click('No')
		close()


		assert_p('TextField', 'Text',  commonBits.fl('Found (line, field Num, field position)=') + '18, 6, 0')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('LineList.FileDisplay_JTbl', 'cell:3|DATE,0(40118)')
		rightclick('LineList.FileDisplay_JTbl', '3|DATE,0')
		select_menu(commonBits.fl('Edit Record'))
		select('LineList.FileDisplay_JTbl', 'cell:3|DATE,0(40118)')
		click('Find1')
		select('Find.Search For_Txt', '3.99')
##		click('ScrollPane$ScrollBar', 9, 42)
##		select('Find.Operator_Txt', ' = (Numeric)')
		select('Find.Operator_Txt', commonBits.fl('= (Numeric)')
)
		commonBits.find(click)
		assert_p('TextField', 'Text',  commonBits.fl('Found (line, field Num, field position)=') + '11, 5, 0')
		commonBits.find(click)
		assert_p('TextField', 'Text',  commonBits.fl('Found (line, field Num, field position)=') + '12, 5, 0')
		commonBits.find(click)

		if window(''):
			click('No')
		close()

		assert_p('TextField', 'Text',  commonBits.fl('Found (line, field Num, field position)=') + '18, 6, 0')
	close()
