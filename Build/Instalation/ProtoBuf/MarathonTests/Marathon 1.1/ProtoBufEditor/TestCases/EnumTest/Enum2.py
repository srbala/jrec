useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() +  'protoStoreSales6.bin')
		click('Edit1')
		##select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, SALE, CHEQUE], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'OTHER', 'saleType,8')
		##select('JTreeTable', '')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, OTHER, CHEQUE], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		##select('JTreeTable', '')
		rightclick('JTreeTable', 'quantity,8')
		select_menu('Edit Record')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 19000, 19000], [saleType, 5, , OTHER, OTHER], [paymentType, 6, , CHEQUE, CHEQUE]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales6.bin>>Tree View')
		select('JTreeTable', 'SALE', 'saleType,8')
		select('JTreeTable', 'cell:quantity,8(1)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, SALE, CHEQUE], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() +  'protoStoreSales6.bin'):
			click('No')
		close()
	close()
