useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'Ams_LocDownload_20041228_Extract2.bin')
		##commonBits.setRecordLayout(select, 'ams Store')
		click('Edit1')
		select_menu('Data>>Sort')
		#select('List', 'Locations')
		select('Table', 'Loc_Type', 'Field,0')
		select('Table', 'Loc_Nbr', 'Field,1')
		select('Table', 'cell:Field,1(Loc_Nbr)')
		click('Sort1')
		select('LinesTbl', 'cell:4|Loc_Name,6(Ringwood)')
		assert_p('LinesTbl', 'Content', '[[TAR, 5839, DC, DC - Taras Ave, , 30-68 Taras Ave, Altona North, 3025, VIC, A], [TAR, 5850, DC, VIC West Ad Support, , Lot 2 Little Boundary Rd, Laverton, 3028, VIC, A], [TAR, 5966, DC, Huntingwood DC, Huntingwood DC, 35 Huntingwood Drive, Huntingwood, 2148, NSW, A], [TAR, 5967, DC, Hendra DC, Hendra DC, Cnr Headly Ave & Nudgee Road, Hendra, 4011, QLD, A], [TAR, 5968, DC, Beverly DC, Beverly DC, 117 Main Street, Beverly, 5009, SA, A], [TAR, 5002, ST, Coffs Harbour, Coffs Harbour, Cnr. Park Beach Road & Pacific Hwy, Coffs Harbour, 2450, NSW, A], [TAR, 5012, ST, Ringwood, Ringwood, Seymour Street, Ringwood, 3134, VIC, A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5030, ST, Epping, Epping Plaza Shopping Centre, Cnr. High & Cooper Streets, Epping, 3076, VIC, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5054, ST, Highpoint City, Laverton, Lot 2, Cnr Lt Boundry & Old Geelong Road, Laverton, 3028, VIC, A], [TAR, 5062, ST, Castletown, Townsville, Cnr. Woolcock St. & Kings Road, Townsville, 4810, QLD, A], [TAR, 5096, ST, Canberra Civic, Target Canberra, Canberra City Centre, Akuna Ave, Canberra, 2601, ACT, A], [TAR, 5138, ST, Cairns Central, Cairns, Cnr. McLeod & Aplin Streets, Cairns, 4870, QLD, A], [TAR, 5141, ST, The Willows, Thuringowa Central, Cnr Thuringowa Drive &  Range Rd, Thuringowa Central, 4817, QLD, A], [TAR, 5146, ST, Palmerston, Palmerston Shopping Centre, Temple Terrace, Palmerston, 830, NT, A]]')
		select('LinesTbl', 'cell:4|Loc_Name,6(Ringwood)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'Ams_LocDownload_20041228_Extract2.bin'):
			click('No')
		close()
	close()
