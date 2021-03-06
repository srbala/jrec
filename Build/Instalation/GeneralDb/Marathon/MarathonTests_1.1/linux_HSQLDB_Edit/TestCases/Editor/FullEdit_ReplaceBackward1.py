useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_LocDownload_20041228.txt')
		commonBits.setRecordLayout(select, 'ams Store')

		click(commonBits.fl('Edit') + '1')
		select('Table', 'cell:4 - 4|Loc Nbr,0(5839)')
		rightclick('Table', '4 - 4|Loc Nbr,1')
		select_menu( commonBits.fl('Edit Record'))
		click('Find1')
		#click('MetalInternalFrameTitlePane', 211, 12)
		select('TextField', 'West')
##		click('Find1')
##		click('Find1')
##		click('Find1')
##		click('Find1')
##		click('Find1')
##		click('Find1')
##		click('Find1')

		commonBits.find(click)
		commonBits.find(click)
		commonBits.find(click)
		commonBits.find(click)
		commonBits.find(click)
		commonBits.find(click)
		commonBits.find(click)
		##commonBits.find(click)


		select('ComboBox2', commonBits.fl('Backward'))
		assert_p('ComboBox2', 'Text', commonBits.fl('Backward'))
		select('TextField1', 'West_')
		select('ComboBox', commonBits.fl('All Fields'))



		click(commonBits.fl('Replace'))


		select('Table', 'cell:' + commonBits.fl('Data') + ',6(Newcastle)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',6(Newcastle)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5016, 5016], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Glendale, Glendale], [Loc Addr Ln1, 45, 40, Glendale Power Centre, Glendale Power Centre], [Loc Addr Ln2, 85, 40, Cnr. West_ Wallsend & Lake Roads, Cnr. West_ Wallsend & Lake Roads], [Loc Addr Ln3, 125, 35, Newcastle, Newcastle], [Loc Postcode, 160, 10, 2300, 2300], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(Cnr. West_ Wallsend & Lake Roads)')
		assert_p('Table', 'Text', 'Cnr. West_ Wallsend & Lake Roads', commonBits.fl('Data') + ',5')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(Cnr. West_ Wallsend & Lake Roads)')

		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Find'))
		#click('Find1')
		select('TextField1', 'West_')
		select('ComboBox2', commonBits.fl('Backward'))
		select('ComboBox', commonBits.fl('All Fields'))



		click(commonBits.fl('Replace'))


		select('Table', 'cell:' + commonBits.fl('Data') + ',4(West_ Point Shopping Ctr)')
		assert_p('Table', 'Text', 'cell:' + commonBits.fl('Data') + ',4(West_ Point Shopping Ctr)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',4(West_ Point Shopping Ctr)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Blacktown - Not Yet Open)')
##		click('Find1')
		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Find'))
		select('TextField1', 'West_')
		select('ComboBox2', commonBits.fl('Backward'))
		select('ComboBox', commonBits.fl('All Fields'))



		click(commonBits.fl('Replace'))


		select('Table', 'cell:' + commonBits.fl('Data') + ',4(West_field Shopping Centre)')
		assert_p('Table', 'Text', 'West_field Shopping Centre', commonBits.fl('Data') + ',4')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(George Street)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Hornsby)')
		click('Find1')
		select('TextField1', 'West_')
		select('ComboBox2', commonBits.fl('Backward'))
		select('ComboBox', commonBits.fl('All Fields'))


		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Find'))

#		click('Find1')
		click(commonBits.fl('Replace Find'))

		click(commonBits.fl('Replace Find'))

		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Miranda)')
		select('ComboBox2', commonBits.fl('Forward'))




		assert_p('ComboBox2', 'Text', commonBits.fl('Forward'))



		commonBits.find(click)

##		click('Find1')
		select('Table', 'cell:' + commonBits.fl('Data') + ',4(West_field Phoenix Plaza)')
		assert_p('Table', 'Text', 'West_field Phoenix Plaza', commonBits.fl('Data') + ',4')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(Northumberland Street)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, West_field Phoenix Plaza, West_field Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(Northumberland Street)')
		click('Find1')
		select('ComboBox2', commonBits.fl('Forward'))




		select('TextField1', 'West_')
		select('ComboBox', commonBits.fl('All Fields'))


		commonBits.find(click)

##		click('Find1')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(152 Bunnerong Road)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, West_field Shoppingtown Eastgardens, West_field Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',4(West_field Shoppingtown Eastgardens)')
		assert_p('Table', 'Text', 'cell:' + commonBits.fl('Data') + ',4(West_field Shoppingtown Eastgardens)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',4(West_field Shoppingtown Eastgardens)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		#click('BasicInternalFrameTitlePane$NoFocusButton2')
		#click('MetalInternalFrameTitlePane', 637, 7)
		#select('Table', 'cell:4 - 4|Loc Nbr,0(5839)')
		#rightclick('Table', '10 - 35|Loc Name,2')
		#select_menu( commonBits.fl('Edit Record'))
		#click('BasicInternalFrameTitlePane$NoFocusButton2')
		#click('MetalInternalFrameTitlePane', 598, 8)
		#click('BasicInternalFrameTitlePane$NoFocusButton2')

		#if window('Save Changes to file: ' + commonBits.sampleDir() + 'Ams_LocDownload_20041228.txt'):
		#	click('No')
		#close()
	close()
