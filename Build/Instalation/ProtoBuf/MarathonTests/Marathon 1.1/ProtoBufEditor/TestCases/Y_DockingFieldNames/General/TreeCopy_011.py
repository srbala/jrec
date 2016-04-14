useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window(commonBits.applicationName()):
		select('File_Txt', commonBits.sampleDir() + 'protoStoreSales7.bin')
		click('Edit1')
		select('LineTreeChild.FileDisplay_JTbl', 'cell:Tree,0(null)')
		rightclick('LineTreeChild.FileDisplay_JTbl', 'Tree,0')
		select_menu('Collapse Tree')
		select('LineTreeChild.FileDisplay_JTbl', 'cell:Tree,1(null)')
		rightclick('LineTreeChild.FileDisplay_JTbl', 'Tree,1')
		select_menu('Collapse Tree')
		select('LineTreeChild.Layouts_Txt', 'Store')
		assert_p('LineTreeChild.FileDisplay_JTbl', 'Content', '[[, , 20, Store: 20], [, , 59, Store: 59], [, , 166, Store: 166], [, , 184, Store: 184]]')
		select('LineTreeChild.FileDisplay_JTbl', 'rows:[1,2],columns:[Tree]')
		rightclick('LineTreeChild.FileDisplay_JTbl', 'Tree,2')
		select_menu('Copy Record#{s#}')
		select('LineTreeChild.FileDisplay_JTbl', 'cell:Tree,0(null)')
		rightclick('LineTreeChild.FileDisplay_JTbl', 'Tree,0')
		select_menu('Paste Record#{s#} Prior')
##		select('LineTreeChild.FileDisplay_JTbl', '')
		assert_p('LineTreeChild.FileDisplay_JTbl', 'Content', '[[, , 59, Store: 59], [, , 166, Store: 166], [, , 20, Store: 20], [, , 59, Store: 59], [, , 166, Store: 166], [, , 184, Store: 184]]')
		select_menu('Utilities>>Compare with Disk')
		assert_p('Table', 'Content', '[[, , , , , , , , , , ], [, Inserted, 1, 59, Store: 59, , , , , , ], [, , , , , , , , , , ], [, Inserted, 2, 335, Department: 335, , , , , , ], [, , , , , , , , , , ], [, Inserted, 3, 61664713, [40118, 40118], [1, -1], [17990, -17990], [SALE, RETURN], [17.99, -17.99], [17.99, -17.99], [\'\',\' -1\']], [, , , , , , , , , , ], [, Inserted, 4, 61684613, [40118], [1], [12990], [SALE], [12.99], [12.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 5, 1, 12990, 3, , , , , ], [, , , , , , , , , , ], [, Inserted, 6, 410, Department: 410, , , , , , ], [, , , , , , , , , , ], [, Inserted, 7, 68634752, [40118], [1], [8990], [SALE], [8.99], [8.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 8, 1, 8990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 9, 620, Department: 620, , , , , , ], [, , , , , , , , , , ], [, Inserted, 10, 60664659, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 11, 60694698, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 12, 2, 7980, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 13, 878, Department: 878, , , , , , ], [, , , , , , , , , , ], [, Inserted, 14, 60614487, [40118], [1], [5950], [SALE], [5.95], [5.95], [\'\']], [, , , , , , , , , , ], [, Inserted, 15, 63644339, [40118], [1], [12650], [SALE], [12.65], [12.65], [\'\']], [, , , , , , , , , , ], [, Inserted, 16, 2, 18600, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 17, 929, Department: 929, , , , , , ], [, , , , , , , , , , ], [, Inserted, 18, 67674686, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 19, 1, 3990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 20, 957, Department: 957, , , , , , ], [, , , , , , , , , , ], [, Inserted, 21, 62684217, [40118], [1], [9990], [SALE], [9.99], [9.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 22, 64614401, [40118, 40118], [1, 1], [1990, 1990], [SALE, SALE], [1.99, 1.99], [1.99, 1.99], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 23, 64624770, [40118], [1], [2590], [SALE], [2.59], [2.59], [\'\']], [, , , , , , , , , , ], [, Inserted, 24, 4, 16560, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 25, 61684613, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 26, 68634752, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 27, 60664659, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 28, 60694698, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 29, 60614487, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 30, 63644339, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 31, 67674686, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 32, 62684217, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 33, 64614401, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 34, 64624770, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 35, 11, 69110, 13, , , , , ], [, , , , , , , , , , ], [, Inserted, 36, 166, Store: 166, , , , , , ], [, , , , , , , , , , ], [, Inserted, 37, 60, Department: 60, , , , , , ], [, , , , , , , , , , ], [, Inserted, 38, 60614646, [40118], [1], [6000], [SALE], [6.0], [6.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 39, 60614707, [40118], [1], [6000], [SALE], [6.0], [6.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 40, 68654655, [40118], [1], [5080], [SALE], [5.08], [5.08], [\'\']], [, , , , , , , , , , ], [, Inserted, 41, 69644897, [40118], [1], [5080], [SALE], [5.08], [5.08], [\'\']], [, , , , , , , , , , ], [, Inserted, 42, 69654084, [40118], [1], [6000], [SALE], [6.0], [6.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 43, 5, 28160, 5, , , , , ], [, , , , , , , , , , ], [, Inserted, 44, 80, Department: 80, , , , , , ], [, , , , , , , , , , ], [, Inserted, 45, 60604100, [40118], [1], [13300], [SALE], [13.3], [13.3], [\'\']], [, , , , , , , , , , ], [, Inserted, 46, 69624033, [40118], [1], [18190], [SALE], [18.19], [18.19], [\'\']], [, , , , , , , , , , ], [, Inserted, 47, 2, 31490, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 48, 170, Department: 170, , , , , , ], [, , , , , , , , , , ], [, Inserted, 49, 68674560, [40118], [1], [5990], [SALE], [5.99], [5.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 50, 1, 5990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 51, 193, Department: 193, , , , , , ], [, , , , , , , , , , ], [, Inserted, 52, 62694485, [40118], [1], [17560], [SALE], [17.56], [17.56], [\'\']], [, , , , , , , , , , ], [, Inserted, 53, 62694706, [40118], [1], [13590], [SALE], [13.59], [13.59], [\'\']], [, , , , , , , , , , ], [, Inserted, 54, 62694843, [40118], [1], [13590], [SALE], [13.59], [13.59], [\'\']], [, , , , , , , , , , ], [, Inserted, 55, 67644384, [40118], [1], [23960], [SALE], [23.96], [23.96], [\'\']], [, , , , , , , , , , ], [, Inserted, 56, 68664211, [40118], [1], [11190], [SALE], [11.19], [11.19], [\'\']], [, , , , , , , , , , ], [, Inserted, 57, 69644164, [40118], [1], [21590], [SALE], [21.59], [21.59], [\'\']], [, , , , , , , , , , ], [, Inserted, 58, 6, 101480, 6, , , , , ], [, , , , , , , , , , ], [, Inserted, 59, 220, Department: 220, , , , , , ], [, , , , , , , , , , ], [, Inserted, 60, 64674633, [40118], [1], [15990], [SALE], [15.99], [15.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 61, 1, 15990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 62, 230, Department: 230, , , , , , ], [, , , , , , , , , , ], [, Inserted, 63, 69644961, [40118], [1], [9600], [SALE], [9.6], [9.6], [\'\']], [, , , , , , , , , , ], [, Inserted, 64, 1, 9600, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 65, 235, Department: 235, , , , , , ], [, , , , , , , , , , ], [, Inserted, 66, 64604513, [40118], [1], [16990], [SALE], [16.99], [16.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 67, 64674965, [40118, 40118, 40118], [1, -1, 1], [19990, -19990, 12000], [SALE, RETURN, SALE], [19.99, -19.99, 12.0], [19.99, -19.99, 12.0], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , , ], [, Inserted, 68, 2, 28990, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 69, 250, Department: 250, , , , , , ], [, , , , , , , , , , ], [, Inserted, 70, 69604743, [40118], [1], [29950], [SALE], [29.95], [29.95], [\'\']], [, , , , , , , , , , ], [, Inserted, 71, 1, 29950, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 72, 261, Department: 261, , , , , , ], [, , , , , , , , , , ], [, Inserted, 73, 60624523, [40118], [1], [12000], [SALE], [12.0], [12.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 74, 60624864, [40118], [1], [15000], [SALE], [15.0], [15.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 75, 62694605, [40118], [1], [25000], [SALE], [25.0], [25.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 76, 69634261, [40118], [1], [12000], [SALE], [12.0], [12.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 77, 69634263, [40118, 40118, 40118], [1, -1, 1], [25000, -25000, 12000], [SALE, RETURN, SALE], [25.0, -25.0, 12.0], [25.0, -25.0, 12.0], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , , ], [, Inserted, 78, 69634660, [40118], [1], [12000], [SALE], [12.0], [12.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 79, 69634922, [40118], [1], [19000], [SALE], [19.0], [19.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 80, 69644909, [40118], [1], [9000], [SALE], [9.0], [9.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 81, 8, 116000, 10, , , , , ], [, , , , , , , , , , ], [, Inserted, 82, 265, Department: 265, , , , , , ], [, , , , , , , , , , ], [, Inserted, 83, 62684207, [40118], [1], [19000], [SALE], [19.0], [19.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 84, 62684580, [40118], [1], [19000], [SALE], [19.0], [19.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 85, 69644602, [40118], [1], [19000], [SALE], [19.0], [19.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 86, 3, 57000, 3, , , , , ], [, , , , , , , , , , ], [, Inserted, 87, 270, Department: 270, , , , , , ], [, , , , , , , , , , ], [, Inserted, 88, 60664241, [40118], [1], [9000], [SALE], [9.0], [9.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 89, 60664302, [40118], [1], [9000], [SALE], [9.0], [9.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 90, 63634768, [40118], [1], [12000], [SALE], [12.0], [12.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 91, 69694959, [40118], [1], [11990], [SALE], [11.99], [11.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 92, 4, 41990, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 93, 275, Department: 275, , , , , , ], [, , , , , , , , , , ], [, Inserted, 94, 63654066, [40118], [1], [24990], [SALE], [24.99], [24.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 95, 1, 24990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 96, 280, Department: 280, , , , , , ], [, , , , , , , , , , ], [, Inserted, 97, 64624081, [40118], [1], [26240], [SALE], [26.24], [26.24], [\'\']], [, , , , , , , , , , ], [, Inserted, 98, 69684947, [40118], [1], [22490], [SALE], [22.49], [22.49], [\'\']], [, , , , , , , , , , ], [, Inserted, 99, 2, 48730, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 100, 320, Department: 320, , , , , , ], [, , , , , , , , , , ], [, Inserted, 101, 62664576, [40118], [1], [9720], [SALE], [9.72], [9.72], [\'\']], [, , , , , , , , , , ], [, Inserted, 102, 63634260, [40118], [1], [5590], [SALE], [5.59], [5.59], [\'\']], [, , , , , , , , , , ], [, Inserted, 103, 63654450, [40118], [1], [13990], [SALE], [13.99], [13.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 104, 63684449, [40118], [1], [16990], [SALE], [16.99], [16.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 105, 4, 46290, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 106, 335, Department: 335, , , , , , ], [, , , , , , , , , , ], [, Inserted, 107, 62604139, [40118], [1], [7990], [SALE], [7.99], [7.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 108, 1, 7990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 109, 355, Department: 355, , , , , , ], [, , , , , , , , , , ], [, Inserted, 110, 62634862, [40118], [1], [11890], [SALE], [11.89], [11.89], [\'\']], [, , , , , , , , , , ], [, Inserted, 111, 62654800, [40118], [1], [19990], [SALE], [19.99], [19.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 112, 69624221, [40118], [1], [16990], [SALE], [16.99], [16.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 113, 3, 48870, 3, , , , , ], [, , , , , , , , , , ], [, Inserted, 114, 360, Department: 360, , , , , , ], [, , , , , , , , , , ], [, Inserted, 115, 66674979, [40118], [1], [4500], [SALE], [4.5], [4.5], [\'\']], [, , , , , , , , , , ], [, Inserted, 116, 69694685, [40118], [1], [6990], [SALE], [6.99], [6.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 117, 69694814, [40118, 40118], [1, 1], [2500, 2500], [SALE, SALE], [2.5, 2.5], [2.5, 2.5], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 118, 69694937, [40118], [1], [2500], [SALE], [2.5], [2.5], [\'\']], [, , , , , , , , , , ], [, Inserted, 119, 5, 18990, 5, , , , , ], [, , , , , , , , , , ], [, Inserted, 120, 366, Department: 366, , , , , , ], [, , , , , , , , , , ], [, Inserted, 121, 62614014, [40118], [1], [14990], [SALE], [14.99], [14.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 122, 1, 14990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 123, 370, Department: 370, , , , , , ], [, , , , , , , , , , ], [, Inserted, 124, 62624382, [40118, 40118, 40118, 40118, 40118, 40118, 40118, 40118], [1, -1, 1, 1, -1, -1, 1, 1], [18980, -18980, 18980, 18980, -18980, -18980, 18980, 18980], [SALE, RETURN, SALE, SALE, RETURN, RETURN, SALE, SALE], [18.98, -18.98, 18.98, 18.98, -18.98, -18.98, 18.98, 18.98], [18.98, -18.98, 18.98, 18.98, -18.98, -18.98, 18.98, 18.98], [\'\',\' -1\',\' -1 1\',\' -1 1 1\',\' -1 1 1 -1\',\' -1 1 1 -1 -1\',\' -1 1 1 -1 -1 1\',\' -1 1 1 -1 -1 1 1\']], [, , , , , , , , , , ], [, Inserted, 125, 62664231, [40118], [1], [8990], [SALE], [8.99], [8.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 126, 62664347, [40118], [1], [8990], [SALE], [8.99], [8.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 127, 68614651, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 128, 5, 59930, 11, , , , , ], [, , , , , , , , , , ], [, Inserted, 129, 375, Department: 375, , , , , , ], [, , , , , , , , , , ], [, Inserted, 130, 62684907, [40118], [1], [13990], [SALE], [13.99], [13.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 131, 62694193, [40118, 40118, 40118], [1, -1, 1], [13990, -13990, 11990], [SALE, RETURN, SALE], [13.99, -13.99, 11.99], [13.99, -13.99, 11.99], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , , ], [, Inserted, 132, 2, 25980, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 133, 395, Department: 395, , , , , , ], [, , , , , , , , , , ], [, Inserted, 134, 60614265, [40118, 40118, 40118, 40118, 40118, 40118, 40118], [1, 1, -1, -1, 1, -1, 1], [15990, 15990, -15990, -15990, 15990, -15990, 12800], [SALE, SALE, RETURN, RETURN, SALE, RETURN, SALE], [15.99, 15.99, -15.99, -15.99, 15.99, -15.99, 12.8], [15.99, 15.99, -15.99, -15.99, 15.99, -15.99, 12.8], [\'\',\' 1\',\' 1 -1\',\' 1 -1 -1\',\' 1 -1 -1 1\',\' 1 -1 -1 1 -1\',\' 1 -1 -1 1 -1 1\']], [, , , , , , , , , , ], [, Inserted, 135, 63614741, [40118], [1], [27990], [SALE], [27.99], [27.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 136, 2, 40790, 8, , , , , ], [, , , , , , , , , , ], [, Inserted, 137, 405, Department: 405, , , , , , ], [, , , , , , , , , , ], [, Inserted, 138, 62614815, [40118], [1], [20000], [SALE], [20.0], [20.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 139, 1, 20000, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 140, 410, Department: 410, , , , , , ], [, , , , , , , , , , ], [, Inserted, 141, 63684098, [40118, 40118, 40118], [1, 1, 1], [1980, 1980, 1980], [SALE, SALE, SALE], [1.98, 1.98, 1.98], [1.98, 1.98, 1.98], [\'\',\' 1\',\' 1 1\']], [, , , , , , , , , , ], [, Inserted, 142, 64684719, [40118], [1], [9990], [SALE], [9.99], [9.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 143, 4, 15930, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 144, 415, Department: 415, , , , , , ], [, , , , , , , , , , ], [, Inserted, 145, 62684548, [40118, 40118], [1, 1], [39990, 39990], [SALE, SALE], [39.99, 39.99], [39.99, 39.99], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 146, 2, 79980, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 147, 432, Department: 432, , , , , , ], [, , , , , , , , , , ], [, Inserted, 148, 61694741, [40118], [1], [9060], [SALE], [9.06], [9.06], [\'\']], [, , , , , , , , , , ], [, Inserted, 149, 62614534, [40118], [1], [9090], [SALE], [9.09], [9.09], [\'\']], [, , , , , , , , , , ], [, Inserted, 150, 62664568, [40118], [1], [5990], [SALE], [5.99], [5.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 151, 62694387, [40118], [1], [7990], [SALE], [7.99], [7.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 152, 4, 32130, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 153, 440, Department: 440, , , , , , ], [, , , , , , , , , , ], [, Inserted, 154, 64684534, [40118], [1], [14990], [SALE], [14.99], [14.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 155, 1, 14990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 156, 455, Department: 455, , , , , , ], [, , , , , , , , , , ], [, Inserted, 157, 62664151, [40118], [1], [25000], [SALE], [25.0], [25.0], [\'\']], [, , , , , , , , , , ], [, Inserted, 158, 1, 25000, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 159, 471, Department: 471, , , , , , ], [, , , , , , , , , , ], [, Inserted, 160, 62664674, [40118], [1], [24990], [SALE], [24.99], [24.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 161, 1, 24990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 162, 475, Department: 475, , , , , , ], [, , , , , , , , , , ], [, Inserted, 163, 62694575, [40118], [1], [14990], [SALE], [14.99], [14.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 164, 1, 14990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 165, 485, Department: 485, , , , , , ], [, , , , , , , , , , ], [, Inserted, 166, 64674609, [40118], [1], [29990], [SALE], [29.99], [29.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 167, 1, 29990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 168, 500, Department: 500, , , , , , ], [, , , , , , , , , , ], [, Inserted, 169, 60624185, [40118], [1], [8990], [SALE], [8.99], [8.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 170, 60624314, [40118], [1], [8990], [SALE], [8.99], [8.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 171, 2, 17980, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 172, 520, Department: 520, , , , , , ], [, , , , , , , , , , ], [, Inserted, 173, 62684028, [40118], [1], [29990], [SALE], [29.99], [29.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 174, 1, 29990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 175, 650, Department: 650, , , , , , ], [, , , , , , , , , , ], [, Inserted, 176, 62634996, [40118], [1], [9990], [SALE], [9.99], [9.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 177, 1, 9990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 178, 670, Department: 670, , , , , , ], [, , , , , , , , , , ], [, Inserted, 179, 61674701, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 180, 63654007, [40118], [1], [56990], [SALE], [56.99], [56.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 181, 2, 60980, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 182, 685, Department: 685, , , , , , ], [, , , , , , , , , , ], [, Inserted, 183, 61684889, [40118, 40118], [1, 1], [4490, 4490], [SALE, SALE], [4.49, 4.49], [4.49, 4.49], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 184, 2, 8980, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 185, 801, Department: 801, , , , , , ], [, , , , , , , , , , ], [, Inserted, 186, 64604876, [40118, 40118], [1, 1], [29620, 29620], [SALE, SALE], [29.62, 29.62], [29.62, 29.62], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 187, 64644495, [40118, 40118], [1, 1], [29650, 29650], [SALE, SALE], [29.65, 29.65], [29.65, 29.65], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 188, 67624103, [40118], [1], [16500], [SALE], [16.5], [16.5], [\'\']], [, , , , , , , , , , ], [, Inserted, 189, 5, 135040, 5, , , , , ], [, , , , , , , , , , ], [, Inserted, 190, 805, Department: 805, , , , , , ], [, , , , , , , , , , ], [, Inserted, 191, 60684907, [40118], [1], [5500], [SALE], [5.5], [5.5], [\'\']], [, , , , , , , , , , ], [, Inserted, 192, 1, 5500, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 193, 830, Department: 830, , , , , , ], [, , , , , , , , , , ], [, Inserted, 194, 65604476, [40118], [1], [19950], [SALE], [19.95], [19.95], [\'\']], [, , , , , , , , , , ], [, Inserted, 195, 1, 19950, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 196, 845, Department: 845, , , , , , ], [, , , , , , , , , , ], [, Inserted, 197, 62654454, [40118], [1], [5950], [SALE], [5.95], [5.95], [\'\']], [, , , , , , , , , , ], [, Inserted, 198, 64634712, [40118], [1], [3900], [SALE], [3.9], [3.9], [\'\']], [, , , , , , , , , , ], [, Inserted, 199, 2, 9850, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 200, 851, Department: 851, , , , , , ], [, , , , , , , , , , ], [, Inserted, 201, 62674092, [40118], [1], [15990], [SALE], [15.99], [15.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 202, 62694170, [40118], [1], [16990], [SALE], [16.99], [16.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 203, 2, 32980, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 204, 870, Department: 870, , , , , , ], [, , , , , , , , , , ], [, Inserted, 205, 63624299, [40118], [1], [10990], [SALE], [10.99], [10.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 206, 63624367, [40118], [1], [11190], [SALE], [11.19], [11.19], [\'\']], [, , , , , , , , , , ], [, Inserted, 207, 2, 22180, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 208, 902, Department: 902, , , , , , ], [, , , , , , , , , , ], [, Inserted, 209, 68644966, [40118, 40118, 40118], [1, -1, 1], [12500, -12500, 10], [SALE, RETURN, SALE], [12.5, -12.5, 0.01], [12.5, -12.5, 0.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , , ], [, Inserted, 210, 69614229, [40118], [1], [15950], [SALE], [15.95], [15.95], [\'\']], [, , , , , , , , , , ], [, Inserted, 211, 2, 15960, 4, , , , , ], [, , , , , , , , , , ], [, Inserted, 212, 904, Department: 904, , , , , , ], [, , , , , , , , , , ], [, Inserted, 213, 63694928, [40118], [1], [11490], [SALE], [11.49], [11.49], [\'\']], [, , , , , , , , , , ], [, Inserted, 214, 69664661, [40118], [1], [14950], [SALE], [14.95], [14.95], [\'\']], [, , , , , , , , , , ], [, Inserted, 215, 2, 26440, 2, , , , , ], [, , , , , , , , , , ], [, Inserted, 216, 905, Department: 905, , , , , , ], [, , , , , , , , , , ], [, Inserted, 217, 60654072, [40118, 40118], [1, 1], [4330, 4330], [SALE, SALE], [4.33, 4.33], [4.33, 4.33], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 218, 68604583, [40118, 40118, 40118, 40118, 40118], [1, -1, 1, -1, 1], [15990, -15990, 15990, -15990, 12800], [SALE, RETURN, SALE, RETURN, SALE], [15.99, -15.99, 15.99, -15.99, 12.8], [15.99, -15.99, 15.99, -15.99, 12.8], [\'\',\' -1\',\' -1 1\',\' -1 1 -1\',\' -1 1 -1 1\']], [, , , , , , , , , , ], [, Inserted, 219, 68614329, [40118], [1], [39990], [SALE], [39.99], [39.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 220, 69614011, [40118], [1], [6990], [SALE], [6.99], [6.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 221, 5, 68440, 9, , , , , ], [, , , , , , , , , , ], [, Inserted, 222, 910, Department: 910, , , , , , ], [, , , , , , , , , , ], [, Inserted, 223, 69674069, [40118], [1], [10490], [SALE], [10.49], [10.49], [\'\']], [, , , , , , , , , , ], [, Inserted, 224, 1, 10490, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 225, 929, Department: 929, , , , , , ], [, , , , , , , , , , ], [, Inserted, 226, 60694417, [40118], [1], [650], [SALE], [0.65], [0.65], [\'\']], [, , , , , , , , , , ], [, Inserted, 227, 63634081, [40118], [1], [3890], [SALE], [3.89], [3.89], [\'\']], [, , , , , , , , , , ], [, Inserted, 228, 65694328, [40118], [1], [590], [SALE], [0.59], [0.59], [\'\']], [, , , , , , , , , , ], [, Inserted, 229, 67664645, [40118], [1], [1390], [SALE], [1.39], [1.39], [\'\']], [, , , , , , , , , , ], [, Inserted, 230, 67664966, [40118, 40118], [1, 1], [890, 890], [SALE, SALE], [0.89, 0.89], [0.89, 0.89], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 231, 6, 8300, 6, , , , , ], [, , , , , , , , , , ], [, Inserted, 232, 957, Department: 957, , , , , , ], [, , , , , , , , , , ], [, Inserted, 233, 62664909, [40118], [1], [3290], [SALE], [3.29], [3.29], [\'\']], [, , , , , , , , , , ], [, Inserted, 234, 62674492, [40118, 40118], [1, 1], [1490, 1490], [SALE, SALE], [1.49, 1.49], [1.49, 1.49], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 235, 62674751, [40118], [1], [1990], [SALE], [1.99], [1.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 236, 64654284, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 237, 66624253, [40118, 40118], [1, 1], [3490, 3490], [SALE, SALE], [3.49, 3.49], [3.49, 3.49], [\'\',\' 1\']], [, , , , , , , , , , ], [, Inserted, 238, 66624829, [40118], [1], [1990], [SALE], [1.99], [1.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 239, 8, 21220, 8, , , , , ], [, , , , , , , , , , ], [, Inserted, 240, 970, Department: 970, , , , , , ], [, , , , , , , , , , ], [, Inserted, 241, 67634503, [40118], [1], [24990], [SALE], [24.99], [24.99], [\'\']], [, , , , , , , , , , ], [, Inserted, 242, 1, 24990, 1, , , , , ], [, , , , , , , , , , ], [, Inserted, 243, 60614646, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 244, 60614707, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 245, 68654655, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 246, 69644897, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 247, 69654084, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 248, 60604100, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 249, 69624033, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 250, 68674560, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 251, 62694485, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 252, 62694706, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 253, 62694843, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 254, 67644384, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 255, 68664211, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 256, 69644164, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 257, 64674633, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 258, 69644961, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 259, 64604513, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 260, 64674965, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 261, 69604743, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 262, 60624523, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 263, 60624864, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 264, 62694605, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 265, 69634261, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 266, 69634263, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 267, 69634660, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 268, 69634922, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 269, 69644909, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 270, 62684207, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 271, 62684580, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 272, 69644602, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 273, 60664241, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 274, 60664302, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 275, 63634768, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 276, 69694959, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 277, 63654066, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 278, 64624081, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 279, 69684947, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 280, 62664576, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 281, 63634260, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 282, 63654450, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 283, 63684449, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 284, 62604139, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 285, 62634862, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 286, 62654800, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 287, 69624221, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 288, 66674979, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 289, 69694685, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 290, 69694814, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 291, 69694937, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 292, 62614014, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 293, 62624382, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 294, 62664231, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 295, 62664347, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 296, 68614651, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 297, 62684907, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 298, 62694193, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 299, 60614265, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 300, 63614741, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 301, 62614815, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 302, 63684098, 3, , , , , , ], [, , , , , , , , , , ], [, Inserted, 303, 64684719, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 304, 62684548, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 305, 61694741, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 306, 62614534, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 307, 62664568, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 308, 62694387, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 309, 64684534, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 310, 62664151, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 311, 62664674, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 312, 62694575, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 313, 64674609, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 314, 60624185, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 315, 60624314, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 316, 62684028, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 317, 62634996, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 318, 61674701, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 319, 63654007, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 320, 61684889, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 321, 64604876, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 322, 64644495, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 323, 67624103, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 324, 60684907, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 325, 65604476, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 326, 62654454, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 327, 64634712, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 328, 62674092, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 329, 62694170, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 330, 63624299, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 331, 63624367, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 332, 68644966, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 333, 69614229, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 334, 63694928, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 335, 69664661, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 336, 60654072, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 337, 68604583, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 338, 68614329, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 339, 69614011, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 340, 69674069, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 341, 60694417, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 342, 63634081, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 343, 65694328, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 344, 67664645, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 345, 67664966, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 346, 62664909, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 347, 62674492, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 348, 62674751, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 349, 64654284, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 350, 66624253, 2, , , , , , ], [, , , , , , , , , , ], [, Inserted, 351, 66624829, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 352, 67634503, 1, , , , , , ], [, , , , , , , , , , ], [, Inserted, 353, 122, 1591450, 146, , , , , ]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window(r'Save Changes to file: ' + commonBits.sampleDir() + 'protoStoreSales7.bin'):
			click('No')
		close()
	close()
