/*
 * Purpose: Record orientated reading of Text files
 *
 * @Author Bruce Martin
 * Created on 27/08/2005
 *
 * # Version 0.60 Bruce Martin 2007/02/16
 *   - Started work on seperating Record section out, so removing
 *     all reference to the Common module and used a new Constants
 *     module
 */
package net.sf.JRecord.IO;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.FieldDetail;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Details.AbstractLine;
import net.sf.JRecord.Details.AbstractRecordDetail;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.LineProvider;
import net.sf.JRecord.Details.RecordDetail;
import net.sf.JRecord.Types.Type;


/**
 * This class reads "Line's" from a text file
 *
 * @author Bruce Martin
 *
 */
public class TextLineReader extends StandardLineReader {

    private InputStream inStream;
	private InputStreamReader stdReader;
	private BufferedReader reader = null;
	private boolean namesInFile = false;
	
    private String defaultDelim  = ","; 
    private String defaultQuote  = "'";



	/**
	 * This class provides record oriented reading of a Text files
	 */
	public TextLineReader() {
	    super();
	}


	/**
	 * This class provides record oriented reading of a Text files
	 * using a user supplied Line Provider.
	 * <p><b>Note:</b> A line provider creates lines. This allows
	 * you to use your own Line's
	 *
	 * @param provider line provider
	 */
	public TextLineReader(final LineProvider provider) {
	    super(provider);
	}

	/**
	 *  This class provides record oriented reading of a Text files
	 * using a user supplied Line Provider.
	 * <p><b>Note:</> A line provider creates lines. This allows
	 * you to use your own Line's
	 *
	 * @param provider line provider used to create lines
	 * @param namesOn1stLine wether names are stored on the first line of
	 *        a file
	 */
	public TextLineReader(final LineProvider provider,
	        			  final boolean namesOn1stLine) {
	    super(provider);

	    namesInFile = namesOn1stLine;
	}


    /**
     * @see net.sf.JRecord.IO.StandardLineReader#open(java.io.InputStream, net.sf.JRecord.Details.LayoutDetail)
     */
    public void open(InputStream inputStream, LayoutDetail layout)
    throws IOException, RecordException {
    	String font = "";
        inStream = inputStream;
        setLayout(layout);

		if (layout == null || "".equals(layout.getFontName())) {
		    stdReader = new InputStreamReader(inputStream);
		} else {
		    try {
		    	font = layout.getFontName();
		        stdReader = new InputStreamReader(inputStream, font);
		    } catch (Exception e) {
 		        stdReader = new InputStreamReader(inputStream);
		    }
		}

		reader = new BufferedReader(stdReader);

		if (namesInFile) {
		    createLayout(reader, inputStream, font);
		}
    }


    /**
     * create a layout
     *
     * @param pReader file read
     *
     * @throws IOException sny IO error that occurs
     */
    protected void createLayout(BufferedReader pReader, InputStream inputStream, String font) throws IOException, RecordException {
        LayoutDetail layout;
	    
        RecordDetail rec = null;
	    int fieldType = Type.ftChar;
        int decimal   = 0;
        int format    = 0;
        String param  = "";
        String delim  = defaultDelim; 
        String quote  = defaultQuote;

        byte[] recordSep = Constants.SYSTEM_EOL_BYTES;

	    try {
	    	delim     = getLayout().getDelimiter();
	        rec = getLayout().getRecord(0);
	        fieldType = rec.getField(0).getType();
	        decimal   = rec.getField(0).getDecimal();
	        format    = rec.getField(0).getFormat();
	        param     = rec.getField(0).getParamater();
	        quote     = rec.getQuote();
	        recordSep = getLayout().getRecordSep();
	        font      = getLayout().getFontName();
	    } catch (Exception e) {
        }
	    
	    //System.out.println(" Quote  ->" + quote + " " + (getLayout() == null));

	    layout = createLayout(pReader.readLine(), rec, 
	    		recordSep, font,  delim,
                quote, 0, fieldType, decimal, format, param);
	    //System.out.println(" Quote  ->");

	    if (layout != null) {
	        setLayout(layout);
	    }
    }

    /**
     * create a Layout from the first line in the file
     * @param line line being built
     * @param recordSep record seperator
     * @param fontName font name
     * @param delimiter field delitier
     * @param quote Quote Character to use
     * @param parser Identifier of the CSV parser to use
     * @param fieldType field type
     * @param decimal number of decimal places
     * @param format format to use
     * @param param param to add to each field
     * @throws IOException any error
     */
    public static LayoutDetail createLayout(String line, AbstractRecordDetail rec,
    		byte[] recordSep,
            String fontName, String delimiter, String quote, int parser,
            int fieldType, int decimal, int format, String param) throws IOException {

    	int fldType, idx;
        int i = 0;
        LayoutDetail ret = null;
        String s;

        if (line != null) {
            //RecordDetail rec = getLayout().getRecord(0);
            StringTokenizer tok = new StringTokenizer(
                    line, delimiter, false);
            //String fontName = fontname;
            int len = tok.countTokens();
            FieldDetail[] flds = new FieldDetail[len];
            RecordDetail[] recs = new RecordDetail[1];

            if (fieldType < 0) {
                fieldType = Type.ftChar;
            }

            while (tok.hasMoreElements()) {
                s = tok.nextToken();
                fldType = fieldType;
                if (rec != null 
                && (idx = rec.getFieldIndex(s)) >= 0) {
                	fldType = rec.getField(idx).getType();
                }
                flds[i] = new FieldDetail(s, s, fldType, decimal,
                        fontName, format, param);
                flds[i].setPosOnly(i + 1);
                i += 1;
            }

            recs[0] = new RecordDetail("", "", "", Constants.rtDelimited,
                    delimiter, quote, fontName, flds, 0);

            try {
                ret =
                    new LayoutDetail("", recs, "",
                        Constants.rtDelimited,
                        recordSep, "", fontName, null,
                        Constants.IO_NAME_1ST_LINE
                    );
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return ret;
    }


    /**
     * @see net.sf.JRecord.IO.StandardLineReader#read()
     */
    public AbstractLine read()  throws IOException {
        AbstractLine ret = null;

        if (reader == null) {
            throw new IOException(StandardLineReader.NOT_OPEN_MESSAGE);
        }
        String s = reader.readLine();

        if (s != null) {
            ret = getLine(s);
        }

        return ret;
    }


    /**
     * @see net.sf.JRecord.IO.StandardLineReader#close()
     */
    public void close() throws IOException {

        if (reader != null) {
            reader.close();
    		stdReader.close();
    		inStream.close();
        }

    	reader    = null;
    	stdReader = null;
    	inStream  = null;
    }


    /**
     * set default delimiter
     * @param theDefaultDelim new default field delimeter
     */
	public void setDefaultDelim(String theDefaultDelim) {
		this.defaultDelim = theDefaultDelim;
	}


	public void setDefaultQuote(String theDefaultQuote) {
		this.defaultQuote = theDefaultQuote;
	}


	/**
	 * @return the defaultDelim
	 */
	public String getDefaultDelim() {
		return defaultDelim;
	}


	/**
	 * @return the defaultQuote
	 */
	public String getDefaultQuote() {
		return defaultQuote;
	}

}
