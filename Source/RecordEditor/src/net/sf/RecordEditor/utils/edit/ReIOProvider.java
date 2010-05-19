package net.sf.RecordEditor.utils.edit;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Details.LineProvider;
import net.sf.JRecord.IO.AbstractLineReader;
import net.sf.JRecord.IO.LineIOProvider;
import net.sf.JRecord.IO.StandardLineIOProvider;

public class ReIOProvider extends StandardLineIOProvider {

	private static ReIOProvider instance = null;
	
    private static final int numberOfEntries = 2;
    private static String[] names = new String [numberOfEntries] ;
    private static String[] externalNames = new String [numberOfEntries] ;
    private static int[] keys = new int[numberOfEntries];
    
 	
    static {
			int i = 0;
		 
			keys[i] = Constants.IO_UNKOWN_FORMAT;				externalNames[i] = "UNKNOWN_FORMAT";			names[i++] = "Unknow Format (Choose details at run time)";	
			keys[i] = Constants.IO_GENERIC_CSV;				externalNames[i] = "CSV_GENERIC";			names[i++] = "Generic CSV (Choose details at run time)";	
	 }

	@Override
	public AbstractLineReader getLineReader(int fileStructure,
			LineProvider lineProvider) {
	
		//System.out.println(" ~~ ReIOProvider ~ " + fileStructure + " --> " + Constants.IO_GENERIC_CSV);
        if (fileStructure == Constants.IO_GENERIC_CSV
        ||  fileStructure == Constants.IO_UNKOWN_FORMAT) {
        	LineProvider lLineProvider = lineProvider;

	        if (lLineProvider == null) {
	            lLineProvider = super.getLineProvider(fileStructure);
	        }
	        if (fileStructure == Constants.IO_GENERIC_CSV) {
	        	return new GenericCsvReader(lLineProvider);
	        }
	        return new UnknownFormatReader();
        } else {
			return super.getLineReader(fileStructure, lineProvider);
        }
	}

//	@Override
//	public AbstractLineWriter getLineWriter(int fileStructure) {
//		int structure = fileStructure;
//		if (structure == Constants.IO_UNKOWN_FORMAT) {
//			return
//		}
//	
//		return super.getLineWriter(structure);
//	}

	   
    /* (non-Javadoc)
	 * @see net.sf.JRecord.IO.AbstractLineIOProvider#isCopyBookFileRequired(int)
	 */ @Override
    public boolean isCopyBookFileRequired(int fileStructure) {
    	return ! ( fileStructure == Constants.IO_UNKOWN_FORMAT
    			|| fileStructure == Constants.IO_GENERIC_CSV);
    }
    
    
    /* (non-Javadoc)
	 * @see net.sf.JRecord.IO.AbstractLineIOProvider#getStructureName(int)
	 */ @Override
    public String getStructureName(int fileStructure) {
    	for (int i = 0; i < keys.length && keys[i] != Constants.NULL_INTEGER; i++) {
    		if (keys[i] == fileStructure) {
    			return externalNames[i];
    		}
    	}
    	return "";
    }


    /* (non-Javadoc)
	 * @see net.sf.JRecord.IO.AbstractLineIOProvider#getKey(int)
	 */
	@Override
	public int getKey(int idx) {
		return keys[idx];
	}


	/* (non-Javadoc)
	 * @see net.sf.JRecord.IO.AbstractLineIOProvider#getName(int)
	 */
	@Override
	public String getName(int idx) {
		return names[idx];
	}


	/**
	 * @see net.sf.JRecord.Common.AbstractManager#getNumberOfEntries()
	 */
	@Override
	public int getNumberOfEntries() {
		return numberOfEntries;
	}

	public static void register() {
		
		if (instance == null) {
			instance = new ReIOProvider();

			LineIOProvider.getInstance().register(instance);
		}
	}
	
	public static LineIOProvider getInstance() {
		register();
		return LineIOProvider.getInstance();
	}
}
