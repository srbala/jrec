useFixture(default)
###
###  
###
def test():
	from Modules import commonBits
	import os
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'zcStore.bin')
		select('FileNameTxtFld1', commonBits.stdCopybookDir() + 'Sales.proto')
		select('ComboBox', 'Delimited Messages')
		select('ComboBox1', 'Proto Definition')


		click('Edit1')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,2(0)')
##		assert_p('Table', 'Content', '[[keycode, 1, , , ], [store, 2, , , ], [department, 3, , , ], [saleDate, 4, , , ], [quantity, 5, , , ], [price, 6, , , ]]')
##[[keycode, 1, , 0, 0], [store, 2, , 0, 0], [department, 3, , 0, 0], [saleDate, 4, , 0, 0], [quantity, 5, , 0, 0], [price, 6, , 0, 0]]')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 0, 0], [store, 2, , 0, 0], [department, 3, , 0, 0], [saleDate, 4, , 0, 0], [quantity, 5, , 0, 0], [price, 6, , 0, 0]]')
		select('BaseLineAsColumn$LineAsColTbl', '1111', 'Data,0')
		select('BaseLineAsColumn$LineAsColTbl', '222', 'Data,1')
		select('BaseLineAsColumn$LineAsColTbl', '3333', 'Data,2')
		select('BaseLineAsColumn$LineAsColTbl', '445566', 'Data,3')
		select('BaseLineAsColumn$LineAsColTbl', '1', 'Data,4')
		select('BaseLineAsColumn$LineAsColTbl', '11000', 'Data,5')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,4(1)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 1111, 1111], [store, 2, , 222, 222], [department, 3, , 3333, 3333], [saleDate, 4, , 445566, 445566], [quantity, 5, , 1, 1], [price, 6, , 11000, 11000]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		assert_p('LinesTbl', 'Content', '[[1111, 222, 3333, 445566, 1, 11000]]')
		click('New')
		select('BaseLineAsColumn$LineAsColTbl', '1212', 'Data,0')
		select('BaseLineAsColumn$LineAsColTbl', '12', 'Data,1')
		select('BaseLineAsColumn$LineAsColTbl', '12', 'Data,2')
		select('BaseLineAsColumn$LineAsColTbl', '121212', 'Data,3')
		select('BaseLineAsColumn$LineAsColTbl', '1', 'Data,4')
		select('BaseLineAsColumn$LineAsColTbl', '12000', 'Data,5')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,4(1)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 1212, 1212], [store, 2, , 12, 12], [department, 3, , 12, 12], [saleDate, 4, , 121212, 121212], [quantity, 5, , 1, 1], [price, 6, , 12000, 12000]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>zcStore.bin>>Table:')
		assert_p('LinesTbl', 'Content', '[[1111, 222, 3333, 445566, 1, 11000], [1212, 12, 12, 121212, 1, 12000]]')
		click('Save1')
		
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Edit1')
		assert_p('LinesTbl', 'Content', '[[1111, 222, 3333, 445566, 1, 11000], [1212, 12, 12, 121212, 1, 12000]]')
##		click('Delete2')

		select('LinesTbl', 'rows:[0,1],columns:[3|department,4|saleDate]')
		click('Delete2')
		click('Save1')

		click('BasicInternalFrameTitlePane$NoFocusButton2')

		os.remove(commonBits.sampleDir() + 'zcStore.bin')
	close()
