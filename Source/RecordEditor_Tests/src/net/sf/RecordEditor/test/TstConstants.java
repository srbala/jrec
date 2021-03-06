/*
 * @Author Bruce Martin
 * Created on 11/11/2005
 *
 * Purpose:
 */
package net.sf.RecordEditor.test;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Random;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.JRecord.Details.AbstractLine;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.External.ExternalRecord;
import net.sf.JRecord.External.RecordEditorXmlLoader;
import net.sf.JRecord.IO.AbstractLineReader;
import net.sf.JRecord.IO.LineIOProvider;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.utils.fileStorage.DataStoreLarge;
import net.sf.RecordEditor.utils.fileStorage.DataStoreLargeView;
import net.sf.RecordEditor.utils.fileStorage.DataStoreStd;
import net.sf.RecordEditor.utils.fileStorage.FileDetails;
import net.sf.RecordEditor.utils.fileStorage.IDataStore;

/**
 * Constants for testing
 *
 * @author Bruce Martin
 *
 */
public final class TstConstants {

 //   public static final String TEMP_DIRECTORY = "/home/bm/Programs/RecordEdit/Test/";
	public static final int DS_NORMAL = 1;
	public static final int DS_FIXED  = 2;
	public static final int DS_VB     = 3;
	public static final int DS_CHAR   = 4;
	public static final int DS_LARGE_VIEW_NORMAL = 5;
	public static final int DS_LARGE_VIEW_CHAR   = 6;
	public static final int DS_LARGE_VIEW_VB     = 7;
	
	public static final int SIZE_SMALL   = 6;
	public static final int SIZE_LARGE   = 7;
	
    public static final String TEMP_DIRECTORY = "G:\\Temp\\RecordEditorTest\\";
    public static final int    DB_INDEX       = 0;

    public static final String TAB_CSV_LAYOUT =
			  "<?xml version=\"1.0\" ?>"
			+ "<RECORD RECORDNAME=\"Tab Delimited, names on the first line\" COPYBOOK=\"\" DELIMITER=\"&lt;Tab&gt;\" DESCRIPTION=\"Tab Delimited, names on the first line\" FILESTRUCTURE=\"CSV_NAME_1ST_LINE\" STYLE=\"0\" RECORDTYPE=\"Delimited\" LIST=\"Y\" QUOTE=\"\" RecSep=\"default\">"
			+ "	<FIELDS>"
			+ "		<FIELD NAME=\"Dummy\" DESCRIPTION=\"1 field is Required for the layout to load\" POSITION=\"1\" TYPE=\"Char\"/>"
			+ "	</FIELDS>"
			+ "</RECORD>";


    public static final String TAB_CSV_LAYOUT_NUM =
			  "<?xml version=\"1.0\" ?>"
			+ "<RECORD RECORDNAME=\"Tab Delimited, names on the first line\" COPYBOOK=\"\" DELIMITER=\"&lt;Tab&gt;\" DESCRIPTION=\"Tab Delimited, names on the first line\" FILESTRUCTURE=\"CSV_NAME_1ST_LINE\" STYLE=\"0\" RECORDTYPE=\"Delimited\" LIST=\"Y\" QUOTE=\"\" RecSep=\"default\">"
			+ "	<FIELDS>"
			+ "		<FIELD NAME=\"Dummy\" DESCRIPTION=\"1 field is Required for the layout to load\" POSITION=\"1\" TYPE=\"Num (Left Justified)\"/>"
			+ "	</FIELDS>"
			+ "</RECORD>";


    public static final String AMS_PO_LAYOUT
    		=	"<?xml version=\"1.0\" ?>"
    		+	"<RECORD RECORDNAME=\"ams PO Download\" COPYBOOK=\"\" DELIMITER=\"&lt;Tab&gt;\" FILESTRUCTURE=\"Default\" STYLE=\"0\" "
    		+	"        RECORDTYPE=\"GroupOfRecords\" LIST=\"Y\" QUOTE=\"\" RecSep=\"default\">"
    		+	"	<RECORDS>"
    		+	"		<RECORD RECORDNAME=\"ams PO Download: Detail\" COPYBOOK=\"\" DELIMITER=\"&lt;Tab&gt;\" "
    		+	"		        DESCRIPTION=\"PO Download: Detail\" FILESTRUCTURE=\"Default\" STYLE=\"0\" ECORDTYPE=\"RecordLayout\""
    		+	"			LIST=\"N\" QUOTE=\"\" RecSep=\"default\" TESTFIELD=\"Record Type\" TESTVALUE=\"D1\">"
    		+	"			<FIELDS>"
    		+	"				<FIELD NAME=\"Record Type\"  POSITION=\"1\" LENGTH=\"2\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Pack Qty\"     POSITION=\"3\" LENGTH=\"9\" DECIMAL=\"4\" TYPE=\"Num Assumed Decimal (Zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Cost\"    POSITION=\"12\" LENGTH=\"13\" DECIMAL=\"4\" TYPE=\"Num Assumed Decimal (Zero padded)\"/>"
    		+	"				<FIELD NAME=\"APN\"          POSITION=\"25\" LENGTH=\"13\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Filler\"       POSITION=\"38\" LENGTH=\"1\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Product\"      POSITION=\"39\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"pmg dtl tech key\" POSITION=\"72\" LENGTH=\"15\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Case Pack id\" POSITION=\"87\" LENGTH=\"15\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Product Name\" POSITION=\"101\" LENGTH=\"50\" TYPE=\"Char\"/>"
    		+	"			</FIELDS>"
    		+	"		</RECORD>"
    		+	"		<RECORD RECORDNAME=\"ams PO Download: Header\" COPYBOOK=\"\" DELIMITER=\"&lt;Tab&gt;\" "
    		+	"		        DESCRIPTION=\"PO Download: Header\" FILESTRUCTURE=\"Default\" STYLE=\"0\" RECORDTYPE=\"RecordLayout\" LIST=\"N\" "
    		+	"			QUOTE=\"\" RecSep=\"default\" TESTFIELD=\"Record Type\" TESTVALUE=\"H1\">"
    		+	"			<FIELDS>"
    		+	"				<FIELD NAME=\"Record Type\"     POSITION=\"1\" LENGTH=\"2\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Sequence Number\" POSITION=\"3\" LENGTH=\"5\" DECIMAL=\"3\" TYPE=\"Num Assumed Decimal (Zero padded)\"/>"
    		+	"				<FIELD NAME=\"Vendor\"          POSITION=\"8\" LENGTH=\"10\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"PO\"              POSITION=\"18\" LENGTH=\"12\" TYPE=\"Num Assumed Decimal (Zero padded)\"/>"
    		+	"				<FIELD NAME=\"Entry Date\" DESCRIPTION=\"Format YYMMDD\" POSITION=\"30\" LENGTH=\"6\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Filler\"          POSITION=\"36\" LENGTH=\"8\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"beg01 code\"      POSITION=\"44\" LENGTH=\"2\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"beg02 code\"      POSITION=\"46\" LENGTH=\"2\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Department\"      POSITION=\"48\" LENGTH=\"4\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Expected Reciept Date\" DESCRIPTION=\"Format YYMMDD\" POSITION=\"52\" LENGTH=\"6\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Cancel by date\" DESCRIPTION=\"Format YYMMDD\" POSITION=\"58\" LENGTH=\"6\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"EDI Type\"       POSITION=\"68\" LENGTH=\"1\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Add Date\" DESCRIPTION=\"Format YYMMDD\" POSITION=\"69\" LENGTH=\"6\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Filler\"         POSITION=\"75\" LENGTH=\"1\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Department Name\" POSITION=\"76\" LENGTH=\"10\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Prcoess Type\" DESCRIPTION=\"C/N Conveyable/Non-Conveyable\" POSITION=\"86\" LENGTH=\"1\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Order Type\" POSITION=\"87\" LENGTH=\"2\" TYPE=\"Char\"/>"
    		+	"			</FIELDS>"
    		+	"		</RECORD>"
    		+	"		<RECORD RECORDNAME=\"ams PO Download: Allocation\" COPYBOOK=\"\" DELIMITER=\"&lt;Tab&gt;\" DESCRIPTION=\"Allocation Line\" "
    		+	"		        FILESTRUCTURE=\"Default\" STYLE=\"0\" RECORDTYPE=\"RecordLayout\" LIST=\"N\" QUOTE=\"\" RecSep=\"default\" "
    		+	"			TESTFIELD=\"Record Type\" TESTVALUE=\"S1\">"
    		+	"			<FIELDS>"
    		+	"				<FIELD NAME=\"Record Type\" POSITION=\"1\" LENGTH=\"2\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"DC Number 1\" POSITION=\"3\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 1\" POSITION=\"7\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 2\" POSITION=\"15\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 2\" POSITION=\"19\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 4\" POSITION=\"39\" LENGTH=\"4\" TYPE=\"Char\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 4\" POSITION=\"43\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 5\" POSITION=\"51\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 5\" POSITION=\"55\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 6\" POSITION=\"63\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 6\" POSITION=\"67\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 7\" POSITION=\"75\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 7\" POSITION=\"79\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 8\" POSITION=\"87\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 8\" POSITION=\"91\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 9\" POSITION=\"99\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 9\" POSITION=\"103\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"DC Number 10\" POSITION=\"111\" LENGTH=\"4\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"				<FIELD NAME=\"Pack Quantity 10\" POSITION=\"115\" LENGTH=\"8\" TYPE=\"Num (Right Justified zero padded)\"/>"
    		+	"			</FIELDS>"
    		+	"		</RECORD>"
    		+	"	</RECORDS>"
    		+	"</RECORD>";

    public final String[] AMS_PO_LINES = {
    		"H1453490000006060286225      040909        00  200 0501020501075965        LADIES KNICFT",
    		"D100007000000000000000022222500000000 43314531000000054540000007       2075359        45614531       DONKEY 24-006607 SHWL WRAP CARD                   ",
    		"S1504300000001504500000001506500000001507600000001507900000001515100000001507200000001    00000000    00000000    00000000",
    		"D100004000000000014832000000000000000 05614944000000054540000004       2075360        5614944        MILK 24-006607 SHWL WRAP CARD                     ",
    		"S1504500000001507600000001507900000001333149440001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100048000000000014832000000000000000 55615071000000054540000048       2075361        55615071       M.ROSE 24-006607 SHWL WRAP CARD                   ",
    		"S1503600000003504300000005504500000005333150710003506500000004506900000004507600000004507900000002509400000004512800000003",
    		"S1515100000004518000000003507200000002517300000002    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100004000000000014832000000000000000 55615156000000054540000004       2075362        55615156       AQUA 24-006607 SHWL WRAP CARD                     ",
    		"S1504300000001504500000001506500000001333151560001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"H1453500000006228000000222227040909        00  200 0501020501075966        LADIES KNICFT",
    		"D100016000000622814832000000000002222 02224531000000054540000016       2075348        5614531        DONKEY 24-006607 SHWL WRAP CARD                   ",
    		"S150190000000150370000000150740000000150780000000150850000000150910000000150930000000150950000000151 DONKEY 24-006607 SHWL WRAP CARD                  ",
    		"S1517100000001517700000001508900000001513600000001514500000001509600000001    00000000    00000000    00000000    00000000",
    		"D100008000000000014832000000000000000 62224944000000054540000008       2075349        65614944       MILK 24-006607 SHWL WRAP CARD                     ",
    		"S1501900000001503700000001507800000001509100000001509300000001512900000001517700000001514500000001    00000000    00000000",
    		"D100108000000000014832000000000000000 62225071000000054540000108       2075350        65615071       M.ROSE 24-006607 SHWL WRAP CARD                   ",
    		"S1501500000002501900000005503300000002503500000002503700000004505200000002505500000002506000000002507000000002507400000004",
    		"S1507800000005508100000002508500000003509000000002509100000004509300000004509500000004512900000004514400000004516500000002",
    		"S1530300000002516900000002517000000002517100000003517700000004501600000002508900000004513600000003501100000002504600000002",
    		"S1514500000004509600000003515400000002516200000002516300000002516400000002519200000002515000000002517500000002    00000000",
    		"D100008000000000014832000000000000000 52225156000000054540000008       2075351        55615156       M.ROSE 24-006607 SHWL WRAP CARD                   ",
    		"S1501900000001503700000001507800000001509100000001509300000001512900000001517700000001514500000001    00000000    00000000",
    		"H1453510000006228000000222243040909        00  200 0501020501075968        LADIES KNICFT",
    		"D100006000000000014832000000000000000 45614531000000054540000006       2075352        45614531       DONKEY 24-006607 SHWL WRAP CARD                   ",
    		"S1500900000001502100000001502400000001502500000001502600000001512700000001    00000000    00000000    00000000    00000000",
    		"D100003000000000014832000000000000000 45614944000000054540000003       2075353        45614944       MILK 24-006607 SHWL WRAP CARD                     ",
    		"S1500900000001502100000001512700000001    00000000    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100044000000000014832000000000000000 45615071000000054540000044       2075354        45615071       M.ROSE 24-006607 SHWL WRAP CARD                   ",
    		"S1500900000005502100000005502400000004502500000004502600000004504700000003507700000002512700000005513400000004514200000002",
    		"S1504400000002507100000002515900000002    00000000    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100003000000000014832000000000000000 45615156000000054540000003       2075355        35615156       AQUA 24-006607 SHWL WRAP CARD                     ",
    		"S1500900000001502100000001512700000001    00000000    00000000    00000000    00000000    00000000    00000000    00000000",
    		"H1453520000005341294915      041013        00  475 0412310501075965P       WOMENS SHOCFT",
    		"D100030000000000029268000000000000000 45846680000000072720000030       2120736        45615156       CONCERTO BLACK LEATHER ANKLE BOOT                 ",
    		"S1503600000002504300000003504500000003505700000001506500000002506900000002507600000003507900000001509400000003512800000003",
    		"S1515100000003518000000002507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"H1453530000005341294987      041013        00  475 0412310501075965P       WOMENS SHOCFT",
    		"D100029000000000019836000000000000000 45846772000000054540000029       2121104        5846772        ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT      ",
    		"S1503600000002504300000003504500000003505700000001506500000002506900000002507600000003507900000001509400000002512800000003",
    		"S1515100000003518000000002507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100029000000000019836000000000000000 45847489000000054540000029       2121627        45847489       ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT      ",
    		"S1503600000002504300000003504500000003505700000001506500000002506900000002507600000002507900000001509400000003512800000003",
    		"S1515100000003518000000002507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"H1453540000005341295139      041013        00  475 0412310501075965P       WOMENS SHOCFT",
    		"D100025000000000046548000000000000000 45848707000000090900000025       2179843        45848707A      ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT      ",
    		"S1503600000002504300000002504500000002505700000001506500000002506900000002507600000002507900000001509400000002512800000002",
    		"S1515100000002518000000002507200000002517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"H1453550000005341303662      041110        00  310 0412310501075965P       YOUTH SHOECFT",
    		"D100008000000000008216000000000000000 46164790000000036360000008       2203070        46164790B8     ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT     E",
    		"S1504300000001504500000001506500000001506900000001507600000001509400000001512800000001515100000001    00000000    00000000",
    		"D100024000000000011297000000000000000 46164790000000036360000024       2203056        46164790       ANGEL PINK SYNTHETIC MICRO SUEDE SLOUCH BOOT     E",
    		"S1503600000001504300000002504500000002505700000001506500000002506900000002507600000002507900000001509400000002512800000002",
    		"S1515100000003518000000002507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100007000000000008216000000000000000 46165360000000036360000007       2203075        46165360B8     CABERETCARAMEL MICRO SUEDE PEEP TOE               ",
    		"S1504300000001504500000001506500000001506900000001507600000001512800000001515100000001    00000000    00000000    00000000",
    		"D100023000000000011297000000000000000 46165360000000036360000023       2203072        46165360       CABERETCARAMEL MICRO SUEDE PEEP TOE               ",
    		"S1503600000001504300000002504500000002505700000001506500000002506900000002507600000002507900000001509400000001512800000002",
    		"S1515100000003518000000002507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"H1453560000005341304100      041111        00  310 0412310501075965P       YOUTH SHOECFT",
    		"D100008000000000008384000000000000000 45928553000000036360000008       2203222        45928553B8     CABERETCARAMEL MICRO SUEDE PEEP TOE               ",
    		"S1504300000001504500000001506900000001507600000001509400000001512800000001515100000001518000000001    00000000    00000000",
    		"D100022000000000012576000000000000000 45928553000000036360000022       2203219        45928553       CABERETCARAMEL MICRO SUEDE PEEP TOE               ",
    		"S1503600000001504300000002504500000002505700000001506500000001506900000002507600000002507900000001509400000002512800000002",
    		"S1515100000002518000000002507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100022000000000012576000000000000000 15935759000000036360000022       2203223        05935759       JAZZ DUSTY PINK HEELED PEEP TOE                   ",
    		"S1503600000001504300000002504500000002505700000001506500000001506900000002507600000002507900000001509400000002512800000002",
    		"S1515100000003518000000001507200000001517300000001    00000000    00000000    00000000    00000000    00000000    00000000",
    		"D100007000000000008384000000000000000 45935759000000036360000007       2203224        45935759B8     JAZZ DUSTY PINK HEELED PEEP TOE                   ",
    		"S1504300000001504500000001506900000001507600000001509400000001512800000001515100000001    00000000    00000000    00000000",
    };

	public static final String[] CSV_SALES_LINES = {
			"KEYCODE-NO	STORE-NO	DATE	DEPT-NO	QTY-SOLD	SALE-PRICE",
			"63604808	20	40118	170	1	4.87",
			"69684558	20	40118	280	1	19.00",
			"69684558	20	40118	280	-1	-19.00",
			"69694158	20	40118	280	1	5.01",
			"62684671	20	-40118	685	1	69.99",
			"62684671	20	40118	685	-1	-69.99",
			"61664713	59	40118	335	1	17.99",
			"61664713	59	40118	335	-1	-17.99",
			"61684613	59	40118	335	1	12.99",
			"68634752	59	40118	410	1	8.99",
			"60694698	59	40118	620	1	3.99",
			"60664659	59	40118	620	1	3.99",
			"60614487	59	40118	878	1	5.95",
			"68654655	166	-40118	60	1	5.08",
			"69624033	166	40118	80	1	18.19",
			"60604100	166	40118	80	1	13.30",
			"68674560	166	40118	170	1	5.99",
	};



    public static FileView readFileView(AbstractLayoutDetails layout, String[] fileLines, int readerId)
    throws IOException, RecordException {
    	return readFileView(layout, fileLines, readerId, DS_NORMAL);
	};



    public static FileView readFileView(AbstractLayoutDetails layout, String[] fileLines, int readerId, int dsType)
    throws IOException, RecordException {

		AbstractLineReader r = LineIOProvider.getInstance().getLineReader(readerId);
//		ArrayList<AbstractLine> lines = new ArrayList<AbstractLine>();
		AbstractLine l;

		r.open(getFile(fileLines), layout);
		l = r.read();
				
		layout = r.getLayout();
		LayoutDetail schema = (LayoutDetail) layout;
		IDataStore<AbstractLine> ds, dsb;
		FileView fvb;
		switch (dsType) {
		case DS_FIXED:	
			ds = load(r, l, new DataStoreLarge(schema, FileDetails.FIXED_LENGTH, layout.getMaximumRecordLength()));
			break;
		case DS_VB:		
			ds = load(r, l, new DataStoreLarge(schema, FileDetails.VARIABLE_LENGTH, layout.getMaximumRecordLength()));	
			break;
		case DS_CHAR:	
			ds = load(r, l, new DataStoreLarge(schema, FileDetails.CHAR_LINE, layout.getMaximumRecordLength()));		
			break;
		case DS_LARGE_VIEW_NORMAL:	
			dsb = load(r, l, DataStoreStd.newStore(layout));
			fvb = new FileView("", dsb, layout);
			
			return new FileView((new DataStoreLargeView(dsb)).addRange(0, dsb.size() - 1), fvb, null);
		case DS_LARGE_VIEW_CHAR:	
			dsb = load(r, l, new DataStoreLarge(schema, FileDetails.CHAR_LINE, layout.getMaximumRecordLength()));
			fvb = new FileView("", dsb, layout);
			
			return new FileView((new DataStoreLargeView(dsb)).addRange(0, dsb.size() - 1), fvb, null);
		case DS_LARGE_VIEW_VB:	
			dsb = load(r, l, new DataStoreLarge(schema, FileDetails.VARIABLE_LENGTH, layout.getMaximumRecordLength()));
			fvb = new FileView("", dsb, layout);
			
			return new FileView((new DataStoreLargeView(dsb)).addRange(0, dsb.size() - 1), fvb, null);
		case DS_NORMAL:	
		default:
			ds = load(r, l, DataStoreStd.newStore(layout));
		}

		return new FileView("", ds, layout);
    }

    
    private static IDataStore<AbstractLine> load(AbstractLineReader r, AbstractLine l, IDataStore<AbstractLine> ds) throws IOException {
		if (l != null) {
			ds.add(l);
			while ((l = r.read()) != null) {
				ds.add(l);
			}
		}
   	
    	return ds;
    }


	public static InputStream getFile(String[] lines) {
		StringBuilder b = new StringBuilder();

		for (String l : lines) {
			b.append(l).append("\n");
		}

		return new ByteArrayInputStream(b.toString().getBytes());
	}
	
	public static int[] getRandomIncreasingArray(int arraySize, int minLength, int maxLength) {
		int[] ret = new int[arraySize];
		Random r = new Random(21);
		int last = 0;
		int maxJump = maxLength - minLength;
		
		ret[0] = 0;
		for (int i = 1; i < arraySize; i++) {
			last += minLength + (r.nextInt(last + 1)) % maxJump;
			ret[i] = last;
		}
		
		return ret;
	}
	
	public static String[] getLargeCsvLines() {
		String[] ret = new String[CSV_SALES_LINES.length * 20];
		int p = 0;
		for (int i = 0; i < 20; i++) {
			for (int j = 0; j < CSV_SALES_LINES.length;j++) {
				ret[p++] = CSV_SALES_LINES[j];
			}
		}
		return ret;
	}

	public static FileView getSalesCsvFile(int dsType) throws Exception {
		return getSalesCsvFile(dsType, SIZE_SMALL);
	}

	public static FileView getSalesCsvFile(int dsType, int sizeId) throws Exception {
		String[] d = TstConstants.CSV_SALES_LINES;
		if (sizeId == SIZE_LARGE) {
			d = getLargeCsvLines();
		}
		
		return readFileView(getTabCsvLayout(), d, Constants.IO_NAME_1ST_LINE, dsType);
	}

	public static FileView getSalesCsvFile() throws Exception {
		return readFileView(getTabCsvLayout(), TstConstants.CSV_SALES_LINES, Constants.IO_NAME_1ST_LINE, DS_NORMAL);
	}

	public static LayoutDetail getTabCsvLayout() throws Exception {
		return getExternalLayout(TstConstants.TAB_CSV_LAYOUT).asLayoutDetail();
	}


	private static ExternalRecord getExternalLayout(String strLayout) throws Exception {
		return RecordEditorXmlLoader.getExternalRecord(strLayout, "Csv Layout");
	}

  
	
}
