useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'FJ_VB_Test.bin')
		click(commonBits.fl('Layout Wizard'))
		click('Right')
		select('TabbedPane', '')
##		assert_p('BmKeyedComboBox', 'Text', '7')
		assert_p('BmKeyedComboBox', 'Text', commonBits.fl('Fujitsu Variable Binary'))

		click('Right')
		select('TabbedPane', '')
##		select('Table', '')
		rightclick('Table', 'E,0')
##		select('Table', '')
		rightclick('Table', 'J,0')
		click('Right')
		select('TabbedPane', '')
		if commonBits.isVersion80():
			assert_p('Table', 'Content', '[[, 1, 3, 0, 0, true], [, 4, 4, 6, 0, true], [, 8, 2, 0, 0, true], [, 10, 35, 0, 0, true], [, 45, 40, 0, 0, true], [, 85, 40, 0, 0, true], [, 125, 35, 0, 0, true], [, 160, 4, 6, 0, true], [, 164, 6, 0, 0, true], [, 170, 4, 0, 0, true]]')
			assert_p('Table1', 'Content', '[[TAR, 5015, ST, Bankstown                          , Bankstown                               , Unit 2, 39-41 Allingham Street          , Condell Park                       , 2200,       , NSWA], [TAR, 5019, ST, Penrith                            , Penrith                                 , 58 Leland Street                        , Penrith                            , 2750,       , NSWA], [TAR, 5033, ST, Blacktown                          , Marayong                                , Dock 2, 11 Melissa Place                , Marayong                           , 2148,       , NSWA], [TAR, 5035, ST, Rockdale                           , Building B,  Portside DC                , 2-8 Mc Pherson Street                   , Botany                             , 2019,       , NSWA], [TAR, 5037, ST, Miranda                            , Westfield Shoppingtown                  , Cnr. Urunga Pde & The Kingsway          , Miranda                            , 2228,       , NSWA], [TAR, 5052, ST, Eastwood                           , Marayong Offsite Reserve                , 11 Melissa Place                        , Marayong                           , 2148,       , NSWA]]')
		else:
			assert_p('Table', 'Content', '[[, 1, 3, 0, 0, true], [, 4, 4, 6, 0, true], [, 8, 2, 0, 0, true], [, 10, 35, 0, 0, true], [, 45, 10, 0, 0, true], [, 55, 3, 0, 0, true], [, 58, 1, 0, 0, true], [, 59, 1, 0, 0, true], [, 60, 2, 0, 0, true], [, 62, 1, 0, 0, true], [, 63, 1, 0, 0, true], [, 64, 1, 0, 0, true], [, 65, 20, 0, 0, true], [, 85, 1, 6, 0, true], [, 86, 4, 0, 0, true], [, 90, 13, 0, 0, true], [, 103, 1, 0, 0, true], [, 104, 3, 0, 0, true], [, 107, 18, 0, 0, true], [, 125, 4, 0, 0, true], [, 129, 1, 111, 0, true], [, 130, 30, 0, 0, true], [, 160, 4, 6, 0, true], [, 164, 6, 0, 0, true], [, 170, 4, 0, 0, true]]')
			assert_p('Table1', 'Content', '[[TAR, 5015, ST, Bankstown                          , Bankstown ,    ,  ,  ,   ,  ,  ,  ,                     , U, nit , 2, 39-41 Alli, n, gha, m Street          , Cond, e, ll Park                       , 2200,       , NSWA], [TAR, 5019, ST, Penrith                            , Penrith   ,    ,  ,  ,   ,  ,  ,  ,                     , 5, 8 Le, land Street  ,  ,    ,                   , Penr, i, th                            , 2750,       , NSWA], [TAR, 5033, ST, Blacktown                          , Marayong  ,    ,  ,  ,   ,  ,  ,  ,                     , D, ock , 2, 11 Melissa,  , Pla, ce                , Mara, y, ong                           , 2148,       , NSWA], [TAR, 5035, ST, Rockdale                           , Building B, ,  , P, o, rt, s, i, d, e DC                , 2, -8 M, c Pherson Str, e, et ,                   , Bota, n, y                             , 2019,       , NSWA], [TAR, 5037, ST, Miranda                            , Westfield , Sho, p, p, in, g, t, o, wn                  , C, nr. , Urunga Pde & , T, he , Kingsway          , Mira, n, da                            , 2228,       , NSWA], [TAR, 5052, ST, Eastwood                           , Marayong O, ffs, i, t, e , R, e, s, erve                , 1, 1 Me, lissa Place  ,  ,    ,                   , Mara, y, ong                           , 2148,       , NSWA]]')
		select('Table', 'cell:' + commonBits.fl('Start') + ',1(4)')
		rightclick('Table', commonBits.fl('Start') + ',1')
		select_menu(commonBits.fl('Generate Field Names'))
		click('Right')
		select('TabbedPane', '')
		select('TextField', 'Wizard_Z_FjUnknown')
		click('Right')
		if commonBits.isVersion80():
			select('Table', 'cell:45 - 40|n4,1(Penrith)')
			assert_p('Table', 'Content', '[[TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, , NSWA], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, , NSWA], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, , NSWA], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, , NSWA], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, , NSWA], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, , NSWA]]')
			select('Table', 'cell:45 - 40|n4,1(Penrith)')
		else:
			select('Table', 'cell:45 - 10|n4,1(Penrith)')
			assert_p('Table', 'Content', '[[TAR, 5015, ST, Bankstown, Bankstown, , , , , , , , , U, nit, 2, 39-41 Alli, n, gha, m Street, Cond, e, ll Park, 2200, , NSWA], [TAR, 5019, ST, Penrith, Penrith, , , , , , , , , 5, 8 Le, land Street, , , , Penr, i, th, 2750, , NSWA], [TAR, 5033, ST, Blacktown, Marayong, , , , , , , , , D, ock, 2, 11 Melissa, , Pla, ce, Mara, y, ong, 2148, , NSWA], [TAR, 5035, ST, Rockdale, Building B, ,, P, o, rt, s, i, d, e DC, 2, -8 M, c Pherson Str, e, et, , Bota, n, y, 2019, , NSWA], [TAR, 5037, ST, Miranda, Westfield, Sho, p, p, in, g, t, o, wn, C, nr., Urunga Pde &, T, he, Kingsway, Mira, n, da, 2228, , NSWA], [TAR, 5052, ST, Eastwood, Marayong O, ffs, i, t, e, R, e, s, erve, 1, 1 Me, lissa Place, , , , Mara, y, ong, 2148, , NSWA]]')
			select('Table', 'cell:45 - 10|n4,1(Penrith)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

		select_menu(commonBits.fl('Record Layouts') + '>>' + commonBits.fl('Edit Layout'))
		select('TextField', 'Wizard_Z_FjUnknown')
		select('TextField1', '%')
		##click('Delete3')
		commonBits.delete3(click)

		if window(commonBits.fl('Delete: Wizard_Z_FjUnknown')):
			click('Yes')
		close()

		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

	close()
