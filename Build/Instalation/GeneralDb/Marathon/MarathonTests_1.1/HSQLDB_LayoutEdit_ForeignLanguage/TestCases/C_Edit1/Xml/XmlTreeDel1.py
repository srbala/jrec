useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Xml' + commonBits.fileSep() + 'AmsLocationTest1.xml')
		commonBits.doEdit(click)

		select('JTreeTable', 'cell:Xml~Text,1(******************************)')
		click('Delete1')
		select('JTreeTable', 'cell:Xml~Text,1(* Location Download)')

		assert_p('JTreeTable', 'Content', '[[, , , , ], [, , * Location Download, , ], [, , ******************************, , ], [, , , , ]]')

		select('JTreeTable', 'cell:Xml~Text,3(null)')
		rightclick('JTreeTable', 'Xml~Text,3')
		select_menu(commonBits.fl('Expand Tree'))
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',5(null)')
		rightclick('JTreeTable', commonBits.fl('Tree') + ',5')
		select_menu(commonBits.fl('Copy Record#{s#}'))
		select('JTreeTable', 'cell:' + commonBits.fl('Tree') + ',1(null)')
		rightclick('JTreeTable', commonBits.fl('Tree') + ',1')
		select_menu(commonBits.fl('Paste Record#{s#}'))
		select('JTreeTable', 'cell:Xml~Text,2(null)')
		rightclick('JTreeTable', 'Xml~Text,2')
		select_menu(commonBits.fl('Expand Tree'))
		select('LayoutCombo', 'item')
		select('JTreeTable', 'cell:name,3(Location-Number)')
		assert_p('JTreeTable', 'Text', 'Location-Number', 'name,3')
		select('JTreeTable', 'cell:name,4(Location-Type)')

		assert_p('JTreeTable', 'Content', '[[, , , , AMSLOCATIONTEST1.cbl, , , , , , , , ], [, , * Location Download, , , , , , , , , , ], [, , , , 41, 03, Location-Details, 4, 41, , , , ], [, , , , 4, 05, Location-Number, 4, 4, 9(4), true, True, ], [, , , , 2, 05, Location-Type, 8, 2, XX, , True, ], [, , , , 35, 05, Location-Name, 10, 35, X(35), , True, ], [, , ******************************, , , , , , , , , , ], [, , , , 173, 01, Ams-Vendor, 1, 173, , , , ]]')

		select('JTreeTable', 'cell:name,3(Location-Number)')
		assert_p('JTreeTable', 'RowCount', '8')
		select('JTreeTable', 'rows:[3,4],columns:[' + commonBits.fl('Tree') + ']')
		click('Delete1')
		select('JTreeTable', 'cell:name,2(Location-Details)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window(commonBits.fl('Save Changes to file: ' + commonBits.sampleDir() + 'Xml' + commonBits.fileSep() + 'AmsLocationTest1.xml')):
			click('No')
		close()
	close()
