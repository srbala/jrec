useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoStoreSales3xxx_Compare.bin')
		click('Edit1')
		click('Export')
		select('TabbedPane', 'CSV')
		select('CheckBox2', 'true')
		select('ComboBox1', ';')
		select('CheckBox12', 'true')
		select('CheckBox13', 'true')
		click('save file')
		assert_p('Table', 'Content', '[[, , , , , , , , ], [Store, , , , , 20, Store: 20, , ], [Store, department\'s, , , , , , , ], [Store, department\'s, Deptartment, , , 170, Department: 170, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 63604808, 40118, 1, 4870], [Store, department\'s, Deptartment, summary, , 1, 4870, 1, ], [Store, department\'s, Deptartment, , , 280, Department: 280, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 69684558, 40118, 1, 19000], [Store, department\'s, Deptartment, product\'s, Product, 69684558, 40118, -1, -19000], [Store, department\'s, Deptartment, product\'s, Product, 69694158, 40118, 1, 19000], [Store, department\'s, Deptartment, product\'s, Product, 69694158, 40118, 1, 5010], [Store, department\'s, Deptartment, summary, , 2, 10020, 6, ], [Store, department\'s, Deptartment, , , 685, Department: 685, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 62684671, 40118, 1, 69990], [Store, department\'s, Deptartment, product\'s, Product, 62684671, 40118, -1, -69990], [Store, department\'s, Deptartment, summary, , 0, 0, 2, ], [Store, department\'s, Deptartment, , , 957, Department: 957, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 63674861, 40118, 10, 2700], [Store, department\'s, Deptartment, product\'s, Product, 64634429, 40118, 1, 3990], [Store, department\'s, Deptartment, product\'s, Product, 66624458, 40118, 1, 890], [Store, department\'s, Deptartment, summary, , 12, 7580, 3, ], [Store, order\'s, , , , , , , ], [Store, order\'s, Order, , , 63604808, 1, , ], [Store, order\'s, Order, , , 69694158, 1, , ], [Store, order\'s, Order, , , 63674861, 10, , ], [Store, order\'s, Order, , , 64634429, 1, , ], [Store, order\'s, Order, , , 66624458, 1, , ], [Store, summary, , , , 16, 26060, 13, ], [Store, , , , , 59, Store: 59, , ], [Store, department\'s, , , , , , , ], [Store, department\'s, Deptartment, , , 335, Department: 335, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 61664713, 40118, 1, 17990], [Store, department\'s, Deptartment, product\'s, Product, 61664713, 40118, -1, -17990], [Store, department\'s, Deptartment, product\'s, Product, 61684613, 40118, 1, 12990], [Store, department\'s, Deptartment, summary, , 1, 12990, 3, ], [Store, department\'s, Deptartment, , , 410, Department: 410, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 68634752, 40118, 1, 8990], [Store, department\'s, Deptartment, summary, , 1, 8990, 1, ], [Store, department\'s, Deptartment, , , 620, Department: 620, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 60664659, 40118, 1, 3990], [Store, department\'s, Deptartment, product\'s, Product, 60694698, 40118, 1, 3990], [Store, department\'s, Deptartment, summary, , 2, 7980, 2, ], [Store, department\'s, Deptartment, , , 878, Department: 878, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 60614487, 40118, 1, 5950], [Store, department\'s, Deptartment, product\'s, Product, 63644339, 40118, 1, 12650], [Store, department\'s, Deptartment, summary, , 2, 18600, 2, ], [Store, department\'s, Deptartment, , , 929, Department: 929, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 67674686, 40118, 1, 3990], [Store, department\'s, Deptartment, summary, , 1, 3990, 1, ], [Store, department\'s, Deptartment, , , 957, Department: 957, , ], [Store, department\'s, Deptartment, product\'s, , , , , ], [Store, department\'s, Deptartment, product\'s, Product, 62684217, 40118, 1, 9990], [Store, department\'s, Deptartment, product\'s, Product, 64614401, 40118, 1, 1990], [Store, department\'s, Deptartment, product\'s, Product, 64614401, 40118, 1, 1990], [Store, department\'s, Deptartment, product\'s, Product, 64624770, 40118, 1, 2590], [Store, department\'s, Deptartment, summary, , 4, 16560, 4, ], [Store, order\'s, , , , , , , ], [Store, order\'s, Order, , , 61684613, 1, , ], [Store, order\'s, Order, , , 68634752, 1, , ], [Store, order\'s, Order, , , 60664659, 1, , ], [Store, order\'s, Order, , , 60694698, 1, , ], [Store, order\'s, Order, , , 60614487, 1, , ], [Store, order\'s, Order, , , 63644339, 1, , ], [Store, order\'s, Order, , , 67674686, 1, , ], [Store, order\'s, Order, , , 62684217, 1, , ], [Store, order\'s, Order, , , 64614401, 2, , ], [Store, order\'s, Order, , , 64624770, 1, , ], [Store, summary, , , , 11, 69110, 13, ]]')
##		assert_p('Table', 'Content', '[[Store, , , , , 20, Store: 20, , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, summary, , , , , , , ], [Store, , , , , 59, Store: 59, , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, department\'s, Deptartment, , , , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, product\'s, Product, , , , ], [Store, department\'s, Deptartment, summary, , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, order\'s, Order, , , , , , ], [Store, summary, , , , , , , ]]')

		select('LayoutCombo', 'Full Line')
		assert_p('Table', 'Content', '[[;;;;], [Store;;;;;20;Store: 20], [Store;department\'s;;;], [Store;department\'s;Deptartment;;;170;Department: 170], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;63604808;40118;1;4870], [Store;department\'s;Deptartment;summary;;1;4870;1], [Store;department\'s;Deptartment;;;280;Department: 280], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;69684558;40118;1;19000], [Store;department\'s;Deptartment;product\'s;Product;69684558;40118;-1;-19000], [Store;department\'s;Deptartment;product\'s;Product;69694158;40118;1;19000], [Store;department\'s;Deptartment;product\'s;Product;69694158;40118;1;5010], [Store;department\'s;Deptartment;summary;;2;10020;6], [Store;department\'s;Deptartment;;;685;Department: 685], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;62684671;40118;1;69990], [Store;department\'s;Deptartment;product\'s;Product;62684671;40118;-1;-69990], [Store;department\'s;Deptartment;summary;;0;0;2], [Store;department\'s;Deptartment;;;957;Department: 957], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;63674861;40118;10;2700], [Store;department\'s;Deptartment;product\'s;Product;64634429;40118;1;3990], [Store;department\'s;Deptartment;product\'s;Product;66624458;40118;1;890], [Store;department\'s;Deptartment;summary;;12;7580;3], [Store;order\'s;;;], [Store;order\'s;Order;;;63604808;1], [Store;order\'s;Order;;;69694158;1], [Store;order\'s;Order;;;63674861;10], [Store;order\'s;Order;;;64634429;1], [Store;order\'s;Order;;;66624458;1], [Store;summary;;;;16;26060;13], [Store;;;;;59;Store: 59], [Store;department\'s;;;], [Store;department\'s;Deptartment;;;335;Department: 335], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;61664713;40118;1;17990], [Store;department\'s;Deptartment;product\'s;Product;61664713;40118;-1;-17990], [Store;department\'s;Deptartment;product\'s;Product;61684613;40118;1;12990], [Store;department\'s;Deptartment;summary;;1;12990;3], [Store;department\'s;Deptartment;;;410;Department: 410], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;68634752;40118;1;8990], [Store;department\'s;Deptartment;summary;;1;8990;1], [Store;department\'s;Deptartment;;;620;Department: 620], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;60664659;40118;1;3990], [Store;department\'s;Deptartment;product\'s;Product;60694698;40118;1;3990], [Store;department\'s;Deptartment;summary;;2;7980;2], [Store;department\'s;Deptartment;;;878;Department: 878], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;60614487;40118;1;5950], [Store;department\'s;Deptartment;product\'s;Product;63644339;40118;1;12650], [Store;department\'s;Deptartment;summary;;2;18600;2], [Store;department\'s;Deptartment;;;929;Department: 929], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;67674686;40118;1;3990], [Store;department\'s;Deptartment;summary;;1;3990;1], [Store;department\'s;Deptartment;;;957;Department: 957], [Store;department\'s;Deptartment;product\'s;], [Store;department\'s;Deptartment;product\'s;Product;62684217;40118;1;9990], [Store;department\'s;Deptartment;product\'s;Product;64614401;40118;1;1990], [Store;department\'s;Deptartment;product\'s;Product;64614401;40118;1;1990], [Store;department\'s;Deptartment;product\'s;Product;64624770;40118;1;2590], [Store;department\'s;Deptartment;summary;;4;16560;4], [Store;order\'s;;;], [Store;order\'s;Order;;;61684613;1], [Store;order\'s;Order;;;68634752;1], [Store;order\'s;Order;;;60664659;1], [Store;order\'s;Order;;;60694698;1], [Store;order\'s;Order;;;60614487;1], [Store;order\'s;Order;;;63644339;1], [Store;order\'s;Order;;;67674686;1], [Store;order\'s;Order;;;62684217;1], [Store;order\'s;Order;;;64614401;2], [Store;order\'s;Order;;;64624770;1], [Store;summary;;;;11;69110;13]]')
##		assert_p('Table', 'Content', '[[Store;;;;;20;Store: 20], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;summary;;;;;;], [Store;;;;;59;Store: 59], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;department\'s;Deptartment;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;product\'s;Product;;;;], [Store;department\'s;Deptartment;summary;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;order\'s;Order;;;;], [Store;summary;;;;;;]]')

		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
