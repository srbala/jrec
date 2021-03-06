useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser',  commonBits.sampleDir() + 'DTAR020.bin')
		click('Choose File')

		if window('Open'):
			click('Open')
		close()
		commonBits.setRecordLayout(select, 'DTAR020')

		click('Edit1')
		click('Filter1')
		select('Table1', 'STORE-NO', 'Field,0')
		select('Table1', '20', 'Value,0')
		select('Table1', 'cell:Field,1(null)')
		click('Filter1')
		rightclick('Table', '9 - 2|STORE-NO,4')
		select('Table', 'cell:1 - 8|KEYCODE-NO,4(69694158)')
		assert_p('Table', 'Content', '[[69684558, 20, 40118, 280, 1, 19.00], [69684558, 20, 40118, 280, -1, -19.00], [69684558, 20, 40118, 280, 1, 5.01], [69694158, 20, 40118, 280, 1, 19.00], [69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [63604808, 20, 40118, 170, 1, 4.87], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [64634429, 20, 40118, 957, 1, 3.99], [66624458, 20, 40118, 957, 1, 0.89], [63674861, 20, 40118, 957, 10, 2.70], [65674532, 20, 40118, 929, 1, 3.59]]')
		select('Table', 'cell:1 - 8|KEYCODE-NO,4(69694158)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:9 - 2|STORE-NO,0(20)')
		select('Table', '201', '9 - 2|STORE-NO,0')
		select('Table', '201', '9 - 2|STORE-NO,1')
		select('Table', 'cell:9 - 2|STORE-NO,1(20)')
		click('Save1')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Edit1')
		select('Table', 'cell:9 - 2|STORE-NO,0(201)')
		assert_p('Table', 'Text', '201', '9 - 2|STORE-NO,0')
		select('Table', 'cell:9 - 2|STORE-NO,1(201)')
		assert_p('Table', 'Text', '201', '9 - 2|STORE-NO,1')
		select('Table', 'cell:9 - 2|STORE-NO,2(20)')
		assert_p('Table', 'Text', '20', '9 - 2|STORE-NO,2')
		select('Table', '20', '9 - 2|STORE-NO,1')
		select('Table', '20', '9 - 2|STORE-NO,0')
		select('Table', '20', '9 - 2|STORE-NO,1')
##		select('Table', 'cell:9 - 2|STORE-NO,0(201)')
		click('Save1')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Edit1')
		select('Table', 'cell:9 - 2|STORE-NO,0(20)')
		assert_p('Table', 'Text', 'cell:9 - 2|STORE-NO,0(20)')
		select('Table', 'cell:9 - 2|STORE-NO,1(20)')
		assert_p('Table', 'Text', 'cell:9 - 2|STORE-NO,1(20)')
		select('Table', 'cell:9 - 2|STORE-NO,2(20)')
		assert_p('Table', 'Text', '20', '9 - 2|STORE-NO,2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
