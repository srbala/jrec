useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_LocDownload_20041228_Extract2.txt')
		click('Create Layout Wizard')
		##select('TextField2', 'Wizard - ZZ1')
		select('BmKeyedComboBox1', '2')
		click('Right')
		#select('Table', '')
		rightclick('Table', 'D,0')
		#select('Table', '')
		rightclick('Table', 'H,0')
		#select('Table', '')
		rightclick('Table', 'J,0')
		#select('Table', '')
		rightclick('Table', 'U,0')
		#select('Table', '')
		rightclick('Table', 'AB,0')
		click('Right')
		select('Table', 'cell:Field Name,1()')
		assert_p('Table', 'Content', '[[, 1, 3, 2, 0, true], [, 4, 4, 2, 0, true], [, 8, 2, 2, 0, true], [, 10, 11, 2, 0, true], [, 21, 7, 2, 0, true], [, 28, 146, 2, 0, true]]')
		select('Table', 'cell:Field Name,1()')
		select('Table1', 'cell:B,1(5850)')
		assert_p('Table1', 'Content', '[[TAR, 5839, DC, DC - Taras , Ave    ,                                                          30-68 Taras Ave                         Altona North                       3025      VICA], [TAR, 5850, DC, VIC West Ad,  Suppor, t                                                        Lot 2 Little Boundary Rd                Laverton                           3028      VICA], [TAR, 5015, ST, Bankstown  ,        ,                  Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA], [TAR, 5019, ST, Penrith    ,        ,                  Penrith                                 58 Leland Street                        Penrith                            2750      NSWA], [TAR, 5033, ST, Blacktown  ,        ,                  Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA], [TAR, 5096, ST, Canberra Ci, vic    ,                  Target Canberra                         Canberra City Centre, Akuna Ave         Canberra                           2601      ACTA], [TAR, 5012, ST, Ringwood   ,        ,                  Ringwood                                Seymour Street                          Ringwood                           3134      VICA], [TAR, 5030, ST, Epping     ,        ,                  Epping Plaza Shopping Centre            Cnr. High & Cooper Streets              Epping                             3076      VICA], [TAR, 5054, ST, Highpoint C, ity    ,                  Laverton                                Lot 2, Cnr Lt Boundry & Old Geelong RoadLaverton                           3028      VICA], [TAR, 5062, ST, Castletown ,        ,                  Townsville                              Cnr. Woolcock St. & Kings Road          Townsville                         4810      QLDA], [TAR, 5138, ST, Cairns Cent, ral    ,                  Cairns                                  Cnr. McLeod & Aplin Streets             Cairns                             4870      QLDA], [TAR, 5141, ST, The Willows,        ,                  Thuringowa Central                      Cnr Thuringowa Drive &  Range Rd        Thuringowa Central                 4817      QLDA], [TAR, 5146, ST, Palmerston ,        ,                  Palmerston Shopping Centre              Temple Terrace                          Palmerston                         0830      NT A], [TAR, 5002, ST, Coffs Harbo, ur     ,                  Coffs Harbour                           Cnr. Park Beach Road & Pacific Hwy      Coffs Harbour                      2450      NSWA], [TAR, 5966, DC, Huntingwood,  DC    ,                  Huntingwood DC                          35 Huntingwood Drive                    Huntingwood                        2148      NSWA], [TAR, 5967, DC, Hendra DC  ,        ,                  Hendra DC                               Cnr Headly Ave & Nudgee Road            Hendra                             4011      QLDA], [TAR, 5968, DC, Beverly DC ,        ,                  Beverly DC                              117 Main Street                         Beverly                            5009      SA A]]')
		#select('Table1', '')
		select('Table', 'Brand', 'Field Name,0')
		select('Table', 'Store', 'Field Name,1')
		select('Table', 'Type', 'Field Name,2')
		select('Table', 'a1', 'Field Name,3')
		select('Table', 'a2', 'Field Name,4')
		select('Table', 'a3', 'Field Name,5')
		select('Table', 'cell:Field Name,4(a2)')
		assert_p('Table', 'Content', '[[Brand, 1, 3, 2, 0, true], [Store, 4, 4, 2, 0, true], [Type, 8, 2, 2, 0, true], [a1, 10, 11, 2, 0, true], [a2, 21, 7, 2, 0, true], [a3, 28, 146, 2, 0, true]]')
		select('Table', 'cell:Field Name,1(Store)')
		assert_p('Table', 'Text', 'Store', 'Field Name,1')
		select('Table', 'cell:Field Name,1(Store)')
		select('Table1', 'cell:Brand,0(TAR)')
		assert_p('Table1', 'Text', 'TAR', 'Brand,0')
		select('Table1', 'cell:a1,0(DC - Taras )')
		assert_p('Table1', 'Text', 'DC - Taras ', 'a1,0')
		select('Table1', 'cell:a1,2(Bankstown  )')
		assert_p('Table1', 'Content', '[[TAR, 5839, DC, DC - Taras , Ave    ,                                                          30-68 Taras Ave                         Altona North                       3025      VICA], [TAR, 5850, DC, VIC West Ad,  Suppor, t                                                        Lot 2 Little Boundary Rd                Laverton                           3028      VICA], [TAR, 5015, ST, Bankstown  ,        ,                  Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA], [TAR, 5019, ST, Penrith    ,        ,                  Penrith                                 58 Leland Street                        Penrith                            2750      NSWA], [TAR, 5033, ST, Blacktown  ,        ,                  Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA], [TAR, 5096, ST, Canberra Ci, vic    ,                  Target Canberra                         Canberra City Centre, Akuna Ave         Canberra                           2601      ACTA], [TAR, 5012, ST, Ringwood   ,        ,                  Ringwood                                Seymour Street                          Ringwood                           3134      VICA], [TAR, 5030, ST, Epping     ,        ,                  Epping Plaza Shopping Centre            Cnr. High & Cooper Streets              Epping                             3076      VICA], [TAR, 5054, ST, Highpoint C, ity    ,                  Laverton                                Lot 2, Cnr Lt Boundry & Old Geelong RoadLaverton                           3028      VICA], [TAR, 5062, ST, Castletown ,        ,                  Townsville                              Cnr. Woolcock St. & Kings Road          Townsville                         4810      QLDA], [TAR, 5138, ST, Cairns Cent, ral    ,                  Cairns                                  Cnr. McLeod & Aplin Streets             Cairns                             4870      QLDA], [TAR, 5141, ST, The Willows,        ,                  Thuringowa Central                      Cnr Thuringowa Drive &  Range Rd        Thuringowa Central                 4817      QLDA], [TAR, 5146, ST, Palmerston ,        ,                  Palmerston Shopping Centre              Temple Terrace                          Palmerston                         0830      NT A], [TAR, 5002, ST, Coffs Harbo, ur     ,                  Coffs Harbour                           Cnr. Park Beach Road & Pacific Hwy      Coffs Harbour                      2450      NSWA], [TAR, 5966, DC, Huntingwood,  DC    ,                  Huntingwood DC                          35 Huntingwood Drive                    Huntingwood                        2148      NSWA], [TAR, 5967, DC, Hendra DC  ,        ,                  Hendra DC                               Cnr Headly Ave & Nudgee Road            Hendra                             4011      QLDA], [TAR, 5968, DC, Beverly DC ,        ,                  Beverly DC                              117 Main Street                         Beverly                            5009      SA A]]')
		select('Table1', 'cell:Store,1(5850)')
		assert_p('Table1', 'Text', '5850', 'Store,1')
		select('Table1', 'cell:Type,2(ST)')
		assert_p('Table1', 'Text', 'ST', 'Type,2')
		select('Table1', 'cell:a2,1( Suppor)')
		assert_p('Table1', 'Text', ' Suppor', 'a2,1')
		select('Table1', 'cell:a2,1( Suppor)')
		click('Right')

		#   Save Layout panel
		#   -----------------
		select('TabbedPane', '')
		select('TextField', 'Wizard - ZZ1')
		click('Right')

		select('Table', 'cell:10 - 11|a1,2(Bankstown  )')
		assert_p('Table', 'Text', 'Bankstown  ', '10 - 11|a1,2')
		select('Table', 'cell:10 - 11|a1,4(Blacktown  )')
		assert_p('Table', 'Content', '[[TAR, 5839, DC, DC - Taras , Ave    ,                                                          30-68 Taras Ave                         Altona North                       3025      VICA], [TAR, 5850, DC, VIC West Ad,  Suppor, t                                                        Lot 2 Little Boundary Rd                Laverton                           3028      VICA], [TAR, 5015, ST, Bankstown  ,        ,                  Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA], [TAR, 5019, ST, Penrith    ,        ,                  Penrith                                 58 Leland Street                        Penrith                            2750      NSWA], [TAR, 5033, ST, Blacktown  ,        ,                  Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA], [TAR, 5096, ST, Canberra Ci, vic    ,                  Target Canberra                         Canberra City Centre, Akuna Ave         Canberra                           2601      ACTA], [TAR, 5012, ST, Ringwood   ,        ,                  Ringwood                                Seymour Street                          Ringwood                           3134      VICA], [TAR, 5030, ST, Epping     ,        ,                  Epping Plaza Shopping Centre            Cnr. High & Cooper Streets              Epping                             3076      VICA], [TAR, 5054, ST, Highpoint C, ity    ,                  Laverton                                Lot 2, Cnr Lt Boundry & Old Geelong RoadLaverton                           3028      VICA], [TAR, 5062, ST, Castletown ,        ,                  Townsville                              Cnr. Woolcock St. & Kings Road          Townsville                         4810      QLDA], [TAR, 5138, ST, Cairns Cent, ral    ,                  Cairns                                  Cnr. McLeod & Aplin Streets             Cairns                             4870      QLDA], [TAR, 5141, ST, The Willows,        ,                  Thuringowa Central                      Cnr Thuringowa Drive &  Range Rd        Thuringowa Central                 4817      QLDA], [TAR, 5146, ST, Palmerston ,        ,                  Palmerston Shopping Centre              Temple Terrace                          Palmerston                         0830      NT A], [TAR, 5002, ST, Coffs Harbo, ur     ,                  Coffs Harbour                           Cnr. Park Beach Road & Pacific Hwy      Coffs Harbour                      2450      NSWA], [TAR, 5966, DC, Huntingwood,  DC    ,                  Huntingwood DC                          35 Huntingwood Drive                    Huntingwood                        2148      NSWA], [TAR, 5967, DC, Hendra DC  ,        ,                  Hendra DC                               Cnr Headly Ave & Nudgee Road            Hendra                             4011      QLDA], [TAR, 5968, DC, Beverly DC ,        ,                  Beverly DC                              117 Main Street                         Beverly                            5009      SA A]]')
		select('Table', 'cell:10 - 11|a1,4(Blacktown  )')
		rightclick('Table', '4 - 4|Store,2')
		select_menu('Edit Record')
##		select('Table1', 'cell:10 - 11|a1,4(Blacktown  )')
		select('Table', 'cell:Data,1(5015)')
		assert_p('Table', 'Content', '[[Brand, 1, 3, TAR, TAR], [Store, 4, 4, 5015, 5015], [Type, 8, 2, ST, ST], [a1, 10, 11, Bankstown  , Bankstown], [a2, 21, 7,        , ], [a3, 28, 146,                  Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA,                  Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA]]')
		select('Table', 'cell:Data,3(Bankstown  )')
		assert_p('Table', 'Text', 'Bankstown  ', 'Data,3')
		select('Table', 'cell:Data,3(Bankstown  )')
		click('Right')
		select('Table', 'cell:Data,3(Penrith    )')
		assert_p('Table', 'Text', 'Penrith    ', 'Data,3')
		select('Table', 'cell:Data,1(5019)')
		assert_p('Table', 'Content', '[[Brand, 1, 3, TAR, TAR], [Store, 4, 4, 5019, 5019], [Type, 8, 2, ST, ST], [a1, 10, 11, Penrith    , Penrith], [a2, 21, 7,        , ], [a3, 28, 146,                  Penrith                                 58 Leland Street                        Penrith                            2750      NSWA,                  Penrith                                 58 Leland Street                        Penrith                            2750      NSWA]]')
		select('Table', 'cell:Data,1(5019)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		#click('ScrollPane$ScrollBar', 8, 118)

		select_menu('Record Layouts>>Edit Layout')
		select('TextField', 'Wizard - ZZ1%')
		select('TextField1', '%')
		select('Table', 'cell:Description,0()')
		click('Delete3')

		if window('Delete: Wizard - ZZ1'):
			click('Yes')
		close()

		click('BasicInternalFrameTitlePane$NoFocusButton2')

		commonBits.setRecordLayout(select, 'ams Store')
		click('Edit1')
		select('Table', 'cell:10 - 35|Loc Name,2(Bankstown)')
		rightclick('Table', '10 - 35|Loc Name,2')
		select_menu('Edit Record')
##		select('Table1', 'cell:10 - 35|Loc Name,2(Bankstown)')
		select('Table', 'cell:Data,4(Bankstown)')
		assert_p('Table', 'Text', 'Bankstown', 'Data,4')
		select('Table', 'cell:Data,5(Unit 2, 39-41 Allingham Street)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5015, 5015], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Bankstown, Bankstown], [Loc Addr Ln1, 45, 40, Bankstown, Bankstown], [Loc Addr Ln2, 85, 40, Unit 2, 39-41 Allingham Street, Unit 2, 39-41 Allingham Street], [Loc Addr Ln3, 125, 35, Condell Park, Condell Park], [Loc Postcode, 160, 10, 2200, 2200], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Unit 2, 39-41 Allingham Street)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
