package net.sf.JRecord.zTest.Common;

import java.io.ByteArrayInputStream;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.Conversion;
import net.sf.JRecord.Common.TranslateXmlChars;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.External.ExternalRecord;
import net.sf.JRecord.External.RecordEditorXmlLoader;



public class TestCommonCode {


	public static ByteArrayInputStream arrayToStream(String[] array) {
		return arrayToStream(array, "\n", "");
	}


	public static ByteArrayInputStream arrayToStream(String[] array, String eol) {
		return arrayToStream(array, eol, "");
	}


	public static ByteArrayInputStream arrayToStream(String[] array, String eol, String charset) {
		return stringToStream(arrayToString(array, eol), charset);
	}

	public static String arrayToString(String[] array, String eol) {

		StringBuilder b = new StringBuilder();

		for (int i = 0; i < array.length; i++) {
			b.append(array[i]).append(eol);
		}

		return b.toString();
	}

	public static ByteArrayInputStream stringToStream(String s) {
//		System.out.println();
//		System.out.println(s);
//		System.out.println();
		return new ByteArrayInputStream(s.getBytes());
	}


	public static ByteArrayInputStream stringToStream(String s, String charset) {
		return new ByteArrayInputStream(Conversion.getBytes(s, charset));
	}

	public static final LayoutDetail getCsvLayout(int fileStructure, String font, String delim, String quote,
			boolean embeddedCr, int style)
	throws Exception {
		return getCsvExternal(fileStructure + "", font, delim, quote, embeddedCr, style).asLayoutDetail();
	}

	public static final LayoutDetail getCsvLayout(String fileStructure, String font, String delim, String quote,
			boolean embeddedCr, int style)
	throws Exception {
		return getCsvExternal(fileStructure, font, delim, quote, embeddedCr, style).asLayoutDetail();
	}

	public static final ExternalRecord getCsvExternal(String fileStructure, String font, String delim, String quote,
			boolean embeddedCr, int style)
	throws Exception {
		String xml;
		String embeddedStr = "";
		String fontStr = "";

		if ( "<none>".equals(quote.toLowerCase())) {
			quote = "";
		}
		if (embeddedCr) {
			embeddedStr = " " + Constants.RE_XML_EMBEDDED_CR + "=\"Y\" ";
		}

		if (font != null && ! "".equals(font)) {
			fontStr = " FONTNAME=\"" + font + "\" ";
		}

		xml = "<RECORD RECORDNAME=\"Delimited\" COPYBOOK=\"\" STYLE=\"" + style + "\""
			+ "        FILESTRUCTURE=\"" + fileStructure + "\""
			+ "        DELIMITER=\"" + TranslateXmlChars.replaceXmlCharsStr(delim) + "\""
			+ "        QUOTE=\"" + TranslateXmlChars.replaceXmlCharsStr(quote) + "\""
			+          embeddedStr + fontStr
			+ "		   DESCRIPTION=\"Delimited\" RECORDTYPE=\"Delimited\" RecSep=\"default\">"
			+ "	<FIELDS>"
			+ "		<FIELD NAME=\"Dummy\" DESCRIPTION=\" \" POSITION=\"1\" TYPE=\"Char\"/>"
			+ "	</FIELDS>"
			+ "</RECORD>";

		System.out.println("Generated Xml: " +xml);

		return RecordEditorXmlLoader.getExternalRecord(xml, "CsvNamesFirstLine");
	}



}
