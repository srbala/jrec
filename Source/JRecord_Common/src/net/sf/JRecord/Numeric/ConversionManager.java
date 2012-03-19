/*
 * @Author Bruce Martin
 * Created on 2/04/2007
 *
 * Purpose:
 * Store all Cobol Numeric Type Converters. A converter
 * should convert a cobol numeric type (as defined in the copybook)
 * into a JRecord Type identifier
 */
package net.sf.JRecord.Numeric;

import java.util.ArrayList;
import java.util.HashMap;

import net.sf.JRecord.Common.AbstractManager;
import net.sf.JRecord.Types.Type;

/**
 * This class will store all Cobol Numeric Type Converters. A converter
 * should convert a cobol numeric type (as defined in the copybook)
 * into a JRecord Type identifier
 *
 * @author Bruce Martin
 *
 */
public class ConversionManager implements AbstractManager {

	private static final int[] MAINFRAME_BIN_SIZES = {2, 4, 8};
	private static final int[] BIN_SIZES_1248 = {1, 2, 4, 8};
 //   public static final int[] BIN_SIZES_12348 = {1, 2, 3, 4, 8};
	private static final int[] BIN_SIZES_1_TO_8 = {1, 2, 3 ,4 ,5 ,6 ,7 , 8};
	private static final int[] NO_SYNC = {1, 1, 1, 1};
	private static int[] MAINFRAME_SYNC = {2, 2, 4, 4};
	private static final int[] FS2000_SYNC = {2, 2, 4, 8};
	
//	private static final int[] STANDARD_FLOAT_SYNC = {1, 1, 4, 8};

    private static ConversionManager instance = null;
    private ArrayList<Convert> conversions = new ArrayList<Convert>();
    private HashMap<Integer, Convert> conversionsMap = new HashMap<Integer, Convert>(30);

    public ConversionManager() {
        super();

        registerConverter(new BasicConvert(Convert.FMT_INTEL, "Intel", Convert.FMT_INTEL, MAINFRAME_BIN_SIZES, false));
        registerConverter(new BasicConvert(Convert.FMT_MAINFRAME, "Mainframe", Convert.FMT_MAINFRAME, MAINFRAME_BIN_SIZES, 
        		MAINFRAME_SYNC, false, 4, 4));
        registerConverter(new OpenCobol(Convert.FMT_FUJITSU, "Fujitsu", MAINFRAME_BIN_SIZES, MAINFRAME_SYNC, 4, 8));
        registerConverter(new BasicConvert(Convert.FMT_BIG_ENDIAN, "Big-Endian (Old)", Convert.FMT_BIG_ENDIAN, MAINFRAME_BIN_SIZES, false));
        
        registerConverter(new OpenCobol(Convert.FMT_OPEN_COBOL, "Open Cobol Little Endian (Intel)", BIN_SIZES_1248, BIN_SIZES_1248));
        registerConverter(new OpenCobol(Convert.FMT_FS2000, "Open Cobol bs2000 Little Endian (Intel)",  MAINFRAME_BIN_SIZES, FS2000_SYNC));
        registerConverter(new OpenCobol(Convert.FMT_OPEN_COBOL_MVS, "Open Cobol MVS Little Endian (Intel)",  MAINFRAME_BIN_SIZES, FS2000_SYNC));
        registerConverter(new OpenCobol(Convert.FMT_OC_MICRO_FOCUS, "Open Cobol Micro Focus (Intel)",  BIN_SIZES_1_TO_8, NO_SYNC, 1 , 1));
        
        registerConverter(new OpenCobolBE(Convert.FMT_OPEN_COBOL_BE, "Open Cobol Big Endian", BIN_SIZES_1248, BIN_SIZES_1248));
        registerConverter(new OpenCobolBE(Convert.FMT_FS2000_BE, "Open Cobol bs2000 Big Endian",  MAINFRAME_BIN_SIZES, FS2000_SYNC));
        registerConverter(new OpenCobolBE(Convert.FMT_OPEN_COBOL_MVS_BE, "Open Cobol MVS Big Endian",  MAINFRAME_BIN_SIZES, FS2000_SYNC));
        registerConverter(new OpenCobolBE(Convert.FMT_OC_MICRO_FOCUS_BE, "Open Cobol Micro Focus Big E",  BIN_SIZES_1_TO_8, NO_SYNC, 1 , 1));
        //registerConverter(new MicroFocusCobol());
     
        LoadConversion loader = new LoadConversion();
        Convert conv;
        
        for (int i = 0; i < 32; i++) {
        	if ((conv = loader.getConversion(i)) != null) {
        		System.out.println("Registering " + conv.getIdentifier() + " " + conv.getName());
        		registerConverter(conv);
        	}
        	
        }

//        idx = Convert.FMT_MICRO_FOCUS + 1;
//        
//         registerConverter(new BasicConvert(idx++, "Big-Endian 2:4:8 use Positive Int", Convert.FMT_BIG_ENDIAN, MAINFRAME_BIN_SIZES, true));
//              
//        registerConverter(new BasicConvert(idx++, "Little Endian (2:4:8) use Positive Int", Convert.FMT_INTEL, MAINFRAME_BIN_SIZES, true));
//        registerConverter(new BasicConvert(idx++, "Little Endian (1:2:4:8) use Positive Int", Convert.FMT_INTEL, BIN_SIZES_1248, true));
//        registerConverter(new BasicConvert(idx++, "Little Endian (1-8) use Positive Int", Convert.FMT_INTEL, BIN_SIZES_1_TO_8, true));
   }
    /**
     * Get the Number of conversions
     * @return Count of the number of conversions
     */
    public int getNumberOfEntries() {
        return conversions.size();
    }

    /**
     * Get a specific conversion
     * @param index index to be retrieved
     * @return requested Conversion
     */
    public Convert getConverter4code(int index) {
        return conversionsMap.get(index);
    }

    /**
     * Get a specific conversion
     * @param index index to be retrieved
     * @return requested Conversion
     */
    public Convert getConverter(int index) {
        return conversions.get(index);
    }

    /**
     * Register a Converter
     * @param converter converter
     */
    public void registerConverter(Convert converter) {
        conversions.add(converter);
        conversionsMap.put(converter.getIdentifier(), converter);
    }

    
    /**
	 * @see net.sf.JRecord.Common.AbstractManager#getKey(int)
	 */
	@Override
	public int getKey(int idx) {
		return conversions.get(idx).getIdentifier();
	}
	
	/**
	 * @see net.sf.JRecord.Common.AbstractManager#getName(int)
	 */
	@Override
	public String getName(int idx) {
		return conversions.get(idx).getName();
	}
	
	/**
     * Get the manager
     * @return Conversion Manager
     */
    public static ConversionManager getInstance() {
    	if (instance == null) {
    		instance = new ConversionManager();
    	}
        return instance;
    }
    
    private static class OpenCobol extends BasicConvert {
    	public OpenCobol(int id, String name,  int[] binarySizes, int[] syncAt) {
    		super(id,  name, Convert.FMT_BIG_ENDIAN, binarySizes, syncAt, true, 4, 8);
    	}
 
    	public OpenCobol(int id, String name,  int[] binarySizes, int[] syncAt, int floatSync, int doubleSync) {
    		super(id,  name, Convert.FMT_BIG_ENDIAN, binarySizes, syncAt, true, floatSync, doubleSync);
    	}

    	public int getTypeIdentifier(String usage, String picture, boolean signed) {
    		int iType;
    		if ( "computational-5".equals(usage)) {
    			iType = Type.ftBinaryInt;
    			if (super.isPositiveIntAvailable() && ! signed) {
    				iType = Type.ftPostiveBinaryInt;
    			}
    		} else {
    			iType = super.getTypeIdentifier(usage, picture, signed) ;
    		}
    		return iType;
    	}
    }
    
    private static class OpenCobolBE extends BasicConvert {
    	public OpenCobolBE(int id, String name,  int[] binarySizes, int[] syncAt) {
    		super(id,  name, Convert.FMT_BIG_ENDIAN, binarySizes, syncAt, true, 4, 8);
    	}
 
    	public OpenCobolBE(int id, String name,  int[] binarySizes, int[] syncAt, int floatSync, int doubleSync) {
    		super(id,  name, Convert.FMT_BIG_ENDIAN, binarySizes, syncAt, true, floatSync, doubleSync);
    	}
    }
}